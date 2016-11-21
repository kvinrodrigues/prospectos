from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required

def autenticar(request):
    logout(request)
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('inicio:home'))
    return render(request, 'inicio/autenticar.html')

@login_required
def menu(request):
    return render(request, 'inicio/menu.html')

def home(request):
    return render(request,'inicio/home.html')


def salir(request):
    logout(request)
    return render(request, 'inicio/autenticar.html')

def view_menu(request):

    return