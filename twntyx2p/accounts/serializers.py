from rest_framework import serializers
from twntyx2p.accounts.models import User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        min_length=6, write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'password', 'is_staff',
            'is_active', 'created_at')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)