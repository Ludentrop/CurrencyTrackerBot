import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from config import settings


TOKEN = settings.TOKEN.get_secret_value()
KEY = settings.KEY.get_secret_value()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
