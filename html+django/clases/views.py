from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def productos(request):
    return render(request, "productos.html")

def nosotros(request):
    return render(request, "nosotros.html")

def contactos(request):
    return render(request, "contactos.html")

def login(request):
    return render(request, "login.html")

def registro(request):
    return render(request, "registro.html")

def restaurar(request):
    return render(request, "restaurar.html")