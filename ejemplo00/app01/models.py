from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

def __str__(self):
    return "%s - %s - %s - %d" % (self.nombre,
            self.apellido,
            self.cedula,
            self.edad)


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    poblacion = models.IntegerField()

def __str__(self):
    return "%s - %d" % (self.nombre ,
            self.poblacion)