from django.db import models
from decimal import Decimal

class DailyAnalytics(models.Model):
    date = models.DateField(unique=True, verbose_name="Дата")
    order_count = models.PositiveIntegerField(default=0, verbose_name="Количество заказов за день")
    total_revenue = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'),
        verbose_name="Общий доход за день"
    )
    average_order_value = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'),
        verbose_name="Средний чек"
    )
    sold_units = models.PositiveIntegerField(default=0, verbose_name="Количество проданных единиц товара")

    def __str__(self):
        return f"{self.date} — Заказов: {self.order_count}, Доход: {self.total_revenue} ₽"

    class Meta:
        verbose_name = "Дневная аналитика"
        verbose_name_plural = "Дневная аналитика"
        ordering = ["-date"]
