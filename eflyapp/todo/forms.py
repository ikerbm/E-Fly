from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class CreateUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','contraseña','email',
                  'DNI','fechaNaci',
                  'lugarNaci','dirFact','sexo',] 


class LoginForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['email','contraseña']

class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['contraseña']

class EditForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['nombre','apellido','contraseña',
                'lugarNaci','dirFact','sexo',]


