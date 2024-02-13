from .models import Expense
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpenseSerializer, ExpenseCreateUpdateSerializer, ExpenseReportSerializer
from django.db import models
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .filters import ExpenseFilter
from datetime import datetime
from django.utils import timezone

class ExpenseList(generics.ListAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    queryset = Expense.objects.none()
    filterset_class = ExpenseFilter

    def get_queryset(self):
        return Expense.objects.filter(created_by=self.request.user)
    
class ExpenseCreate(generics.CreateAPIView):
    serializer_class = ExpenseCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class ExpenseUpdateRetrieveDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(created_by=self.request.user)
    
    def get_serializer(self, *args, **kwargs):
        if self.request.method in ['PUT', 'PATCH']:
            return ExpenseCreateUpdateSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)
    
class ExpenseByCategoryReport(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="daterange_after",
                required=False,
                type=str,
                location=OpenApiParameter.QUERY,
                description="Start date",
            ),
            OpenApiParameter(
                name="daterange_before",
                required=False,
                type=str,
                location=OpenApiParameter.QUERY,
                description="Before date",
            ),
        ],
            responses={
                "application/json": {
                    "example": [{
                        "category__name": "Food",
                        "total_amount": 100}
                    ]
                }
            }
    )
    def get(self, request, *args, **kwargs):
        start_date = self.request.query_params.get("daterange_after", None) # type: ignore
        end_date = self.request.query_params.get("daterange_before", None) # type: ignore

        expenses = Expense.objects.filter(
            created_by=request.user,
        )

        if type(start_date) == str:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        if type(end_date) == str:
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        if not start_date:
            start_date = expenses.last().created_at if expenses.exists() else timezone.now()  # type: ignore
        if not end_date:
            end_date = expenses.first().created_at if expenses.exists() else timezone.now()  # type: ignore

        expenses = expenses.values('categories__name').annotate(
            total_amount=models.Sum('amount')
        ).order_by('-total_amount')
        
        data = {
            "expenses": expenses,
            "total": self.request.user.total_expense() # type: ignore
        }

        return Response(data)