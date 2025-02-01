from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def make_choice() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Red pill')
    kb.button(text='Blue pill')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
 
