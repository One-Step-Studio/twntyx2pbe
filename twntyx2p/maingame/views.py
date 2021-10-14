from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.parsers import JSONParser

import requests

from .models import UserGame
from .serializers import GameInstanceSerializer

import environments as env



class GameInstanceManage(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = UserGame.objects
    serializer_class = GameInstanceSerializer

    def list(self, request):
        my_id = request.user.id
        print(my_id + " requested info")
        try:
            req = requests.get(
                env.PROTOCOL + env.LOCAL_SERVER + env.GAME_API + my_id + env.CHECK_API + env.DEFAULT_ROUTE)
            print("info is " + str(req.json()))
            res = Response(req, status=status.HTTP_200_OK)
        except:
            res = Response(status=status.HTTP_204_NO_CONTENT)
        return res

    def retrieve(self, request, *args, **kwargs):
        my_id = request.user.id
        res = Response(status=status.HTTP_204_NO_CONTENT)
        parsed_req = JSONParser().parse(request)
        if parsed_req["info_type"] == "check_clock":
            try:
                req = requests.get(
                    env.PROTOCOL + env.LOCAL_SERVER + env.GAME_API + my_id + env.CHECK_API + env.DEFAULT_ROUTE)
                res = Response(req, status=status.HTTP_200_OK)
            except:
                pass

        return res


    def create(self, request, *args, **kwargs):
        pass
        # my_id = request.user.id
        # req = requests.get(env.PROTOCOL + env.LOCAL_SERVER + env.GAME_API + my_id)
        # serializer = GameInstanceSerializer(data=my_id)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        # return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
