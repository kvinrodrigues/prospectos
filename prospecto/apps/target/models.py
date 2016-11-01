from django.db import models

# Create your models here.
class Target (models.Model):
    idTarget = models.IntegerField ()
    nombreTarget = models.CharField(max_length=80)
    telefonoTarget = models.IntegerField()
    origenTarget = models.CharField(max_length=80)
    estadoTarget = models.BooleanField()
    def __str__(self):
        return self.nombreTarget


