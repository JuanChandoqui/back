from .views import RegisterAPI
from django.urls import path, re_path

urlpatterns = [
    path('api/v1/register/', RegisterAPI.as_view(), name='register'),
]