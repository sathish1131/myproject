from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="pending")
    description = models.CharField(max_length=500)
    priority = models.CharField(max_length=50, default="low")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task for {self.user.first_name} (Priority: {self.priority})"