from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from uni_party.keyboards.main_menu import create_main_menu
from uni_party.repositories.postgres.users import pg_upsert_user

start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message):
    user = await pg_upsert_user(tg_id=message.from_user.id, username=message.from_user.username)

    keyboard = create_main_menu(is_admin=user.is_admin)
    await message.answer('Главное меню:', reply_markup=keyboard)
