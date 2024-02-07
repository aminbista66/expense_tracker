from django.urls import path
from .views import CategoryCreate, CategoryUpdateRetrieveDestroy, CategoryList

urlpatterns = [
    path("create/", CategoryCreate.as_view(), name="category_create"),
    path("<int:pk>/", CategoryUpdateRetrieveDestroy.as_view(), name="category_update_retrieve_destroy"),
    path("list/", CategoryList.as_view(), name="category_list")
]