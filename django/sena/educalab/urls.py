from django.urls import path
from . import views

# rutas de la aplicación EducaLab

urlpatterns = [
    path(" ",views.index, name="index"), 
    path("saludar/", views.saludar , name="saludar"),   
    path("saludo_per/<str:nombre>/", views.saludar_personalizado, name="saludo_per"),
    path("suma/<int:num1>/<int:num2>/", views.suma, name="suma"),
    path("suma_formulario/", views.suma_formulario , name="suma_formulario"),
    path("procesar_suma/", views.procesar_suma , name="procesar_suma"),
]