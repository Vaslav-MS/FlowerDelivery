import os
import os
from django.db import models
from django.db.models import Avg
from django.apps import apps  # Импортируем apps вместо Review напрямую

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def average_rating(self):
        """Вычисляет средний рейтинг товара по отзывам"""
        Review = apps.get_model("reviews", "Review")  # Получаем модель Review через apps
        avg_rating = Review.objects.filter(product=self).aggregate(avg_rating=Avg("rating"))["avg_rating"]
        return round(avg_rating, 1) if avg_rating else None

    def save(self, *args, **kwargs):
        """Удаляет старое изображение при загрузке нового"""
        try:
            old_instance = Product.objects.get(id=self.id)
            if old_instance.image and old_instance.image != self.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        except Product.DoesNotExist:
            pass

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

