from django.shortcuts import render
from django.http import HttpResponse

def catalog_home(request):
    return HttpResponse("<h1>Каталог товаров</h1><p>Скоро здесь появится список товаров.</p>")

