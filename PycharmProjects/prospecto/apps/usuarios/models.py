from django.db import models

# Create your models here.
class Usuarios(models.Model):
    idUsuario = models.IntegerField ()
    nombreUsuario = models.CharField(max_length=20)
    passUsuario = models.CharField(max_length=20)