from django.urls import path
from .views import checkout, order_history, repeat_order

app_name = 'orders'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('history/', order_history, name='history'),
    path('repeat/<int:order_id>/', repeat_order, name='repeat'),
]
