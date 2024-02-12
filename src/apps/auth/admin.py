from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')