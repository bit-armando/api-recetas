from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, redirect

from .models import Blog
from .forms import BlogForm

from django.http import Http404

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog_form.html'  

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.object.pk})    
    

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog_form.html'  

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.object.pk})    

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.user == blog.author:
        blog.delete()

    return redirect('blog-list')

class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'  
    context_object_name = 'blogs'  
    paginate_by = 2


class BlogByAuthorListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 2

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Blog.objects.filter(author=self.request.user).order_by('-created_date')
        else:
            # If the user is not logged in, display all blogs
            return Blog.objects.all().order_by('-created_date')

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html' 
    context_object_name = 'blog'  

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return self.render_error_page()

    def render_error_page(self):
        return render(
            self.request,
            'blog_not_found.html',
            status=404)