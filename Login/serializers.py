from rest_framework  import serializers
from django.contrib.auth.models import User

'''
# Modelos
from .models import LoginModel

class LoginModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoginModel
        fields = ('__all__')
'''
class UserRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['password', 'username', 'email']
        #fields = '__all__'