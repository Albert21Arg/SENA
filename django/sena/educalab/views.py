from django.http import HttpResponse
from django.shortcuts import render

def saludar(request):
    print("Hola mundo...!")
    return HttpResponse("Hola SENA..!")

def index(request):
    return render(request, "index.html")

def saludar_personalizado(request, nombre):
    return HttpResponse(f"Hola {nombre}")

def suma(request, num1, num2):
    return HttpResponse(f"Resultado: {num1 + num2}")

def suma_formulario(request):
    return render(request, "prueba.html")

def procesar_suma(request):
    if request.method == "POST":
        num1 = int(request.POST.get("num1", 0))
        num2 = int(request.POST.get("num2", 0))
        return HttpResponse(f"Resultado: {num1 + num2}")

def registro(request):
    if request.method == "POST":
        nombre = str(request.POST.get("nombre"))
        correo = str(request.POST.get("correo"))
        return render(f"se creo corretamente: {nombre} con correo {correo}")
    else:
        # Manejar el caso GET
        return render(request, 'registro.html')