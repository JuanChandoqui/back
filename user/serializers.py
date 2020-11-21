from rest_framework  import serializers

# Modelos
from .models import UserModel , UserProfile

class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('__all__') 

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('__all__')