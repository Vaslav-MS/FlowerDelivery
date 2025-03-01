# Generated by Django 5.1.6 on 2025-02-20 04:23

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True, verbose_name='Дата')),
                ('order_count', models.PositiveIntegerField(default=0, verbose_name='Количество заказов за день')),
                ('total_revenue', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Общий доход за день')),
                ('average_order_value', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Средний чек')),
                ('sold_units', models.PositiveIntegerField(default=0, verbose_name='Количество проданных единиц товара')),
            ],
            options={
                'verbose_name': 'Дневная аналитика',
                'verbose_name_plural': 'Дневная аналитика',
                'ordering': ['-date'],
            },
        ),
    ]
