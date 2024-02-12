from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    total_expense = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "total_expense"
        )