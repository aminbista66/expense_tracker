from rest_framework import serializers
from .models import Category
from src.apps.auth.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

