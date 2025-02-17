from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('catalog:list')  # редирект на страницу каталога (пример)
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    # Реализуйте логику аутентификации
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('catalog:list')
