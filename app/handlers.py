from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import app.keyboards as kb


router = Router()  # router object


@router.message(CommandStart())  # Ловим команду /start
async def cmd_start(message: Message):
    await message.reply(f'''Hello!
Your user id: {message.from_user.id}
firstname: {message.from_user.first_name}
lastname: {message.from_user.last_name}''', reply_markup=kb.main)


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
