from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.TextField()
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.event