from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET(-1))
    address = models.CharField(max_length = 255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.user

class UserProfile(models.Model):
    userModel = models.ForeignKey(UserModel, on_delete=models.SET(-1))
    first_name = models.CharField(max_length = 255, null=False)
    last_name = models.CharField(max_length = 255, null=False)
    email = models.CharField(max_length = 255, null=False)
    age = models.IntegerField()
     
    def __str__ (self):
        return self.userModel