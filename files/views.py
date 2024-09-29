import cloudinary.uploader
from django.shortcuts import render, get_object_or_404
from .models import File, Folder
from django.http import JsonResponse
import cloudinary
import uuid

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
    folders = Folder.objects.filter(user=request.user, parent_folder=None).order_by('name')
    files = File.objects.filter(user=request.user, parent_folder=None).order_by('name')
    return render(request, 'files.html', {'files': files, 'folders': folders})
        
    
def fetch_folders_files(request):
    if request.method == 'GET':
        parent_folder_id = request.GET.get('parent_folder_id')
        if parent_folder_id == '':
            parent_folder = None
        else:
            parent_folder = get_object_or_404(Folder, user=request.user, id=parent_folder_id)
        folders = Folder.objects.filter(user=request.user, parent_folder=parent_folder).order_by('name')
        files = File.objects.filter(user=request.user, parent_folder=parent_folder).order_by('name')
        return render(request, 'files.html', {'files': files, 'folders': folders})

def delete_folder(request):
    if request.method == 'POST':
        folder_id = request.POST.get('folder_id')
        folder = get_object_or_404(Folder, user=request.user, id=folder_id)
        folder.delete()
        return JsonResponse({'success': True, 'message': 'Folder deleted successfully'})

def delete_file(request):
    if request.method == 'POST':
        file_id = request.POST.get('file_id')
        file = get_object_or_404(File, user=request.user, id=file_id)
        file.delete()
        return JsonResponse({'success': True, 'message': 'File deleted successfully'})
    
def edit_folder(request):
    if request.method == 'POST':
        folder_id = request.POST.get('folder_id')
        folder_name = request.POST.get('folder_name')
        parent_folder_id = request.POST.get('parent_folder_id')
        if parent_folder_id == "":
            parent_folder = None
        else:
            parent_folder = get_object_or_404(Folder, user=request.user, id=parent_folder_id)
        filtered_folder = Folder.objects.filter(user=request.user, name=folder_name, parent_folder=parent_folder).exclude(id=folder_id)
        if filtered_folder.exists():
            return JsonResponse({'success': False, 'message': 'Folder name already exists'})
        folder = get_object_or_404(Folder, user=request.user, id=folder_id)
        folder.name = folder_name
        folder.save()
        return JsonResponse({'success': True, 'message': 'Folder updated successfully'})

def add_folder(request):
    if request.method == 'POST':
        folder_name = request.POST.get('folder_name')
        parent_folder_id = request.POST.get('parent_folder_id')
        if parent_folder_id == "":
            parent_folder = None
        else:
            parent_folder = get_object_or_404(Folder, user=request.user, id=parent_folder_id)
        if Folder.objects.filter(user=request.user, name=folder_name, parent_folder=parent_folder).exists():
            return JsonResponse({'success': False, 'message': 'Folder name already exists'})
        Folder.objects.create(user=request.user, name=folder_name, parent_folder=parent_folder)
        return JsonResponse({'success': True, 'message': 'Folder added successfully'})
    
def add_file(request):
    if request.method == 'POST':
        file_name = request.POST.get('name')
        file = request.FILES.get('file')
        unique_file_name = f"{file_name}_{uuid.uuid4()}"
        parent_folder_id = request.POST.get('parent_folder_id')
        if parent_folder_id == "":
            parent_folder = None
        else:
            parent_folder = get_object_or_404(Folder, user=request.user, id=parent_folder_id)

        # logic for file type and size restriction
        cloudinary_response = cloudinary.uploader.upload(file, public_id=unique_file_name)
        secure_url = cloudinary_response['secure_url']
        File.objects.create(user=request.user, name=file_name, url=secure_url, unique_name=unique_file_name, parent_folder=parent_folder)
        return JsonResponse({'success': True, 'message': 'File added successfully'})