from django import forms
from .models import Target


class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = '__all__'
