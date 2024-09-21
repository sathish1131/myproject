from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('quotes', views.quotes, name= "quotes"),
    path('save_tags/', views.save_tags, name= "save_tags")
]