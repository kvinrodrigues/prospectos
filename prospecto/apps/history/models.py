from django.db import models
from apps.target_contact.models import Target_Contact
# Create your models here.
class History (models.Model):
    descripcionHistorial=models.TextField(max_length=200,null=True)
    fechaHistorial=models.DateField(null=True)

    Target_Contact_history = models.ForeignKey(Target_Contact,related_name='Target_Contact_history', null=True)
    def __str__(self):
        return self.Target_Contact_history.idTarget_Contact

