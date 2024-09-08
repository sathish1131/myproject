from django.shortcuts import render
from django.http import JsonResponse
from .models import TodoList

# Create your views here.

def todo(request):
    tasks = TodoList.objects.filter(user = request.user)
    return render(request, 'todo.html', {'tasks': tasks})



def add_task(request):
    if request.method == 'POST':
        priority = request.POST.get('priority')
        task = request.POST.get('description')
        status = request.POST.get('status') == 'on'
        TodoList.objects.create(priority=priority, task=task, status=status, user=request.user)
        return JsonResponse({'message': 'Task added successfully'}, status=200)
    return JsonResponse({'error': 'Invalid Request'}, status=400)