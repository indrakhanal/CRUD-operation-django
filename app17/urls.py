from django.urls import path, include
from .views import f1 as idx1

urlpatterns = [
    path('', idx1),
]