from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import CustomAuthToken, RegisterView


urlpatterns = [
    re_path(r'^login_url', CustomAuthToken.as_view()),
    re_path(r'^register_url', RegisterView.as_view()),
]