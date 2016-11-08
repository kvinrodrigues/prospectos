from django.db import models
from django.contrib.auth.models import User

class Rol (models.Model):
    usuario = models.OneToOneField(User)
    descripcionRol = models.TextField()
    tipoRol = models.CharField(max_length=15)
    def __str__(self):
        return self.descripcionRol
