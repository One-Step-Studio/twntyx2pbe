from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import GameInstance
from .serializers import GameInstanceSerializer


# Create your views here.

class GameInstanceManage(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = GameInstance.objects.order_by('created')
    serializer_class = GameInstanceSerializer

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset().filter(code = pk)
        serializer = GameInstanceSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = GameInstanceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(status=400)