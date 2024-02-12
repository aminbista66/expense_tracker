from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from rest_framework.views import APIView
from rest_framework.response import Response

class Ping(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self, request):
        return Response("pong")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path('auth/', include('src.apps.auth.urls')),
    path('category/', include('src.apps.category.urls')),
    path('expense/', include('src.apps.expense.urls')),
    path('ping/', Ping.as_view())
]