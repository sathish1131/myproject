from django.db import models

# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=500)