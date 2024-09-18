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
    return render(request, "form-suma.html")

def procesar_suma(request):
    if request.method == "POST":
        num1 = int(request.POST.get("num1", 0))
        num2 = int(request.POST.get("num2", 0))
        return HttpResponse(f"Resultado: {num1 + num2}")

def registrarse(request):
    return render(request, "form-registro.html")

def registro(request):
    if request.method == "POST":
        nombre = str(request.POST.get('nombre',0))
        telefono = request.POST.get('telefono',0)
        return HttpResponse(f'Usuario {nombre} registrado correctamente')
    else:
        return HttpResponse('Método no permitido', status=405)  

def logearse(request):
    return render(request, "login.html")

def login(request):
    if request.method == "POST":
        usuario = str(request.POST.get('usuario',0))
        contra = request.POST.get('contra',0)
        return HttpResponse(f'Hola.. {usuario} Bienvenido nuevamente.')
    else:
        return HttpResponse('Método no permitido', status=405) 