from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('enable-notification', views.notification, name="notification"),
    path('notification-status', views.notification_status, name="notification_status")
]