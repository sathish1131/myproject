from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subfolders')
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('name', 'user', 'parent_folder')

    def __str__(self):
        return self.name

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    unique_name = models.CharField(max_length=255, unique=True)
    url = models.URLField()
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('name', 'user', 'parent_folder')
    
    def __str__(self):
        return self.name

