from django.db import models

# Create your models here.
class Target (models.Model):
    nombreTarget = models.CharField(max_length=80)
    telefonoTarget = models.IntegerField()
    origenTarget = models.CharField(max_length=80)
    estadoTarget = models.NullBooleanField()
    def __str__(self):
        return self.nombreTarget


