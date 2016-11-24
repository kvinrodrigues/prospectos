from django.db import models

# Create your models here.
from apps.campanha.models import Campanha
from apps.target.models import Target
from apps.vendedor.models import Vendedor


class Ventas (models.Model):
    contacto = models.ManyToManyField(Target)
    camp = models.ManyToManyField(Campanha)
    vendedor = models.ManyToManyField(Vendedor)