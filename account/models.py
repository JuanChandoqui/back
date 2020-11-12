from django.db import models
from django.contrib.auth.models import User


class AccountModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET(-1))
    first_name = models.CharField(max_length = 255, null=False)
    second_name = models.CharField(max_length = 255, null=False)
    email = models.CharField(max_length = 255, null=False)
    age = models.IntegerField()

    def __str__ (self):
        return self.user

'''
class AccountUser(models.Model):
    accountModel = models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 255, null=False)
    second_name = models.CharField(max_length = 255, null=False)
    email = models.CharField(max_length = 255, null=False)
    age = models.IntegerField()
     
    def __str__ (self):
        return self.accountModel
'''