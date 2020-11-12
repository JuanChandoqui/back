from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets
from Profile import views

urlpatterns = [
    #re_path(r'^profileUser_url', views.ProfileUserModelView.as_view()),
    re_path(r'^profileModel_url', views.ProfileUserModelView.as_view())
]
