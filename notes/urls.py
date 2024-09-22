from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.notes, name= "notes"),
    path('save-note', views.save_note, name= "save_note"),
    path('delete-note', views.delete_note, name= "delete_note")
]