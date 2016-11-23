from django.db import models
from apps.vendedor.models import Vendedor
# Create your models here.
class Target (models.Model):
    nombreTarget = models.CharField(max_length=80)
    DNITarget=models.IntegerField(null=True)
    RUCTarget=models.CharField(max_length=45,null=True)
    DireccionTarget=models.CharField(max_length=150,null=True)
    EmailTarget=models.EmailField(null=True)
    telefonoTarget = models.IntegerField()
    origenTarget = models.CharField(max_length=80)
    estadoTarget = models.NullBooleanField()
    vende=models.ForeignKey(Vendedor,null=True,blank=True)
    def __str__(self):
        return self.nombreTarget


