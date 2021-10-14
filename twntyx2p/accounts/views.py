import http
import traceback

from django.http import JsonResponse
from rest_framework import viewsets
from twntyx2p.accounts.models import User
from twntyx2p.accounts.serializers import UserSerializer


class UserManage(viewsets.ModelViewSet):
    queryset = User.objects

    def create(self, request, *args, **kwargs):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
            serializer = UserSerializer(data={"email":email, "password": password})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse({"code": "success1"}, status=http.HTTPStatus.CREATED)
        except Exception:
            traceback.print_exc()
            return JsonResponse({"code": "error5"}, status=http.HTTPStatus.BAD_REQUEST)