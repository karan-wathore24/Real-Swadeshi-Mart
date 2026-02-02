from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'is_seller', 'is_customer', 'is_staff', 'is_superuser')
    list_filter = ('is_seller', 'is_customer', 'is_staff', 'is_superuser')
