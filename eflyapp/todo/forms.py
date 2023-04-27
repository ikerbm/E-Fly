from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *



class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','contraseña','email',
                  'fechaNaci','lugarNaci','dirFact','sexo',] 
        
class LoginForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['email','contraseña']


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','contraseña','email',
                  'fechaNaci','lugarNaci','dirFact','sexo',] 
        


