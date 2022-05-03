from django.http import HttpResponse
from django.shortcuts import render
from .models import Cursos

# Create your views here.

def curso(self):
    curso=Cursos(nombre="curso de python", comision=2760)
    curso.save()
    texto = f" curso: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)
    