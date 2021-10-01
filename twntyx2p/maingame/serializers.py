from rest_framework import serializers
from .models import GameInstance


class GameInstanceSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return GameInstance.objects.create(**validated_data)

    class Meta:
        model = GameInstance
        fields = ['id', 'created', 'total_time_run']
        read_only_fields = ('id', 'created')
