from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            
    class Meta:
        model = Blog
        fields = ['title', 'content', 'photo']

    # Define a custom widget for the image field
    widgets = {
        'photo': forms.ClearableFileInput(attrs={'class': 'custom-image-input'}),
    }