from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Аккаунт {user.username} создан и вы вошли в систему!")
            return redirect('home')
        else:
            messages.error(request, "Ошибка регистрации. Проверьте правильность введённых данных.")
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                messages.success(request, f"Добро пожаловать, {user.username}!")
                return redirect('home')
            else:
                messages.error(request, "Ошибка входа. Проверьте логин и пароль.")
        else:
            messages.error(request, "Ошибка входа. Проверьте введённые данные.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "Вы успешно вышли из системы.")
    return redirect('home')
