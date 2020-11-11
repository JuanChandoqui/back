from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets
from .views import AccountUserModelView

urlpatterns = [
    re_path(r'^', AccountUserModelView.as_view())
]
