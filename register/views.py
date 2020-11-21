from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserRegisterSerializers

# Create your views here.
class RegisterView(ObtainAuthToken):   
    #PUT REQUEST
    def put(self, request, *args, **kwargs):
        try:
            user = self.kwargs.get('pk')
        except user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserRegisterSerializers(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)