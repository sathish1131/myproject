from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import TodoList
import json

# Create your views here.

def todo(request):
    tasks = TodoList.objects.filter(user = request.user)
    return render(request, 'todo.html', {'tasks': tasks})



def add_task(request):
    if request.method == 'POST':
        priority = request.POST.get('priority')
        description = request.POST.get('description')
        status = request.POST.get('status')
        task = TodoList(priority=priority, description=description, status=status, user=request.user)
        task.save()
        return JsonResponse({'status': 'success', 'tasks': {
            'task_id': task.id,
            'priority': task.priority,
            'description': task.description,
            'status': task.status
        }})
    return JsonResponse({'status': 'error'}, status=400)

def edit_task(request):
    if(request.method == 'GET'):
        task_id = request.GET.get('task_id')
        task = get_object_or_404(TodoList, id=task_id)
        return JsonResponse({
            'status': task.status,
            'priority': task.priority,
            'description': task.description
        })
    elif(request.method == 'POST'):
        task_id = request.POST.get('task_id')
        task = get_object_or_404(TodoList, id=task_id)
        task.status = request.POST.get('status')
        task.priority = request.POST.get('priority')
        task.description = request.POST.get('description')
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})



def delete_task(request):
    if(request.method == 'POST'):
        try:
            data = json.loads(request.body)
            task_id = data.get('task_id')
            if not task_id:
                return JsonResponse({'success': False, 'error': 'Task Id is Missing'}, status=400)
            task = get_object_or_404(TodoList, id= task_id)
            task.delete()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    return JsonResponse({'success': False, 'error': 'Invalid Request Method'}, status=405)

