from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AccountUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 255, null=False)
    second_name = models.CharField(max_length = 255, null=False)
     
    def __str__ (self):
        return self.user