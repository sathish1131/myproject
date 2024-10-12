from django.shortcuts import render
from .models import Application, Notification
from django.http import JsonResponse

# Create your views here.

def index(request):
    applications = Application.objects.all()
    return render(request, 'index.html', {'apps': applications})

def notification(request):
    if request.method == 'POST':
        notification = request.POST.get('notification')
        if notification.lower() == 'true':
            status = True
        else:
            status = False
        enable_notification, created = Notification.objects.update_or_create(user=request.user, defaults={'status':status})
        enable_notification.save()
        return JsonResponse({'success': True})
    
def notification_status(request):
    if request.method == 'GET':
        notification = Notification.objects.filter(user=request.user)
        if notification:
            notification_status = notification[0].status
        else:
            notification_status = False
        return JsonResponse({'success': True, 'status': notification_status})