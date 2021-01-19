from django.urls import path, include
from .views import display_login as idx1
from .views import do_login as idx2
from .views import check_session as idx3

urlpatterns = [
    path('login', idx1),
    path('do_login', idx2),
    path('check_seesion', idx3),
]