import http

from django.http import JsonResponse
from rest_framework import viewsets
from twntyx2p.accounts.models import User


class UserManage(viewsets.ModelViewSet):
    queryset = User.objects

    def create(self, request, *args, **kwargs):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
            new_user = User(email, password)
            new_user.save()
            return JsonResponse({"code": "success1"}, status=http.HTTPStatus.CREATED)
        except:
            return JsonResponse({"code": "error5"}, status=http.HTTPStatus.BAD_REQUEST)