from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola !")

def despedida(request):
    return HttpResponse('Hasta luego.')

def horaactual(request):
    fecha_actual=datetime.datetime.now()
    hora = """ La hora actual es: %s """%fecha_actual
    return HttpResponse(hora)

def edad_futura(request, anho):
    edadactual = 28
    periodo=anho - 2024
    edadfutura = edadactual+periodo
    documento= '''En el año %s tendras %s Años'''%(anho, edadfutura)
    return HttpResponse(documento)