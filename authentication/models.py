from django.db import models
from django.contrib.auth.models import User




class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100,default='1')
    email = models.EmailField(max_length=100,default='djanfo@ayth.com')
    password = models.CharField(max_length=100)
