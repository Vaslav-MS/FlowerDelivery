from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import DailyAnalytics

@staff_member_required
def analytics_dashboard(request):
    """
    Выводит список ежедневной аналитики (количество заказов, доход, средний чек, проданные единицы).
    Доступ ограничен для staff-пользователей (is_staff=True).
    """
    analytics_data = DailyAnalytics.objects.order_by("-date")
    return render(request, "analytics/dashboard.html", {"analytics_data": analytics_data})

