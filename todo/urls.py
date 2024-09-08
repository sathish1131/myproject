from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todo', views.todo, name= "todo"),
    path('add-task/', views.add_task, name= "add_task")
]