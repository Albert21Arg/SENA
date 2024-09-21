from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name="index"), 
    path("productos/",views.productos, name="productos"),
    path("nosotros/",views.nosotros, name="nosotros"),
    path("contactos/",views.contactos, name="contactos"),
    path("login/",views.login, name="login"),
    path("registro/",views.registro, name="registro"),
    path("restaurar/",views.restaurar, name="restaurar"),
]