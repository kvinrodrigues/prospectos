from django.db import models
from usuarios.models import Usuarios

class Rol (models.Model):
    usuario = models.OneToOneField(Usuarios)
    idRol = models.IntegerField()
    descripcionRol = models.TextField()
    tipoRol = models.CharField()