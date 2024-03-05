import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.handlers import router
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    """Main function to run bot"""
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':  # Конструкция позволяет запустить бота только когда выполняется этот файл, а не импортируемый
    logging.basicConfig(level=logging.INFO)  # log Используется только в процесе разработки так как на продакшене нагружает сервер
    try:
        asyncio.run(main())  # asyncio.run используется потому что функция main является асинхронной
        # Запустить асинхронную функцию вне асинхронной нельзя
    except KeyboardInterrupt:
        print('exit()')
