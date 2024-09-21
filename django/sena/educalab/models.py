from django.db import models
#ORM : Object Relatinal Mapping

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=254)
    grado = models.IntegerField()
    fecha_nacimiento = models.DateTimeField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.nombre} -- {self.email}"