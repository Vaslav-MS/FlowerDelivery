from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Order
from asgiref.sync import async_to_sync
from apps.telegram_bot.notifications import send_status_change_notification

@receiver(pre_save, sender=Order)
def store_old_status(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Order.objects.get(pk=instance.pk)
            instance._old_status = old_instance.status
        except Order.DoesNotExist:
            instance._old_status = None

@receiver(post_save, sender=Order)
def notify_status_change(sender, instance, created, **kwargs):
    if created:
        # Новый заказ — уведомление о создании уже отправляется отдельно.
        return
    if hasattr(instance, '_old_status') and instance._old_status != instance.status:
        async_to_sync(send_status_change_notification)(instance)

