from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
import datetime

# Create your views here.

def calender(request):
    now = datetime.date.today()
    cal = HTMLCalendar().formatmonth(now.year, now.month)
    return render(request, 'calender.html', {'calender': cal})