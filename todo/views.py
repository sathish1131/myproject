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
    pass



def delete_task(request):
    pass

