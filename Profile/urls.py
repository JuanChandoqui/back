from django.urls import path, re_path

from Profile import views

urlpatterns = [
    re_path(r'^profileUser_url', views.ProfileUserModelView.as_view())
]