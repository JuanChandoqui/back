from django.urls import path, re_path
from rest_framework import routers, serializers, viewsets
from .views import RegisterView

urlpatterns = [
    re_path(r'^', RegisterView.as_view()),
]