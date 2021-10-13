from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ['phone', 'email', 'password','created_at', 'realm_name', 'is_active']
        read_only_fields = ('id', 'created_at')
