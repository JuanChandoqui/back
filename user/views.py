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

from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

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


class UserProfileView(ObtainAuthToken):
    #GET REQUEST
    def get(self, request, format=None):  
        usernames = UserProfile.objects.all()
        serializer = UserProfileSerializers(usernames, many=True)
        return Response(serializer.data)
    
    #PUT REQUEST
    def put(self, request, *args, **kwargs):
    #def put(request, pk, format=None):
        try:
            user = self.kwargs.get('pk')
            #user = UserProfile.objects.get(pk=pk)
        except user.DoesNotExist:
        #except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializers(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #DELETE REQUEST
    def delete(pk, format=None):
        try:
            user = UserProfile.objects.get(id=pk) #<----- pk lo reconoce como objeto, no como int, si se coloca un entero, lo reconocera
        except UserProfile.DoesNotExist:         
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
@api_view(['DELETE'])
def deleteUserView(request, pk, format=None):
    try:
        user = UserProfile.objects.get(id=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
