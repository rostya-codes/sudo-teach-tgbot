from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalog')],
    [KeyboardButton(text='Cart'), KeyboardButton(text='Contacts')],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Select anything...')


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/@sudoteach')]
])

cars = ['Tesla', 'Mercedes', 'BMW']


async def inline_cars():
    """Transform list to inline keyboard using builder"""
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://www.youtube.com/@sudoteach'))
    return keyboard.adjust(2).as_markup()  # Количество кнопок в ряду
