from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('calender', views.calender, name= "calender"),
    path('fetch-calender/', views.fetch_calender, name="fetch_calender"),
    path('fetch-years/', views.fetch_years, name="fetch_years"),
    path('fetch_events/', views.fetch_events, name="fetch_events"),
    path('add-event/', views.add_event, name="add_event"),
    path('edit-event/', views.edit_event, name="edit_event"),
    path('delete-event/', views.delete_event, name="delete_event")
]