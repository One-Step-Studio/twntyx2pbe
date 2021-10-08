from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r'instance', views.GameInstanceManage)

urlpatterns = [
    path('', include(router.urls)),
]