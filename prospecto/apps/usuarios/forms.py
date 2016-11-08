from django.contrib.auth.models import User
from django import forms


class UsuarioModelForm(forms.ModelForm):
    model=User
    fields=['username','first_name','email','groups','is_active']
    labels = {
        'first_name': 'Nombre',
        'last_name': 'Apellido',
        'email': 'Email',
        'is_active': 'Activar usuario',
        'groups': 'Perfiles',
    }
    help_texts = {
            'username':'(*) Requerido. 30 caracteres o menos. Letras, digitos y @/./+/-/_',
            # 'password':'(*)',
            'is_active':'',
            'groups':'',
        }


