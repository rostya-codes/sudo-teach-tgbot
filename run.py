import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())  # Ловим команду /start
async def cmd_start(message: Message):
    await message.reply(f'''Hello!
Your user id: {message.from_user.id}
firstname: {message.from_user.first_name}
lastname: {message.from_user.last_name}''')


@dp.message(Command('help'))  # Ловим команду /help
async def get_help(message: Message):
    await message.answer('It\'s /help command.')


@dp.message(F.text == 'How are you?')  # Ловим текст
async def how_are_you(message: Message):
    await message.answer('OK!')


@dp.message(F.photo)  # Ловим фото
async def get_id_of_photo(message: Message):
    await message.answer(f'id of photo: {message.photo[-1].file_id}')  # [-1] - это самое лучшее качество


@dp.message(Command('get_photo'))  # /get_photo
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAIBKmXnitcsaFF_GmG0iYBLY8v2pyebAAK41zEblXw4S1uVAfgYrd2AAQADAgADeQADNAQ',
                               caption='It\'s Ivan Zolo2004 and n3koglai')  # Также вместо id можно указывать ссылку на фото


async def main():
    """Main function to run bot"""
    await dp.start_polling(bot)


if __name__ == '__main__':  # Конструкция позволяет запустить бота только когда выполняется этот файл, а не импортируемый
    logging.basicConfig(level=logging.INFO)  # log Используется только в процесе разработки так как на продакшене нагружает сервер
    try:
        asyncio.run(main())  # asyncio.run используется потому что функция main является асинхронной
        # Запустить асинхронную функцию вне асинхронной нельзя
    except KeyboardInterrupt:
        print('exit()')
