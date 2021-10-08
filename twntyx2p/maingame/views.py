from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.parsers import JSONParser

import requests

from .models import UserGame
from .serializers import GameInstanceSerializer

import environments as env

# Create your views here.
from ..accounts.models import User


class GameInstanceManage(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    user = User.id
    queryset = UserGame.objects.get(user_id=user)
    serializer_class = GameInstanceSerializer

    def list(self, request):
        try:
            req = requests.get(
                env.PROTOCOL + env.LOCAL_SERVER + env.GAME_API + self.user + env.CHECK_API + env.DEFAULT_ROUTE)
            res = Response(req, status=status.HTTP_200_OK)
        except:
            res = Response(status=status.HTTP_204_NO_CONTENT)
        return res

    def retrieve(self, request, *args, **kwargs):
        res = Response(status=status.HTTP_204_NO_CONTENT)
        parsed_req = JSONParser().parse(request)
        if parsed_req["info_type"] == "check_clock":
            try:
                req = requests.get(
                    env.PROTOCOL + env.LOCAL_SERVER + env.GAME_API + self.user + env.CHECK_API + env.DEFAULT_ROUTE)
                res = Response(req, status=status.HTTP_200_OK)
            except:
                pass

        return res


    def create(self, request, *args, **kwargs):
        data = self.user
        if self.queryset:
            req = requests.get(
                env.PROTOCOL + env.LOCAL_SERVER + env.GAME_API + self.user)
            return JsonResponse(req)
        serializer = GameInstanceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
