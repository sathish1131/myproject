from django.db import models

# Create your models here.

class TodoList(models.Model):
    status = models.BooleanField(default=False)
    text = models.CharField(max_length=500)