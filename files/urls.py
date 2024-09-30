from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('files', views.files, name= "files"),
    path('fetch-folder-files/<int:parent_folder_id>', views.fetch_folders_files, name= "fetch"),
    path('delete-folder/', views.delete_folder, name= "delete_folder"),
    path('delete-file/', views.delete_file, name= "delete_file"),
    path('edit-folder/', views.edit_folder, name= "edit_folder"),
    path('add-folder/', views.add_folder, name= "add_folder"),
    path('add-file/', views.add_file, name= "add_file")
]