from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

# Modelos
from Profile.models import ProfileModel

#Serializers
from Profile.serializers import ProfileModelSerializers
from Profile.serializers import ProfileUserModelSerializers

#Views
class ProfileModelView(APIView):
    def post(self, request, format=None):
        #Va a invocar a una clase de serializador
        serializer = ProfileModelSerializers(data = request.data, context = {'request': request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response("Error Formato")


class ProfileUserModelView(APIView):
    def post(self, request, format=None):
        #Va a invocar a una clase de serializador
        serializer = ProfileUserModelSerializers(data = request.data, context = {'request': request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response("Error Formato")