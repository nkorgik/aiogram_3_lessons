import asyncio

from aiogram import types, Dispatcher, Bot
from aiogram.filters import Command


bot = Bot(token='5871111612:AAGb8PVxEX-50Y3RzJU2U7VPfmuEyqSbiBk')
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(msg: types.Message) -> None:
    """Handles start command"""
    
    reply_text = 'Hello World!'
    
    await msg.answer(
        text=reply_text
    )


async def main() -> None:
    """Entry Point to our program"""
    
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
