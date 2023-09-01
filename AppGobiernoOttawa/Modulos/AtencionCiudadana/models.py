from django.db import models

# Aquí definí la estructura de las tablas de la base de datos y el tipo de datos a introducir en ellas.

# En esta tabla se introduce el código del área urbana del ciudadano, su nombre y la localidad donde vive.
class AreaUrbana(models.Model):
    codigo = models.Charfield(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    localidad = models.CharField(max_length=100)

class Ciudadano(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellido = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)

    def nombreCompleto(self):
        txt = "{0}, {1}, {2}"
        return txt.format(self.apellido, self.nombre, self.dni)

class Solicitud(models.Model):
    tipo = models.CharField(max_length=15, primary_key=True)
    descripcion = models.CharField(max_length=120)
    lugar = models.CharField(max_length=30)

class NumeroDeLaSolicitud(models.Model):
    id = models.AutoField(primary_key=True)
    fechaSolicitud = models.DateTimeField(auto_add_now=True)



    