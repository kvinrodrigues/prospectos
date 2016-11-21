from django import forms
from .models import Target_Contact


class Target_ContactForm(forms.ModelForm):
    class Meta:
        model = Target_Contact
        fields = '__all__'
