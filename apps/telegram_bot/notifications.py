import os
import logging
from aiogram import Bot
from aiogram.client.bot import DefaultBotProperties
from asgiref.sync import sync_to_async
from config import TELEGRAM_BOT_TOKEN, ADMIN_CHAT_ID

logger = logging.getLogger(__name__)

async def send_order_notification(order):
    token = TELEGRAM_BOT_TOKEN
    if not token:
        logger.error('TELEGRAM_BOT_TOKEN не найден.')
        return
    if not ADMIN_CHAT_ID:
        logger.error('ADMIN_CHAT_ID не задан.')
        return

    total = await sync_to_async(order.total_price)()
    message = (
        f'<b>Новый заказ!</b>\n'
        f'ID заказа: {order.id}\n'
        f'Пользователь: {order.user.username}\n'
        f'Сумма: {total} ₽\n'
        f'Статус: {order.status}'
    )
    try:
        async with Bot(token=token, default=DefaultBotProperties(parse_mode='HTML')) as bot:
            await bot.send_message(chat_id=ADMIN_CHAT_ID, text=message)
    except Exception as e:
        logger.exception(f'Ошибка отправки уведомления: {e}')
