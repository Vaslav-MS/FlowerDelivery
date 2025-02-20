from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from apps.catalog.models import Product

def product_reviews(request, product_id):
    """Вывод всех отзывов к товару"""
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    form = ReviewForm()

    return render(request, "reviews/product_reviews.html", {"product": product, "reviews": reviews, "form": form})

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, "Ваш отзыв был добавлен!")
            return redirect("reviews:product_reviews", product_id=product.id)
        else:
            messages.error(request, "Ошибка при добавлении отзыва. Проверьте введенные данные.")

    return redirect("reviews:product_reviews", product_id=product.id)

