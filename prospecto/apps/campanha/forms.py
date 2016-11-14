from django import forms
from .models import Campanha

class CamForm(forms.ModelForm):
    class Meta:
            model = Campanha
            fields = '__all__'



