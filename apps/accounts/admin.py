from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'phone', 'address', 'is_staff', 'is_superuser')
    search_fields = ('username', 'phone', 'address')
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('phone', 'address')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone', 'address', 'password1', 'password2'),
        }),
    )

