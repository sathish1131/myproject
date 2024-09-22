from django.shortcuts import render, get_object_or_404
from .models import Note
from django.utils import timezone
from django.http import JsonResponse

# Create your views here.

def notes(request):
    notes = Note.objects.filter(user=request.user).order_by('-updated_at')
    return render(request, 'notes.html', {'notes': notes})

def delete_note(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        note = get_object_or_404(Note, id=note_id, user=request.user)
        note.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed', 'message': 'Failed to delete note'})

def save_note(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        note_content = request.POST.get('note')
        response_data = {}
        if name or note_content:
            note, created = Note.objects.get_or_create(user=request.user, name=name, defaults={
                'note': note_content,
                'updated_at': timezone.now()
            })
            if created:
                response_data['message'] = 'Note added successfully'
            else:
                note.name = name
                note.note = note_content
                note.updated_at = timezone.now()
                note.save()
                response_data['message'] = 'Note updated successfully'
            return JsonResponse(response_data)
    return JsonResponse({'status': 'failed', 'message': 'Failed to add or update note'})
