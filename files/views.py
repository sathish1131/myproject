from django.shortcuts import render
from .models import File, Folder
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.

def files(request):
    files = File.objects.filter(user=request.user)
    return render(request, 'files.html', {'files': list(files)})

def add_files(request):
    pass

def add_folders(request):
    pass
        
def delete_files(request):
    pass