from django.contrib.auth.models import Group
from django import forms


class RolForm(forms.ModelForm):

    class Meta:
        model = Group
        # fields = ['name', 'permissions']
        fields = '__all__'




