from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=500)

class Notification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)