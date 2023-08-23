from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True)
    kb1 = InlineKeyboardButton('Регистрация', callback_data='btn_reg')
    kb2 = InlineKeyboardButton('Авторизация', callback_data='btn_auth')
    kb.add(kb1, kb2)
    return kb