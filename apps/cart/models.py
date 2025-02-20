from django.db import models
from django.contrib.auth import get_user_model
from apps.catalog.models import Product

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    def total_price(self):
        """Общая стоимость товаров в корзине"""
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

