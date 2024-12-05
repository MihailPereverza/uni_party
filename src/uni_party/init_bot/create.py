import logging
from collections.abc import Awaitable, Callable
from typing import Any, Dict

from aiogram import BaseMiddleware, Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import TelegramObject
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import insert

from uni_party.handlers.main_menu import main_menu_router
from uni_party.handlers.start import start_router
from uni_party.repositories.postgres import pg_engine, pg_session
from uni_party.repositories.postgres.pg_tables.users import users_table
from uni_party.settings.base import settings


logger = logging.getLogger(__name__)


class EventInterceptorMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict,
    ) -> Awaitable[Any]:
        # Process the event here
        print(f"Intercepted event: {event}")
        return await handler(event, data)


class BotService:
    def __init__(self):
        logger.info(settings.tg_bot_token)

        self.engine = pg_engine
        self.session = pg_session

        self._bot = Bot(token=settings.tg_bot_token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))
        self._storage = MemoryStorage()
        self.db = Dispatcher(storage=self._storage)
        self._register_handlers()

    async def on_startup(self):
        async with self.engine.begin() as sa_conn:
            with open('./contrib/postgresql/schema.sql') as f:
                sql_commands = f.read().split(';')
                for command in sql_commands:
                    if not command.strip():
                        continue
                    sa_command = text(command)
                    await sa_conn.run_sync(lambda conn: conn.execute(sa_command))
                logger.info('Schema created')
        await self.set_admin_flags()

    async def set_admin_flags(self):
        async with pg_session() as session:
            admin_ids = settings.admin_ids
            # Добавляем или обновляем записи админов в базе данных
            for admin_id in admin_ids:
                query = (
                    insert(users_table)
                    .values(tg_id=admin_id, is_admin=True)
                    .on_conflict_do_update(
                        index_elements=[users_table.c.tg_id],
                        set_={users_table.c.is_admin: True}
                    )
                )
                await session.execute(query)
            await session.commit()
        logger.info('Admin flags set for all admins')

    def _register_handlers(self):
        self.db.include_router(start_router)
        self.db.include_router(main_menu_router)

    @property
    def aiogram_bot(self) -> Bot:
        return self._bot

    async def start_polling(self):
        self.db.update.middleware(EventInterceptorMiddleware())
        await self.on_startup()
        await self.db.start_polling(
            self._bot,
        )
