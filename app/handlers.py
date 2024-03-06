from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb


router = Router()  # router object


@router.message(CommandStart())  # Ловим команду /start
async def cmd_start(message: Message):
    await message.reply(f'''Hello!
Your user id: {message.from_user.id}
firstname: {message.from_user.first_name}
lastname: {message.from_user.last_name}''', reply_markup=kb.main_cb)


@router.message(Command('help'))  # Ловим команду /help
async def get_help(message: Message):
    await message.answer('It\'s /help command.', reply_markup=kb.settings)


@router.message(F.text == 'How are you?')  # Ловим текст
async def how_are_you(message: Message):
    await message.answer('OK!', reply_markup=await kb.inline_cars())


@router.message(F.photo)  # Ловим фото
async def get_id_of_photo(message: Message):
    await message.answer(f'id of photo: {message.photo[-1].file_id}')  # [-1] - это самое лучшее качество


@router.message(Command('get_photo'))  # /get_photo
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAIBKmXnitcsaFF_GmG0iYBLY8v2pyebAAK41zEblXw4S1uVAfgYrd2AAQADAgADeQADNAQ',
                               caption='It\'s Ivan Zolo2004 and n3koglai')  # Также вместо id можно указывать ссылку на фото


# Callbacks

@router.callback_query(F.data == 'catalog')  # Ловим указанный callback
async def catalog_callback(callback: CallbackQuery):
    """Callback controller to show catalog"""

    # Чтобы не загружалось просто так оставить пустым, или можно вывести всплывающее сообщение указав текст
    await callback.answer('You chose catalog.', show_alert=True)  # show_alert=True для появления окошка с кнопкой ОК

    await callback.message.answer('It\'s callback response')


@router.callback_query(F.data == 'cars')  # Ловим указанный callback
async def cars_callback(callback: CallbackQuery):
    """Callback controller to display cars buttons and show alert"""
    await callback.answer('cars', show_alert=True)
    await callback.message.edit_text('cars', reply_markup=await kb.inline_cars())  # Edit text


@router.callback_query(F.data == 'contacts')  # Ловим указанный callback
async def contacts_callback(callback: CallbackQuery):
    """Callback controller to display contacts buttons"""
    await callback.answer('')
    await callback.message.edit_text('contacts', reply_markup=kb.contacts)  # Edit text


@router.callback_query(F.data == 'back_to_start')  # Ловим указанный callback
async def back_to_start_callback(callback: CallbackQuery):
    """Callback controller to back to start"""
    await callback.answer('')
    await callback.message.edit_text('back to start', reply_markup=kb.main_cb)  # Edit text
