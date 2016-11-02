from django.db import models


class Usuarios(models.Model):

    nombreUsuario = models.CharField(max_length=20)
    passUsuario = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreUsuario
