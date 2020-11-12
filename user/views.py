from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from .models import UserModel, UserProfile
from .serializers import UserModelSerializers, UserProfileSerializers

class UserModelView(ObtainAuthToken, APIView):
    def get(self, request, format=None):  
        #usernames = [user.age for user in ProfileUser.objects.all()]   
        usernames = UserModel.objects.all()
        serializer = UserModelSerializers(usernames, many=True)
        return Response(serializer.data)

    #POST REQUEST
    def post(self, request, format=None):
        serializer = UserModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(ObtainAuthToken, APIView):
    #GET REQUEST
    def get(self, request, format=None):  
        #usernames = [user.age for user in ProfileUser.objects.all()]   
        usernames = UserProfile.objects.all()
        serializer = UserProfileSerializers(usernames, many=True)
        return Response(serializer.data)

    #POST REQUEST
    def post(self, request, format=None):
        serializer = UserProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #PUT REQUEST
    def put(self, request, *args, **kwargs):
        try:
            user = self.kwargs.get('pk')
        except user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializers(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    #DELETE REQUEST
    def delete(self, request, *args, **kwargs):
        user = self.kwargs.get('pk')         
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Va a invocar a una clase de serializador
