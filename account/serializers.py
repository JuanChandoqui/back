from rest_framework  import serializers

# Modelos
from .models import AccountsModel , AccountUser

class AccountModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = AccountsModel
        fields = ('__all__')

class AccountUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = ('__all__')