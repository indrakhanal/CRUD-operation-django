from django.shortcuts import render
from .forms import PersonEntryForm
from .models import Person

# Create your views here.

def display_form(request):
    form1 = PersonEntryForm()
    return render(request, 'app15/form1.html',{'form1':form1})

def receive_form(request):
    result = ""
    if request.method=='POST':
        form1 = PersonEntryForm(request.POST)
        if form1.is_valid():
            person = form1.save(commit=False)
            person.save()
            result="Save record successfully"
    return render(request, 'app15/display1.html', {'result': result})

def display_all(request):
    persons = Person.objects.all()
    return render(request, 'app15/display2.html', {'persons':persons})