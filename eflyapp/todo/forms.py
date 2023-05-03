from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()




class CreateUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2','email',
                  'DNI','fechaNaci',
                  'lugarNaci','dirFact','sexo',] 

class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['password']

class EditForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','first_name','last_name',
                'lugarNaci','dirFact','sexo']


