from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="files/")
    date = models.DateTimeField()
    parent_folder = models.ForeignKey('Folder', null=True, blank=True, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return self.name

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subfolders')

    def __str__(self):
        return self.name