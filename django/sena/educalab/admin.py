from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Estudiante)
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display= ["id","nombre","email","grado","fecha_nacimiento"]
    search_fields= ["nombre"]
    list_filter = ["fecha_nacimiento","grado"]
    list_editable= ["grado", "fecha_nacimiento"]