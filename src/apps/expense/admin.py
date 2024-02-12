from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdminModel(admin.ModelAdmin):
    list_display = ('id', 'amount', 'description', 'created_at', 'created_by')
    list_filter = ('created_at', 'created_by')
    search_fields = ('description', 'created_by__username')
    date_hierarchy = 'created_at'
    list_per_page = 30
