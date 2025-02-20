from django.apps import AppConfig

class AnalyticsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.analytics"
    verbose_name = "Аналитика"

    def ready(self):
        # Импортируем сигналы, чтобы они подключились при старте
        import apps.analytics.signals
