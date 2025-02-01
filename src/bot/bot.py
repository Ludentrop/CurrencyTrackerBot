import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from handlers import process_choice
from config import settings


logging.basicConfig(level=logging.INFO)


async def main(token: str):
    bot = Bot(token=token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML)
              )

    dp = Dispatcher()
    dp.include_routers(process_choice.router)

    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    TOKEN = settings.TOKEN.get_secret_value()
    KEY = settings.KEY.get_secret_value()

    asyncio.run(main(TOKEN))
