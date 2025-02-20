from django.contrib import admin
from django.urls import path, include
from apps.home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('apps.accounts.urls')),
    path('catalog/', include('apps.catalog.urls', namespace='catalog')),
    path('cart/', include('apps.cart.urls')),
    path('orders/', include('apps.orders.urls')),
    path('reviews/', include('apps.reviews.urls')),
    path("analytics/", include("apps.analytics.urls", namespace="analytics")),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

