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
    if request.method == 'GET':
        parent_folder_id = request.GET.get('parent_folder_id')
        if parent_folder_id != "":
            folders = Folder.objects.filter(user=request.user, parent_folder=parent_folder_id)
            files = File.objects.filter(user=request.user, parent_folder=parent_folder_id)
            return render(request, 'files.html', {'files': files, 'folders': folders})
        else:
            folders = Folder.objects.filter(user=request.user, parent_folder__isnull=True)
            files = File.objects.filter(user=request.user, parent_folder__isnull=True)
            return render(request, 'files.html', {'files': files, 'folders': folders})
    else:
        folders = Folder.objects.filter(user=request.user, parent_folder__isnull=True)
        files = File.objects.filter(user=request.user, parent_folder__isnull=True)
        return render(request, 'files.html', {'files': files, 'folders': folders})

def add_update_file_folder(request):
    if request.method == 'POST':
        file_id = request.POST.get('file_id')
        folder_id = request.POST.get('folder_id')
        parent_folder_id = request.POST.get('parent_folder_id')
        new_file = request.FILES.get('file')
        name = request.POST.get('name')
        unique_name = f"{name}_{uuid.uuid4()}"
        if file_id != "":
            file = get_object_or_404(File, user=request.user, id=file_id)
            if new_file:
                cloudinary_response = cloudinary.uploader.upload(new_file, public_id=unique_name)
                file.url = cloudinary_response['secure_url']
                file.name = name
                file.unique_name = cloudinary_response['public_id']
                file.save()
                JsonResponse({'success': True, 'message': 'File updated successfully'})
        elif folder_id != "":
            folder = get_object_or_404(Folder, user=request.user, id=folder_id)
            folder.name = name
            folder.save()
            JsonResponse({'success': True, 'message': 'Folder updated successfully'})
        else:
            if new_file:
                cloudinary_response = cloudinary.uploader.upload(new_file, public_id=unique_name)
                File.objects.create(user=request.user, name=name, parent_folder=parent_folder_id, url=cloudinary_response['secure_url'], unique_name=cloudinary_response['public_id'])
                JsonResponse({'success': True, 'message': 'File added successfully'})
            else:
                Folder.objects.create(user=request.user, name=name, parent_folder=parent_folder_id)
                JsonResponse({'success': True, 'message': 'Folder added successfully'})

def delete_file_folder(request):
    if request.method == 'POST':
        file_id = request.POST.get('file_id')
        folder_id = request.POST.get('folder_id')
        if file_id != "":
            file = get_object_or_404(File, user=request.user, id=file_id)
            file.delete()
            JsonResponse({'success': True, 'message': 'File deleted successfully'})
        elif folder_id != "":
            folder = get_object_or_404(Folder, user=request.user, id=folder_id)
            folder.delete()
            JsonResponse({'success': True, 'message': 'Folder deleted successfully'})
        JsonResponse({'success': False, 'message': 'Error fetching file or folder'})