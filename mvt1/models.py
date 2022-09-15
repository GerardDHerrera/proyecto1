from email.message import EmailMessage
from django.db import models

# Create your models here.

class Curso (models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()

class Familiares (models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.DateField()
    correo = models.EmailField()
