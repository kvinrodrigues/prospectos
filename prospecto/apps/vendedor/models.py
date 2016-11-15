from django.db import models
from simple_history.models import HistoricalRecords

from apps.supervisor.models import Supervisor


class Vendedor (models.Model):

    vendedor_supervisor = models.ForeignKey(Supervisor, null=True)
    nombreVendedor = models.CharField(max_length=80)
    telefonoVendedor = models.IntegerField()
    history = HistoricalRecords()
    def __str__(self):
        return self.nombreVendedor
