from django.shortcuts import render

# Create your views here.

def files(request):
    return render(request, 'files.html')