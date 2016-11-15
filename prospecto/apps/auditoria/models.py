from django.db import models
from django.template.backends import django


class Auditoria(models.Model):
    userlog = models.CharField(max_length=45)
    description=models.CharField(max_length=45)
    access_type=models.CharField(max_length=15)
    parameters=models.TextField()
    ip=models.CharField(max_length=25)
