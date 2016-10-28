from django.db import models

# Create your models here.
class Campanha (models.Model):
    idCampanha = models.IntegerField()
    descripcionCampanha = models.IntegerField()
    fecha_inicio_Campanha = models.DateField()
    fecha_fin_Campanha = models.DateField()
    porcentajeCampanha = models.IntegerField()