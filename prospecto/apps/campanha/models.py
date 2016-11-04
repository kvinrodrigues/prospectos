from django.db import models
from apps.articulo.models import Articulo
from apps.vendedor.models import Vendedor


class Campanha (models.Model):
    vende=models.ManyToManyField(Vendedor)
    arti=models.ManyToManyField(Articulo)
    nombreCamapanha = models.CharField(max_length=80, null=True)
    descripcionCampanha = models.TextField()
    fecha_inicio_Campanha = models.DateField()
    fecha_fin_Campanha = models.DateField()
    porcentajeCampanha = models.IntegerField()
    def __str__(self):
        return self.nombreCampanha