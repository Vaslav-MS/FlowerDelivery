from django.contrib import admin
from django.urls import path, include
from apps.home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('apps.accounts.urls')),
    path('catalog/', include('apps.catalog.urls', namespace='catalog')),
    path('orders/', include('apps.orders.urls')),
    path('reviews/', include('apps.reviews.urls')),
    path('analytics/', include('apps.analytics.urls')),
]
