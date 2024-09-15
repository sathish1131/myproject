from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)

class UserTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
