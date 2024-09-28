from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('files', views.files, name= "files"),
    path('add-file/', views.add_file, name= "add_file"),
    path('add-folder/', views.add_folder, name= "add_folder"),
    path('delete-file-folder/', views.delete_file_folder, name= "delete"),
    path('update-file-folder/', views.update_file_folder, name= "update")
]