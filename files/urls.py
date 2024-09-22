from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('files', views.files, name= "files"),
    path('addfiles/', views.add_files, name= "add_files"),
    path('addfolders/', views.add_folders, name= "add_folders"),
    path('deletefiles/', views.delete_files, name= "delete_files")
]