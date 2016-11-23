from django import forms
from .models import Campanha


class CamForm(forms.ModelForm):
    class Meta:
        model = Campanha
        fields = ('arti', 'nombreCampanha', 'descripcionCampanha', 'fecha_inicio_Campanha', 'fecha_fin_Campanha')


class CamAllForm(forms.ModelForm):
    class Meta:
        model = Campanha
        fields = '__all__'



