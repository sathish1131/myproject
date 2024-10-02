from django.shortcuts import render
import calender
import datetime

# Create your views here.

def calender(request):
    now = datetime.date.today()
    return render(request, 'calender.html', {'calender': now})