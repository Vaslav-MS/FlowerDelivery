from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.cart.models import Cart
from .models import Order, OrderItem
from asgiref.sync import async_to_sync
from apps.telegram_bot.notifications import send_order_notification

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.error(request, "Ваша корзина пуста.")
        return redirect("cart:view")

    order = Order.objects.create(user=request.user)

    for item in cart_items:
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

    cart_items.delete()

    async_to_sync(send_order_notification)(order)

    messages.success(request, "Ваш заказ успешно оформлен!")
    return redirect("orders:history")

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/history.html", {"orders": orders})


