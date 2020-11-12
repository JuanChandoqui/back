from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets
from .views import AccountModelView

urlpatterns = [
    re_path(r'^accountModel_url', AccountModelView.as_view())
]
