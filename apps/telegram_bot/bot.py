import asyncio
import logging
import django

django.setup()

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apps.telegram_bot import handlers
from apps.telegram_bot.utils import get_bot_token

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    token = get_bot_token()
    if not token:
        logger.error("Telegram bot token not found. Set TELEGRAM_BOT_TOKEN environment variable.")
        return

    bot = Bot(token=token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    handlers.register_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await bot.close()

if __name__ == '__main__':
    asyncio.run(main())

