from django.shortcuts import render, get_object_or_404
from .models import Note
from django.utils import timezone
from django.http import JsonResponse

# Create your views here.

def notes(request):
    notes = Note.objects.filter(user=request.user).order_by('-updated_at')
    return render(request, 'notes.html', {'notes': notes})

def get_note(request):
    if(request.method == 'GET'):
        note_id = request.GET.get('id')
        note = get_object_or_404(Note, id=note_id, user=request.user)
        return JsonResponse({
            'name': note.name,
            'content': note.text
        })

def delete_note(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        note = get_object_or_404(Note, id=note_id, user=request.user)
        note.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed', 'message': 'Failed to delete note'})

def save_note(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        note_name = request.POST.get('name')
        note_content = request.POST.get('content')
        if not note_name or not note_content:
            return JsonResponse({'status': 'failed', 'message': 'Note name and content cannot be empty', 'status': 400})
        if note_id:
            note = get_object_or_404(Note, id=note_id, user=request.user)
            note.name = note_name
            note.text = note_content
            note.updated_at = timezone.now()
            note.save()
        else:
            note = Note(name= note_name, text= note_content, updated_at= timezone.now(), user= request.user)
            note.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})
