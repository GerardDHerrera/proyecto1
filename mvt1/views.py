
from django.shortcuts import render
from django.template import Template, Context, loader
from mvt1.models import Curso, Familiares
from django.http import HttpResponse

def cursar (request):

    materia = Curso(nombre="Gerard",edad=55)

    materia.save()

    return HttpResponse(f"Estoy guardando esta informacion: {materia.nombre}")

def familiares (request):


    diccionario = Familiares(nombre="nomb", edad="1973-11-12", correo="kafjñkj@fjdk")

    plantilla = loader.get_template("mvtA1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)