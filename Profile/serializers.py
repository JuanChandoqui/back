from rest_framework  import serializers

# Modelos
from Profile.models import ProfileModel
from Profile.models import ProfileUser

class ProfileModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')

class ProfileUserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('__all__')