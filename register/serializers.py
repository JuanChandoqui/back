from rest_framework  import serializers

from django.contrib.auth.models import models


# Modelos
class UserRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = models
        fields =  ['password', 'username', 'email']