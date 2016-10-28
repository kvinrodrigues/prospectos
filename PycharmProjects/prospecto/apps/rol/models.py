from django.db import models
from apps.usuarios.models import Usuarios

class Rol (models.Model):
    usuario = models.ForeignKey(Usuarios)
    idRol = models.IntegerField()
    descripcionRol = models.TextField()
    tipoRol = models.CharField(max_length=15)