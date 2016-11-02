from django.db import models




class Supervisor (models.Model):

    nombreSupervisor = models.CharField(max_length=20)
    def __str__(self):
        return self.nombreSupervisor
