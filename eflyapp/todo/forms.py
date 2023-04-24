from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class TareaForm(forms.ModelForm):
    
    class Meta:
        model= Tarea
        fields=['tarea']

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','contraseña','email',
                  'fechaNaci','lugarNaci','dirFact','sexo',] 


'''
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2',] 
'''