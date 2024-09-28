from django.shortcuts import render, get_object_or_404
from .models import File, Folder
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.

ALLOWED_FILE_TYPES = ['image/png', 'image/jpeg', 'application/pdf', 'text/plain', 'video/mp4', 'video/quicktime', 'video/webm', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']
MAX_FILE_SIZE = 10 * 1024 * 1024

def files(request):
    if request.method == 'GET':
        currentFolder = request.GET.get('folder_id')
        files = get_object_or_404(File, user= request.user, parent_folder= currentFolder)
        folder = get_object_or_404(Folder, user= request.user)
        return render(request, 'files.html', {'files': files, 'folders': folder})

def add_file(request):
    pass

def add_folder(request):
    pass

def update_file_folder(request):
    pass
        
def delete_file_folder(request):
    pass