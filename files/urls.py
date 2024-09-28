from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('files', views.files, name= "files"),
    path('delete-file-folder/', views.delete_file_folder, name= "delete"),
    path('add-update-file-folder/', views.add_update_file_folder, name= "save")
]