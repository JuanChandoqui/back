from rest_framework  import serializers

# Modelos
from Profile.models import ProfileUser

class ProfileUserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('__all__')