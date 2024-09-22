from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    updated_at = models.DateTimeField(default=timezone.now)