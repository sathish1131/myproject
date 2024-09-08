from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    task = models.CharField(max_length=500)
    priority = models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'low')], default=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task for {self.user.first_name} (Priority: {self.priority})"