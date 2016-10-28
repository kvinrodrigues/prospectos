from django.db import models

class Vendedor (models.Model):
    idVendedor = models.IntegerField()
    nombreVendedor = models.CharField(max_length=80)
    telefonoVendedor = models.IntegerField()
