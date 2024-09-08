from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    priority_choices = [(1, 'Urjent'), (2, 'Normal'), (3, 'Optional')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    task = models.CharField(max_length=500)
    priority = models.IntegerField(priority_choices, default=3)