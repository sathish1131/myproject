from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
import datetime

# Create your views here.

def calender(request):
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_day = datetime.datetime.now().day
    decade_start = current_year-((current_year%10)-1)
    current_decade = f"{decade_start}-{decade_start+9}"
    cal = HTMLCalendar().formatmonth(current_year, current_month)
    years = list(range(decade_start,decade_start+10))
    decades = []
    for start_year in range(1981,2081,10):
        end_year = start_year + 9
        decades.append(f"{start_year}-{end_year}")
    months = list(calendar.month_name[1:13])
    return render(request, 'calender.html', {'calender': cal, 'current_month': current_month, 'current_year': current_year, 'current_day': current_day, 'current_decade': current_decade, 'months': months, 'years': years, 'decades': decades})