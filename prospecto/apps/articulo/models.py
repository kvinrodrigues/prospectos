from django.db import models
class Articulo (models.Model):
    nombreArticulo=models.TextField(max_length=45, null=True)
    tipoArticulo = models.CharField(max_length=80, null=True)
    montoArticulo = models.IntegerField()
    disponibilidad = models.IntegerField()
<<<<<<< HEAD












=======
    def __str__(self):
        return self.nombreArticulo
>>>>>>> 2360f961012cc2de126f18417a5c5d4e2d390261




