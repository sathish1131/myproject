from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subfolders')
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        constraints = [
            models.UniqueConstraint(fields=[
                'name',
                'parent_folder_id',
                'user'
            ], name="unique_folder_name")
        ]

    def __str__(self):
        return self.name

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(default='')
    public_id = models.CharField(max_length=255, default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        constraints = [
            models.UniqueConstraint(fields=[
                'name',
                'parent_folder_id',
                'user'
            ], name="unique_file_name")
        ]

    def __str__(self):
        return self.name

