from django.shortcuts import render
from .models import Application

# Create your views here.

def index(request):
    applications = Application.objects.all()
    return render(request, 'index.html', {'apps': applications})