from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'photo']

    # Define a custom widget for the image field
    widgets = {
        'photo': forms.ClearableFileInput(attrs={'class': 'custom-image-input'}),
    }