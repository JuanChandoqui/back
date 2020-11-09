from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone
# Create your models here.
class ProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET(-1))
    address = models.CharField(max_length = 255, null=False)
    creadted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.user
'''
# Create your models here.
class ProfileTwo(models.Model):
    ProfileModel = models.ForeignKey(ProfileModel, on_delete = models.SET(-1))
    address = models.CharField(max_length = 255, null=False)
    creadted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.ProfileModel
'''

class ProfileUser(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET(-1))
    first_name = models.CharField(max_length = 255, null=False)
    second_name = models.CharField(max_length = 255, null=False)
    email = models.CharField(max_length = 255, null=False)
    age = models.IntegerField(default=timezone)
     
    def __str__ (self):
        return self.user