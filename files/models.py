from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subfolders')
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    unique_name = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to="uploads/")
    updated_at = models.DateTimeField(default=timezone.now)
    parent_folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    content_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

