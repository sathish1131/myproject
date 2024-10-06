from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event

# Create your views here.

def calender(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_date = datetime.now().day
    decade_start = current_year-((current_year%10)-1)
    current_decade = f"{decade_start}-{decade_start+9}"
    cal = HTMLCalendar().formatmonth(current_year, current_month)
    years = list(range(decade_start,decade_start+10))
    decades = []
    for start_year in range(1981,2081,10):
        end_year = start_year + 9
        decades.append(f"{start_year}-{end_year}")
    months = list(calendar.month_name[1:13])
    return render(request, 'calender.html', {'calender': cal, 'current_month': current_month, 'current_year': current_year, 'current_date': current_date, 'current_decade': current_decade, 'months': months, 'years': years, 'decades': decades})

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
    
def fetch_events(request):
    if request.method == 'GET':
        event_year = request.GET.get('event_year')
        event_month = request.GET.get('event_month')
        event_date = request.GET.get('event_date')
        formated_date = datetime(year=int(event_year),month=int(event_month), day=int(event_date)).date()
        events = Event.objects.filter(user=request.user, date=formated_date)
        events_data = list(events.values('id', 'event', 'start_time', 'end_time'))
        return JsonResponse({'success':True, 'events': events_data})

def delete_event(request):
    if request.method == 'POST':
        event_id = request.POST.get('id')
        event = get_object_or_404(Event, user=request.user, id=event_id)
        event.delete()
        return JsonResponse({'success': True})

def edit_event(request):
    if request.method == 'POST':
        event_id = request.POST.get('id')
        event_event = request.POST.get('event')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        event = get_object_or_404(Event, user=request.user, id=event_id)
        event.event = event_event
        event.start_time = datetime.strptime(start_time, '%H:%M')
        event.end_time = datetime.strptime(end_time, '%H:%M')
        event.save()
        return JsonResponse({'success': True})
    
def add_event(request):
    if request.method == 'POST':
        event_event = request.POST.get('event')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        event_year = request.POST.get('event_year')
        event_month = request.POST.get('event_month')
        event_date = request.POST.get('event_date')
        formated_date = datetime(year=int(event_year),month=int(event_month), day=int(event_date)).date()
        startTimeList = start_time.split(':')
        endTimeList = end_time.split(':')
        start_time_obj = datetime(hour=int(startTimeList[0]), minute=int(startTimeList[1])).time()
        end_time_obj = datetime(hour=int(end_time[0]), minute=int(endTimeList[1])).time()
        print(start_time_obj, end_time_obj)
        event = Event(user=request.user, event=event_event, start_time=start_time_obj, end_time=end_time_obj, date=formated_date)
        event.save()
        return JsonResponse({'success': True})


