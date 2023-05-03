from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.widgets import DateInput, Select

#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class DateInput(forms.DateInput):
    input_type = 'date'

class CreateUsuarioForm(UserCreationForm):
    fechaNaci = forms.DateField(widget=DateInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2','email',
                  'DNI','fechaNaci',
                  'lugarNaci','dirFact','sexo','tipoUsuario'] 
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'lugarNaci': forms.TextInput(attrs={'class': 'form-control'}),
            'dirFact': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'DNI': forms.NumberInput(attrs={'class': 'form-control'}),
        }
                  
class CreateAdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2','email',
                  'DNI','tipoUsuario'] 
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'DNI': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model=User

class EditForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','first_name','last_name',
                'lugarNaci','dirFact','sexo']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'lugarNaci': forms.TextInput(attrs={'class': 'form-control'}),
            'dirFact': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }


