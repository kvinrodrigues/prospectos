from django.db import models

# Create your models here.
from apps.supervisor.models import Supervisor
from apps.vendedor.models import Vendedor


class Usuarios(models.Model):
    idUsuario = models.IntegerField ()
    nombreUsuario = models.CharField(max_length=20)
    passUsuario = models.CharField(max_length=20)
    def __str__(self):
        return self.nombreUsuario
