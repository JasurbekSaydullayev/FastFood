from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)
    type = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ("id", "phone_number", "email", "first_name", "last_name", 'password', 'type', 'created_at')
