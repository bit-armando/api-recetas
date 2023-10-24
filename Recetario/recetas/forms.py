from django import forms
from .models import Recetas

class RecetasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            
    class Meta:
        model = Recetas
        exclude = ['created_date', 'author']
