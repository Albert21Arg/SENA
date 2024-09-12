from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def saludar(request):
    print("Hola mundo...!")
    return HttpResponse("Hola SENA..!")

def index(request):
    return render(request, "index.html")

def saludar_personalizado(request, nombre):
    return HttpResponse(f"Hola {nombre}")

def suma(request, num1, num2):
    return HttpResponse(f"Resultado: {num1+num2}")

def suma_formulario(request):
    return HttpResponse(request, "prueba.html")

def procesar_suma(request):
    num1 = int(request.POST.get("num1"))
    num2 = int(request.POST.get("num2"))
    return HttpResponse(f"Resultado: {num1+num2}")
    