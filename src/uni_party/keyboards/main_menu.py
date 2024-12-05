from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_main_menu(is_admin=False):
    keyboard = [
        [KeyboardButton(text="Получить расписание")],
        [KeyboardButton(text="Записаться на мероприятие")],
        [KeyboardButton(text="Квиз")]
    ]

    if is_admin:
        keyboard.append([KeyboardButton(text="Отослать уведомление")])

    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)
