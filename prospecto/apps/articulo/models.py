from django.db import models

class Articulo (models.Model):
    idArticulo = models.IntegerField()
    descripcionArticulo = models.TextField()
    tipoArticulo = models.CharField()
    montoArticulo = models.IntegerField()
    disponibilidad = models.IntegerField()