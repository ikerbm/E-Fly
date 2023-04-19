from django import forms
from .models import *

class TareaForm(forms.ModelForm):
    
    class Meta:
        model= Tarea
        fields=['tarea']