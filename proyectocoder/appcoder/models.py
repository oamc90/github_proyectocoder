import email
from django.db import models

# Create your models here.

class Cursos(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

class Estudientes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.CharField(max_length=50)

class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    profesion=models.CharField(max_length=50)

class Entegables(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()
    

