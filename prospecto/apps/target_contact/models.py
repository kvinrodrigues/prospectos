from django.db import models
from apps.articulo.models import Articulo
from apps.target.models import Target
# En este modelo se guarda cada llamada: Al que se ofrece, el vendedor que realiza la operación, y el Articulo/Servicio ofrecido
class Target_Contact (models.Model):
    Objetivo = models.ForeignKey(Target, null=True)
    Articulo=models.ManyToManyField(Articulo)





