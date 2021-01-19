from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('createImage/', views.createImage),
    path('createCSV/', views.createCSV),
    path('createPDF/', views.createPDF),
]