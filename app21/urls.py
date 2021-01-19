from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.api),
    path('all_data', views.all_data, name='all_data'),
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/', views.CustomerDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)