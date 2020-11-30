from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.decorators import api_view

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from .models import UserModel, UserProfile
from .serializers import UserModelSerializers, UserProfileSerializers


class UserModelView(ObtainAuthToken):
    
    def get(self, request, format=None):   
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

    def put(self, request, *args, **kwargs):
        try:
            user = self.kwargs.get('pk')
        except user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserModelSerializers(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(ObtainAuthToken):
    #GET REQUEST
    def get(self, request, format=None):  
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

    '''
    #POST REQUEST
    def put(self, request, format=None):
        id = request.data.get("id")  
        print(id)
        user = UserProfile.objects.get(id=id)
        serializer = UserProfileSerializers(user, data=request.data)
            
        if serializer.is_valid():
            serializer.save()
            return Response("Update successful")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''
    def put(self, request):
        id = request.data.get("id")
        print(id)       
        user = UserProfile.objects.get(id=id)
        user.first_name = request.data.get("first_name")
        user.last_name = request.data.get("last_name")
        user.age = request.data.get("age")
        user.email = request.data.get("email")
        user.save()      
        return Response("Exito")
    
    #DELETE REQUEST
    def delete(self, request, *args, **kwargs):
        id = request.data.get("id")  
        print(id)          
        user = UserProfile.objects.get(id=id) 

        if(user != None):
            user.delete()
            return Response("Usuario Eliminado")       
        return Response("Usuario no encontrado")