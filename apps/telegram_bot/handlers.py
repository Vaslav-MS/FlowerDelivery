import logging
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from asgiref.sync import sync_to_async

from apps.orders.models import Order
from apps.analytics.models import DailyAnalytics
from config import ADMIN_CHAT_ID

router = Router()
logger = logging.getLogger(__name__)

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Здравствуйте. Я бот Flower Delivery. Используйте /help для справки.')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply(
        'Доступные команды:\n'
        '/start - Запуск бота\n'
        '/help - Помощь\n'
        '/status &lt;order_id&gt; &lt;new_status&gt; - Изменить статус заказа (например, /status 123 delivered)\n'
        '/analytics - Показать аналитические данные (доступно только администратору)'
    )

@router.message(Command('status'))
async def cmd_status(message: Message):
    args = message.text.split()[1:]
    if len(args) < 2:
        await message.answer('Использование: /status &lt;order_id&gt; &lt;new_status&gt;')
        return

    try:
        order_id = int(args[0])
        new_status = args[1].lower()

        valid_statuses = dict(Order.STATUS_CHOICES).keys()
        if new_status not in valid_statuses:
            await message.answer(f'Неверный статус. Допустимые статусы: {", ".join(valid_statuses)}')
            return

        try:
            order = await sync_to_async(Order.objects.get)(id=order_id)
        except Order.DoesNotExist:
            await message.answer('Заказ с таким ID не найден.')
            return

        order.status = new_status
        await sync_to_async(order.save)()
        await message.answer(f'Статус заказа {order_id} изменен на {new_status}.')
    except ValueError:
        await message.answer('Неверный формат order_id. Укажите корректное число.')

@router.message(Command('analytics'))
async def cmd_analytics(message: Message):
    if str(message.from_user.id) != ADMIN_CHAT_ID:
        await message.answer('Нет доступа.')
        return

    analytics_qs = DailyAnalytics.objects.order_by('-date')[:7]
    analytics_data = await sync_to_async(list)(analytics_qs)
    if not analytics_data:
        await message.answer('Аналитических данных пока нет.')
        return

    text = 'Аналитика за последние 7 дней:\n'
    for day in analytics_data:
        text += (
            f'Дата: {day.date} | Заказов: {day.order_count} | '
            f'Доход: {day.total_revenue} ₽ | Средний чек: {day.average_order_value} ₽ | '
            f'Продано: {day.sold_units}\n'
        )
    await message.answer(text)

@router.message()
async def cmd_echo(message: Message):
    await message.answer('Команда не распознана. Используйте /help для справки.')

def register_handlers(dp):
    dp.include_router(router)

