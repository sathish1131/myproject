from django.shortcuts import render
from django.http import JsonResponse
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

def fetch_calender(request):
    if request.method == 'GET':
        month = request.GET.get('month')
        year = request.GET.get('year')
        cal = HTMLCalendar().formatmonth(int(year), int(month))
        return JsonResponse({'success': True, 'calender': cal})
    
def fetch_years(request):
    if request.method == 'GET':
        decade = request.GET.get('selected_decade')
        split_decade = decade.split('-')
        years = []
        for year in range(int(split_decade[0]), int(split_decade[1])+1,1):
            years.append(year)
        return JsonResponse({'success': True, 'years': years})
