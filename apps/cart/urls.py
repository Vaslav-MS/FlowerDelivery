from django.urls import path
from .views import cart_view, add_to_cart, remove_from_cart

app_name = "cart"

urlpatterns = [
    path("", cart_view, name="view"),
    path("add/<int:product_id>/", add_to_cart, name="add"),
    path("remove/<int:cart_id>/", remove_from_cart, name="remove"),
]

