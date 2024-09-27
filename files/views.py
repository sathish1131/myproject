from django.shortcuts import render, get_object_or_404
from .models import File, Folder
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.

def files(request):
    if request.method == 'GET':
        currentFolder = request.GET.get('folder_id')
        files = get_object_or_404(File, user= request.user, parent_folder= currentFolder)
        folder = get_object_or_404(Folder, user= request.user)
        return render(request, 'files.html', {'files': files, 'folders': folder})

def add_files(request):
    pass

def add_folders(request):
    pass
        
def delete_files(request):
    pass