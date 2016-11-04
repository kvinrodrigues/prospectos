from django.db import models
class Articulo (models.Model):


    nombreArticulo=models.TextField(max_length=45,null=True)
    descripcionArticulo = models.TextField(max_length=200,null=True)
    tipoArticulo = models.CharField(max_length=80)
    montoArticulo = models.IntegerField()
    disponibilidad = models.IntegerField()
















