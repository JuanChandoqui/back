'''
from rest_framework  import serializers

# Modelos
from .models import LoginModel

class LoginModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoginModel
        fields = ('__all__')
'''