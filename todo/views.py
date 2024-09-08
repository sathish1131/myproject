from django.shortcuts import render
from .models import TodoList

# Create your views here.

def todo(request):
    list = TodoList.objects.all()
    return render(request, 'todo.html', {'list': list})