from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    address = models.CharField(max_length=255, blank=True, verbose_name="Адрес")

    def __str__(self):
        return self.username
