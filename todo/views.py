from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import TodoList

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
            'id': task.id,
            'priority': task.priority,
            'description': task.description,
            'status': task.status
        }})
    return JsonResponse({'status': 'error'}, status=400)

def edit_task(request, task_id):
    if(request.method == 'GET'):
        task = get_object_or_404(TodoList, id=task_id)
        return JsonResponse({
            'task': {
                'id': task.id,
                'status': task.status,
                'priority': task.priority,
                'description': task.description
            }
        })
    elif(request.method == 'POST'):
        task = get_object_or_404(TodoList, id=task_id)
        task.priority = request.POST.get('priority')
        task.status = request.POST.get('status')
        task.description = request.POST.get('description')
        task.save()
        return JsonResponse({
            'task': {
                'id': task.id,
                'status': task.status,
                'priority': task.priority,
                'description': task.description
            }
        })



def delete_task(request, task_id):
    if(request.method == 'POST'):
        task = get_object_or_404(TodoList, id = task_id)
        task.delete()
        return JsonResponse({'success': True})

