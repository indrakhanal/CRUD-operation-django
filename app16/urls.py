
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('news', views.NewsView.as_view()),
    path('details/<pk>', views.NewsDetails.as_view()),
    path('new', views.NewsCreate.as_view()),
    path('update/<pk>', views.NewsUpdate.as_view()),
    path('delete/<pk>', views.NewsUpdate.as_view()),
    path('sucess', views.sucess),
]