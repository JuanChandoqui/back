from rest_framework  import serializers

# Modelos
from .models import AccountUser

class AccountUserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = ('__all__')