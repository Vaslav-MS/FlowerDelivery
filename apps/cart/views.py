from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart
from apps.catalog.models import Product

@login_required
def cart_view(request):
    """Отображает корзину пользователя"""
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, "cart/cart.html", {"cart_items": cart_items, "total_price": total_price})

@login_required
def add_to_cart(request, product_id):
    """Добавляет товар в корзину"""
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} добавлен в корзину!")
    return redirect("catalog:list")

@login_required
def remove_from_cart(request, cart_id):
    """Удаляет товар из корзины"""
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()

    messages.success(request, "Товар удалён из корзины.")
    return redirect("cart:view")

