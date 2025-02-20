from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
import logging
from apps.orders.models import Order

logger = logging.getLogger(__name__)

async def cmd_start(message: types.Message):
    await message.reply("Здравствуйте. Я бот Flower Delivery. Используйте /help для справки.")

async def cmd_help(message: types.Message):
    await message.reply(
        "Доступные команды:\n"
        "/start - Запуск бота\n"
        "/help - Помощь\n"
        "/status <order_id> <new_status> - Изменить статус заказа (например, /status 123 delivered)"
    )

async def cmd_status(message: types.Message):
    args = message.get_args().split()
    if len(args) < 2:
        await message.reply("Использование: /status <order_id> <new_status>")
        return

    try:
        order_id = int(args[0])
        new_status = args[1].lower()
        valid_statuses = dict(Order.STATUS_CHOICES).keys()
        if new_status not in valid_statuses:
            await message.reply(f"Неверный статус. Допустимые статусы: {', '.join(valid_statuses)}")
            return

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            await message.reply("Заказ с таким ID не найден.")
            return

        order.status = new_status
        order.save()
        await message.reply(f"Статус заказа {order_id} изменен на {new_status}.")
    except ValueError:
        await message.reply("Неверный формат order_id. Укажите корректное число.")

async def cmd_echo(message: types.Message):
    await message.reply("Команда не распознана. Используйте /help для справки.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, Command("start"))
    dp.register_message_handler(cmd_help, Command("help"))
    dp.register_message_handler(cmd_status, Command("status"))
    dp.register_message_handler(cmd_echo)

