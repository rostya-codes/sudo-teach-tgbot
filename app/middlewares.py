from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable


class TestMiddleware(BaseMiddleware):
    """ Test middleware to print() before and after the result """

    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],  # работает только для inner
                       event: TelegramObject,  # можно указать Message or CallbackData
                       data: Dict[str, Any]) -> Any:
        print('Действия до обработчика')
        result = await handler(event, data)
        print('Действия после обработчика')
        return result
