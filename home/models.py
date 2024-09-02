from django.db import models

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=500)