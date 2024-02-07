import django_filters
from .models import Expense

class ExpenseFilter(django_filters.FilterSet):
    daterange = django_filters.DateFromToRangeFilter(field_name="created_at")
    class Meta:
        model = Expense
        fields = ["daterange",]