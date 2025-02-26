from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.cart.models import Cart
from .models import Order, OrderItem
from asgiref.sync import async_to_sync
from apps.telegram_bot.notifications import send_order_notification
from .forms import OrderCheckoutForm


@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.error(request, 'Ваша корзина пуста.')
        return redirect('cart:view')

    # Если заказ повторяется, берем предыдущий адрес доставки из сессии
    initial_data = {}
    if 'repeat_order_delivery_address' in request.session:
        initial_data['delivery_address'] = request.session.pop('repeat_order_delivery_address')

    if request.method == 'POST':
        form = OrderCheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart_items:
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            cart_items.delete()
            async_to_sync(send_order_notification)(order)
            messages.success(request, 'Ваш заказ успешно оформлен!')
            return redirect('orders:history')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = OrderCheckoutForm(initial=initial_data)

    return render(request, 'orders/checkout.html', {'form': form, 'cart_items': cart_items})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/history.html', {'orders': orders})


@login_required
def repeat_order(request, order_id):
    old_order = get_object_or_404(Order, id=order_id, user=request.user)

    # Очистить корзину для пользователя
    Cart.objects.filter(user=request.user).delete()

    # Добавить товары из старого заказа в корзину
    for item in old_order.items.all():
        Cart.objects.create(user=request.user, product=item.product, quantity=item.quantity)

    # Если в старом заказе указан адрес доставки, сохраняем его для предзаполнения формы
    if old_order.delivery_address:
        request.session['repeat_order_delivery_address'] = old_order.delivery_address

    messages.success(request, 'Заказ повторен! Проверьте корзину и оформите заказ.')
    return redirect('orders:checkout')
