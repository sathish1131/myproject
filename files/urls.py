from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('files', views.files, name= "files"),
    path('savefiles/', views.save_files, name= "save_files"),
    path('deletefiles/', views.delete_files, name= "delete_files")
]