from django.contrib.auth.models import AbstractUser
from django.db.models import Sum


class User(AbstractUser):
    pass

    def total_expense(self):
        return self.expenses.aggregate(total_expense=Sum("amount"))["total_expense"] or 0  # type: ignore
