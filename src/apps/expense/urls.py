from django.urls import path
from .views import ExpenseCreate, ExpenseUpdateRetrieveDestroy, ExpenseList, ExpenseByCategoryReport

urlpatterns = [
    path("create/", ExpenseCreate.as_view(), name="expense_create"),
    path("<int:pk>/", ExpenseUpdateRetrieveDestroy.as_view(), name="expense_update_retrieve_destroy"),
    path("list/", ExpenseList.as_view(), name="expense_list"),
    path("report/", ExpenseByCategoryReport.as_view(), name="expense_by_category_report")
]