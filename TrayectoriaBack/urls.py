from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from Profile.views import ProfileUserModelView

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^api/v1/login/', include('Login.urls')),
    re_path(r'^api/v1/profile/', include('Profile.urls')),
    re_path(r'^api/v1/account/', include('account.urls')),
    re_path(r'^api/v1/user/', include('user.urls')),
]