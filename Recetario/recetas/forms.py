from django import forms
from .models import Recetas

class RecetasForm(forms.ModelForm):
    class Meta:
        model = Recetas
        exclude = ['created_date', 'author']
