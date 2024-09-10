from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todo', views.todo, name= "todo"),
    path('add-task/', views.add_task, name= "add_task"),
    path('edit-task/', views.edit_task, name= "edit_task"),
    path('delete-task/', views.delete_task, name= "delete_task")
]