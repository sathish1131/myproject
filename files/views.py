import cloudinary.api
import cloudinary.uploader
from django.shortcuts import render, get_object_or_404, redirect
from .models import File, Folder
from django.http import JsonResponse
import cloudinary.uploader
import os
# Create your views here.

def files(request):
    folders = Folder.objects.filter(user=request.user, parent_folder=None).order_by('name')
    files = File.objects.filter(user=request.user, parent_folder=None).order_by('name')
    return render(request, 'files.html', {'files': files, 'folders': folders})
        
    
def fetch_folders_files(request, parent_folder_id):
    if request.method == 'GET':
        if parent_folder_id == '':
            parent_folder = None
        else:
            parent_folder = get_object_or_404(Folder, user=request.user, id=parent_folder_id)
        folders = Folder.objects.filter(user=request.user, parent_folder=parent_folder).order_by('name')
        files = File.objects.filter(user=request.user, parent_folder=parent_folder).order_by('name')
        return render(request, 'files.html', {'files': files, 'folders': folders})
    
def back(request, folder_id):
    if request.method == 'GET':
        current_folder = get_object_or_404(Folder, user=request.user, id=folder_id)
        parent_folder = current_folder.parent_folder
        if parent_folder:
            folders = Folder.objects.filter(user=request.user, parent_folder=parent_folder).order_by('name')
            files = File.objects.filter(user=request.user, parent_folder=parent_folder).order_by('name')
        else:
            return redirect('files')
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
        file_type = get_file_type(file.url)
        cloudinary.uploader.destroy(file.public_id, resource_type=file_type)
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
        uploaded_file = request.FILES.get('file')
        parent_folder_id = request.POST.get('parent_folder_id')
        if parent_folder_id == "":
            parent_folder = None
        else:
            parent_folder = get_object_or_404(Folder, user=request.user, id=parent_folder_id)
        if File.objects.filter(user=request.user, name=file_name, parent_folder=parent_folder).exists():
            return JsonResponse({'success': False, 'message': 'File name already exists'})
        file = cloudinary.uploader.upload(uploaded_file, resource_type="auto")
        File.objects.create(user=request.user, name=file_name, parent_folder=parent_folder, url= file['url'], public_id=file['public_id'])
        return JsonResponse({'success': True, 'message': 'File added successfully'})



def get_file_type(file_url):
    _, file_extension = os.path.splitext(file_url)
    if file_extension in ['.jpg', '.jpeg', '.png']:
        return 'image'
    elif file_extension in ['.mp4', '.mov']:
        return 'video'
    else:
        return 'raw'
        