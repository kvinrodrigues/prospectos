from django.contrib.auth.models import Group
from .models import Rol
from django import forms


class RolForm(forms.ModelForm):

    class Meta:
        model = Group
        # fields = ['name', 'permissions']
        fields = '__all__'

class role(forms.ModelForm):
    class Meta:
        model =Rol
        # fields = ['name', 'permissions']
        fields = '__all__'


