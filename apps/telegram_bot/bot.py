import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flower_delivery.settings")

import django
django.setup()

import asyncio
import logging

from config import TELEGRAM_BOT_TOKEN

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties

from . import handlers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    token = TELEGRAM_BOT_TOKEN
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN не найден. Установите переменную окружения.")
        return

    storage = MemoryStorage()

    bot = Bot(token=token, default=DefaultBotProperties(parse_mode="HTML"))

    dp = Dispatcher(storage=storage)
    handlers.register_handlers(dp)

    await bot.delete_webhook(drop_pending_updates=True)

    logger.info("Бот запущен (aiogram 3.x). Нажмите Ctrl+C для остановки.")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

