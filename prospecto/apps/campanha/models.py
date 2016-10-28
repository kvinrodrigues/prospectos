from django.db import models
from apps.articulo.models import Articulo
from apps.vendedor.models import Vendedor


class Campanha (models.Model):
    idCampanha = models.IntegerField()
    vende=models.ManyToManyField(Vendedor,null=True)
    arti=models.ManyToManyField(Articulo,null=True)
    descripcionCampanha = models.TextField()
    fecha_inicio_Campanha = models.DateField()
    fecha_fin_Campanha = models.DateField()
    porcentajeCampanha = models.IntegerField()
    def __str__(self):
        return str(self.idCampanha)