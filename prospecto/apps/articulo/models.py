from django.db import models


class Articulo (models.Model):
    idArticulo = models.IntegerField()
    nombreArticulo=models.TextField(max_length=45)
    descripcionArticulo = models.TextField(max_length=200)
    tipoArticulo = models.CharField(max_length=80)
    montoArticulo = models.IntegerField()
    disponibilidad = models.IntegerField()


    def __str__(self):
        return self.descripcionArticulo


