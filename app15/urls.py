from django.contrib import admin
from django.urls import path
from .views import display_form as idx1
from .views import receive_form as idx2
from .views import display_all as idx3
urlpatterns = [
    path('display_form', idx1),
    path('receive_form', idx2),
    path('display_all', idx3),
]