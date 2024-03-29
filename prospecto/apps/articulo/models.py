from django.db import models

class Articulo (models.Model):
    class Meta:
        permissions = (
            ("can_add_articulo", "Puede agregar articulo"),
        )

    nombreArticulo=models.CharField(max_length=45, null=True)
    tipoArticulo = models.CharField(max_length=80, null=True)
    montoArticulo = models.IntegerField()
    disponibilidad = models.IntegerField()



    def __str__(self):
        return self.nombreArticulo





