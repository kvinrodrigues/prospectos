from django import forms
from .models import Articulo

class ArtForm(forms.ModelForm):
    class Meta:
            model = Articulo
            fields = '__all__'



