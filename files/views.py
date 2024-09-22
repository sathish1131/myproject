from django.shortcuts import render
from .models import File
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.

def files(request):
    files = File.objects.filter(user=request.user)
    return render(request, 'files.html', {'files': list(files)})

def save_files(request):
    if request.method == 'POST':
        files = request.POST.getlist('files')
        for file in files:
            file_name = file['filename']
            files_to_upload = file['file']
            file_upload, created = File.objects.update_or_create(user=request.user, name= file_name, defaults={
                'file': files_to_upload,
                'date': timezone.now
            })
            file_upload.save()
        return JsonResponse({'status': True, 'message': f'{len(files)} files saved successfully'})
        
def delete_files(request):
    if request.method == 'POST':
        file_ids = request.POST.getlist('file_ids')
        for file_id in file_ids:
            files = File.objects.filter(id__in=file_id, user=request.user)
            deleted_count = files.delete()
            return JsonResponse({'status': True, 'message': f'{deleted_count} files deleted successfully'})
        return JsonResponse({'status': False, 'message': 'Failed to delete file(s)'})