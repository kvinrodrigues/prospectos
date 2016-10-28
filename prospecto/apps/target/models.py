from django.db import models

# Create your models here.
class Target (models.Model):
    idTarger = models.IntegerField ()
    nombreTarget = models.CharField(max(80))
    telefonoTarget = models.IntegerField()
    origenTarget = models.CharField(max(200))
    estadoTarget = models.BooleanField()