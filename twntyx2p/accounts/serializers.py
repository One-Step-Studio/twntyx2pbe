from rest_framework import serializers
from twntyx2p.accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        min_length=8, required=True)

    class Meta:
        model = User
        fields = (
            'email', 'password')

    def create(self, validated_data):
        print(**validated_data)
        return User.objects.create_user(**validated_data)