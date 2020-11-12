from rest_framework  import serializers

# Modelos
from .models import AccountModel

class AccountModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ('__all__')