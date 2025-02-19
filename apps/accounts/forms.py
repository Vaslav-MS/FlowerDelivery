from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    phone = forms.CharField(required=True, label="Телефон", widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(required=True, label="Адрес", widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'address', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'password1': forms.PasswordInput(attrs={"class": "form-control"}),
            'password2': forms.PasswordInput(attrs={"class": "form-control"}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
