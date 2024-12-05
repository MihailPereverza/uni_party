from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from uni_party.keyboards.main_menu import create_main_menu
from uni_party.repositories.postgres.users import pg_get_user_by_tg_id


main_menu_router = Router()


@main_menu_router.message(Command('main_menu'))
async def show_main_menu(message: Message):
    user = await pg_get_user_by_tg_id(message.from_user.id)
    if not user:
        await message.answer("Пользователь не найден\\.")
        return

    keyboard = create_main_menu(user.is_admin)
    await message.answer("Главное меню\\:", reply_markup=keyboard)
