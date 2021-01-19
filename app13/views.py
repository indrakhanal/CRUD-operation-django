from django.shortcuts import render, HttpResponse
from .models import Person


def home(request):
    return render(request, 'app13/home.html')


def display_new_form(request):
    return render(request, 'app13/form1.html')


def receive_new_form(request):
    try:
        newid = request.GET.get('txt_id')
        name = request.GET.get('txt_name')
        address = request.GET.get('txt_address')
        person = Person(id=newid, full_name=name, contact_address=address)
        person.save()#save record on dattabase
        str1 = "<h3>student info</h3>"
        str1 = str1 + "<p> Id:"+str(id)+"</p>"
        str1 = str1 + "<p> nmae:"+name+"</p>"
        str1 = str1 + "<p> address:"+address+"</p>"
        str1 = str1 + "<p>Save Record Successfully</>"
    except:
        str1 = str1+"<p>Error to save record</p>"
    return HttpResponse(str1)


def display_search_form(request):
    return render(request, 'app13/record_search.html')


def search_person(request):
    id1 = request.GET.get('txt_id')
    try:
        person = Person.objects.get(id=id1)
        context = {
            'person': person

        }
        return render(request, 'app13/display_search_record.html', context)
    except:
        result = "Data Not Found"
        return render(request, 'app13/display_search_record.html', {'error': result})


def display_insert_form(request):
    return render(request, 'app13/display_insert_form.html')


def insert(request):
    try:
        pid = request.GET.get('txt_id')
        name = request.GET.get('txt_name')
        address = request.GET.get('txt_address')
        person = Person(id=pid, full_name=name, contact_address=address)
        person.save()
        return HttpResponse("<h5>successfully Inserted Data Into Database</h5>")
    except:
        return HttpResponse("<h5>Cannot Insert Data To The Database<h5/>")


def display_update_search_form(request):
    return render(request, 'app13/update_search_form.html')


def display_update_form(request):
    try:
        pid = request.GET.get('txt_id')
        person = Person.objects.get(id=pid)
        context = {
            'person': person

        }
        return render(request, 'app13/update_form.html', context)
    except:
        return HttpResponse('<h3 style="color:red;">Record Not Found</h3>')


def receive_update(request):
    try:
        pid = request.GET.get('txt_id')
        name = request.GET.get('txt_name')
        address = request.GET.get('txt_address')
        person = Person.objects.get(id=pid)
        person.full_name = name
        person.contact_address = address
        person.save()
        return HttpResponse("update Record Successfully<br/><a href='/'><h4>BACK</h4></a>")
    except:
        return HttpResponse("Error On Updating please check and try again")


def search_delete_form(request):
    return render(request, 'app13/delete_search.html')


def display_delete_form(request):
    pid = request.GET.get('txt_id')
    person = Person.objects.get(id=pid)
    context = {
        'person': person

    }
    return render(request, 'app13/delete_form.html', context)


def delete(request):
    pid = request.GET.get('txt_id1')
    person = Person.objects.get(id=pid)
    person.delete()
    return HttpResponse('Successfully Deleted')


def display_all(request):
    person = Person.objects.all()
    context ={
        'person': person
    }
    return render(request, 'app13/display_all.html', context)


