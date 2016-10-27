from django.db import models

# Create your models here.
class Usuarios(models.Model):
    idUsuario = models.IntegerField ()
    nombreUsuario = models.CharField(max(80))
    passUsuario = models.CharField(max(20))