from django.db import models

from apps.target.models import Target
from apps.supervisor.models import Supervisor


class Vendedor (models.Model):

    vendedor_supervisor = models.ForeignKey(Supervisor, null=True)
    nombreVendedor = models.CharField(max_length=80)
    telefonoVendedor = models.IntegerField()
    targetToCall=models.ForeignKey(Target, null=True)


    def __str__(self):
        return self.nombreVendedor
