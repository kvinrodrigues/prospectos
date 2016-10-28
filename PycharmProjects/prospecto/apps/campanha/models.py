from django.db import models
from apps.vendedor.models import Vendedor
from apps.articulo.models import Articulo
# Create your models here.
class Campanha (models.Model):
    idCampanha = models.IntegerField()
    vende=models.ManyToManyField(Vendedor,null=True)
    arti=models.ManyToManyField(Articulo,null=True)
    descripcionCampanha = models.TextField()
    fecha_inicio_Campanha = models.DateField()
    fecha_fin_Campanha = models.DateField()
    porcentajeCampanha = models.IntegerField()
    def __str__(self):
        return self.descripcionCampanha