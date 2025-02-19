from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    """Отображение списка всех товаров"""
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, "catalog/product_list.html", {"categories": categories, "products": products})

def product_detail(request, product_id):
    """Отображение детальной страницы товара"""
    product = get_object_or_404(Product, id=product_id)
    return render(request, "catalog/product_detail.html", {"product": product})
