import http

from django.http import HttpResponse, JsonResponse


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from twntyx2p.accounts.models import User
from twntyx2p.accounts.serializers import UserSerializer


class UserManage(viewsets.ModelViewSet):
    queryset = User.objects
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            phone = request.data.get("phone")
            email = request.data.get("email")
            password = request.data.get("password")
            new_user = User(phone=phone,email=email,password=password,realm_name="Hell")
            new_user.save()
            return JsonResponse({"code": "success1"}, status=http.HTTPStatus.CREATED)
        except:
            return JsonResponse({"code": "error5"}, status=http.HTTPStatus.BAD_REQUEST)