import mailbox
from pyexpat import model
from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    mail = models.EmailField(blank=True, null=True)
    nacimiento = models.DateField()

class Posteo(models.Model):
    titulo = models.CharField(max_length=20)
    cuerpo = models.CharField(max_length=200)    

class Moderador(models.Model):
    nombre = models.CharField(max_length=30)
    mail = models.EmailField()
    sector = models.CharField(max_length=30)
    


