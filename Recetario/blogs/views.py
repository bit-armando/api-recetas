from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Blog
from .forms import BlogForm

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog_form.html'  
    # Specify the URL to redirect to after successful post creation
    success_url = reverse_lazy('home')  

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog_form.html'  
    # Specify the URL to redirect to after successful post creation
    success_url = reverse_lazy('home')  

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)