from django.urls import path
from .views import product_list, product_detail

app_name = "catalog"

urlpatterns = [
    path("", product_list, name="list"),
    path("<int:product_id>/", product_detail, name="detail"),
]

