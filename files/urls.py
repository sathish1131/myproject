from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('files', views.files, name= "files"),
    path('add-file-folder/', views.add_file_folder, name= "add"),
    path('delete-file-folder/', views.delete_file_folder, name= "delete"),
    path('update-file-folder/', views.update_file_folder, name= "update")
]