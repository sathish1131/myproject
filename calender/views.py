from django.shortcuts import render

# Create your views here.

def calender(request):
    return render(request, 'calender.html')