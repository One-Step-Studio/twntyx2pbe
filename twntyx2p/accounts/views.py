import http

import random
from django.http import HttpResponse, JsonResponse
import vonage

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from twntyx2p.accounts.models import User
from twntyx2p.accounts.serializers import UserSerializer

client = vonage.Client(key="71518046", secret="tfuFRb1ydnNGhyKO")
sms = vonage.Sms(client)

class UserManage(viewsets.ModelViewSet):
    queryset = User.objects
    serializer_class = UserSerializer

    def send_sms_to(self, phone, code):
        responseData = sms.send_message(
            {
                "from": "Vonage APIs",
                "to": "972543381232",
                "text": "A text message sent using the Nexmo SMS API",
            }
        )
        if responseData["messages"][0]["status"] == "0":
            return True
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
            return False

    def create(self, request, *args, **kwargs):
        try:
            phone = request.data.get("phone")
            print(phone)
            email = request.data.get("email")
            password = request.data.get("password")
            new_user = User(phone=phone,email=email,password=password,realm_name="Hell")
            print(new_user.phone)
            new_user.save_sms_code(random.randint(10000, 99999))
            new_user.save()
            print(new_user.phone_code)
            sms_status = self.send_sms_to(phone=phone)
            return JsonResponse({"code":sms_status}, status=http.HTTPStatus.CREATED)
        except:
            return JsonResponse({"code":"error5"}, status=http.HTTPStatus.BAD_REQUEST)

class UserActions(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        action = request.data.get("action")
        sms_code = request.data.get("code")
        success = False
        if action == "activate" and sms_code:
            query : User = self.queryset.filter(request.data.get("id")).first()
            success = query.activate(sms_code)
        return JsonResponse({"success": success})