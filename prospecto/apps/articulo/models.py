from django.db import models
from simple_history.models import HistoricalRecords
class Articulo (models.Model):
    nombreArticulo=models.CharField(max_length=45, null=True)
    tipoArticulo = models.CharField(max_length=80, null=True)
    montoArticulo = models.IntegerField()
    disponibilidad = models.IntegerField()
    history = HistoricalRecords()


    def __str__(self):
        return self.nombreArticulo





