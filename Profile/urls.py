from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import ProfileUserModelView

urlpatterns = [
    re_path(r'^profile_url', ProfileUserModelView.as_view())
]
