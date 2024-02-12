from src.apps.category.models import Category
from .models import Expense
from rest_framework import serializers
from src.apps.category.serializers import CategorySerializer

class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Expense
        fields = "__all__"

class ExpenseCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        exclude = ['created_by']

    def create(self, validated_data):
        category_datas = validated_data.pop('categories', [])
        expense = Expense.objects.create(
            created_by=self.context['request'].user,
            **validated_data
        )

        for category in category_datas:
            expense.categories.add(category)
        return expense