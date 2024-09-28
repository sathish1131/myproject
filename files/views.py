from django.shortcuts import render, get_object_or_404
from .models import File, Folder
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.

ALLOWED_FILE_TYPES = [
    'image/png',
    'image/jpeg',
    'application/pdf',
    'text/plain',
    'video/mp4',
    'video/quicktime',
    'video/webm',
    'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    ]
MAX_FILE_SIZE = 10 * 1024 * 1024

def files(request):
    
    return render(request, 'files.html', {'files': '', 'folders': ''})

def add_file_folder(request):
    pass

def update_file_folder(request):
    pass
        
def delete_file_folder(request):
    pass