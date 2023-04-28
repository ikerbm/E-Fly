from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *



'''class CreateUserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['usuario','nombre','apellido','email','password1','password2',
                  'fechaNaci','lugarNaci','dirFact','sexo',] '''


'''
class CreateUserForm(UserCreationForm):
    class Meta:
        model=Usuario
        fields=['email','contraseña']
'''

