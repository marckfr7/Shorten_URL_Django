from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import Shorten_URLForm
from .models import Cortar_url
import random, string
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token


# Create your views here.

def home(request):
    return render(request, 'home.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {"form": UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'])
                user.save()
                login(request, user)
                return redirect('my_url')
            except:
                return render(request, 'registro.html', {"form": UserCreationForm, "error": "El usuario ya existe"})
        return render(request, 'registro.html', {"form": UserCreationForm, "error": "Las contraseñas no sn correctas"})

def autenticacion(request):
    if request.method == 'GET':
        return render(request, 'autenticacion.html', {"form": AuthenticationForm})
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
           return render(request, 'autenticacion.html', {"form": AuthenticationForm, "error": "El usuario no existe"})
        else:
            login(request, user)
            return redirect('my_url') 
    
@login_required
def shorten_url(request):
    if request.method == 'GET':
        return render(request, 'shorten_url.html', {"form": Shorten_URLForm})
    else:
        short_url = "https://myapp/" + (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)))
        form = Shorten_URLForm(request.POST)
        new_form = form.save(commit=False)
        new_form.short_url = short_url
        new_form.user = request.user
        new_form.save()
        return redirect('my_url')

@login_required
def my_url(request):
    urls = Cortar_url.objects.filter(user=request.user)   
    return render(request, 'my_url.html', {"urls": urls})

@login_required
def mostrar_url(request, url_id):
    long_url = Cortar_url.objects.filter(pk=url_id).values('long_url').first()
    var = long_url['long_url']
    return redirect(var)

@login_required
def eliminar(request, url_id):
    dato = get_object_or_404(Cortar_url, pk=url_id, user=request.user)
    if request.method == 'POST':
        dato.delete()
        return redirect('my_url')

@login_required
def eliminar_user(request):
    user = User.objects.get(username=request.user).delete()
    logout(request)
    return redirect('home')

@login_required   
def salir(request):
    logout(request)
    return redirect('home')