from django.urls import path
from . import views

# rutas de la aplicación EducaLab

urlpatterns = [
<<<<<<< HEAD
    path("saludar/", views.saludar , name="saludar"),
    path("",views.index, name="index"),   
=======
    path("",views.index, name="index"), 
    path("saludar/", views.saludar , name="saludar"),   
>>>>>>> 5df084347a83728785a513c9482279380c8ad8d2
    path("saludo_per/<str:nombre>/", views.saludar_personalizado, name="saludo_per"),
    path("suma/<int:num1>/<int:num2>/", views.suma, name="suma"),
    path("suma_formulario/", views.suma_formulario , name="suma_formulario"),
    path("procesar_suma/", views.procesar_suma , name="procesar_suma"),
    path("registro/", views.registro, name="registro"),
]