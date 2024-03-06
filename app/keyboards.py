from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalog')],
    [KeyboardButton(text='Basket'), KeyboardButton(text='Contacts')],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Select anything...')

main_cb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Catalog', callback_data='catalog')],
    [InlineKeyboardButton(text='Cars', callback_data='cars'),
     InlineKeyboardButton(text='Contacts', callback_data='contacts')]
])

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


contacts = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='contact 1', url='https://www.youtube.com/@sudoteach'),
        InlineKeyboardButton(text='contact 2', url='https://www.youtube.com/@sudoteach'),
    ],
    [
        InlineKeyboardButton(text='contact 3', url='https://www.youtube.com/@sudoteach'),
        InlineKeyboardButton(text='contact 4', url='https://www.youtube.com/@sudoteach'),
    ],
    [
        InlineKeyboardButton(text='back', callback_data='back_to_start'),
    ],
])
