from django.db import models
from apps.articulo.models import Articulo
from apps.vendedor.models import Vendedor
from apps.target.models import Target
# Create your models here.
class Target_Contact (models.Model):
    idTarget_Contact = models.IntegerField()
    Objetivo = models.ForeignKey(Target)
    Vendedor = models.ForeignKey(Vendedor)
    Articulo=models.ManyToManyField(Articulo)

    def __str__(self):
        return self.art.idArticulo

