from django.urls import path, re_path
from django.conf.urls import include, url
from rest_framework import routers, serializers, viewsets
from .views import UserModelView, UserProfileView #, deleteUserView

#from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    re_path(r'^userModel_url', UserModelView.as_view()),
    re_path(r'^userProfile_url', UserProfileView.as_view()),
    #path('userProfile_url/delete/<int:id>', deleteUserView),
]

#urlpatterns = format_suffix_patterns(urlpatterns)