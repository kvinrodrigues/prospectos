from django.db import models

from apps.supervisor.models import Supervisor


class Vendedor (models.Model):
    vendedor_supervisor = models.ForeignKey(Supervisor)
    idVendedor = models.IntegerField()
    nombreVendedor = models.CharField(max_length=80)
    telefonoVendedor = models.IntegerField()
    def __str__(self):
        return self.nombreVendedor
