from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def f1(request):
    # All Users
    users = User.objects.all()  # get all users
    print(len(users))
    for user in users:
        print(user)

    #New Use
    #user1 = User.objects.create_user(username='admin1', password='admin1', email='info@mail.com')
    #user1.first_name = 'Krishna'
    #user1.last_name = 'Aryal'
    #user1.save()

    # Update Password
    user2 = User.objects.get(username='admin1')
    user2.set_password('admin123')
    user2.save()

    user = authenticate(username='admin', password='admin')
    if user is not None:
        # A backend authenticated the credentials
        print("TRUE")
    else:
        # No backend authenticated the credentials
        print("FALSE")

    return HttpResponse("Hello")