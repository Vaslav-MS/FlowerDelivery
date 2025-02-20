from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from apps.orders.models import Order
from apps.analytics.models import DailyAnalytics

@receiver(post_save, sender=Order)
def update_daily_analytics(sender, instance, **kwargs):
    """
    Обновляет ежедневную аналитику, когда заказ становится 'delivered'.
    """
    if instance.status == "delivered":
        # Вычисляем дату (можно взять дату заказа, но чаще берут текущую)
        date_for_analytics = instance.created_at.date()
        # Ищем или создаём запись DailyAnalytics на нужную дату
        daily, created = DailyAnalytics.objects.get_or_create(date=date_for_analytics)

        # Увеличиваем счётчик заказов
        daily.order_count += 1

        # Считаем сумму заказа и количество единиц
        order_total = sum(item.total_price() for item in instance.items.all())
        sold_units = sum(item.quantity for item in instance.items.all())

        # Обновляем поля
        daily.total_revenue += order_total
        daily.sold_units += sold_units

        # Пересчитываем средний чек
        if daily.order_count > 0:
            daily.average_order_value = daily.total_revenue / daily.order_count

        daily.save()

