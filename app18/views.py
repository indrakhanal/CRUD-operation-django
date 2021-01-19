from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def display_login(request):
    return render(request, "app18/form1.html")


def do_login(request):
    usr = request.GET.get('txt_user')
    pas = request.GET.get('txt_pass')
    if usr=='admin' and pas=='admin':
        print("Login success")
        request.session['user_name']=usr
        return render(request, 'app18/display_result.html', {'user':usr, 'flag':True})
    else:
        return render(request, 'app18/form1.html')


def check_session(request):
    if request.session.has_key('user_name'):
        user_name=request.session.has_key('user_name')
        return render(request, 'app18/display_result.html', {'user': user_name, 'flag': True})
    else:
        return render(request, 'app18/display_result.html', {'user': 'NA', 'flag': False})