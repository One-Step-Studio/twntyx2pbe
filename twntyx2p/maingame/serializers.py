from rest_framework import serializers
from .models import UserGame


class GameInstanceSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return UserGame.objects.create(**validated_data)

    class Meta:
        model = UserGame
        fields = ['user_id', 'created', 'total_time_run']
        read_only_fields = ('user_id', 'created')
