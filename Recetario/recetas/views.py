from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, redirect

from .models import Recetas
from .forms import RecetasForm

from django.http import Http404

class RecetasCreateView(CreateView):
    model = Recetas
    form_class = RecetasForm
    template_name = 'receta_form.html'  

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('recetas-list')    
    

class RecetasUpdateView(UpdateView):
    model = Recetas
    form_class = RecetasForm
    template_name = 'receta_form.html'  

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('receta-detail', kwargs={'pk': self.object.pk})    

def receta_delete(request, pk):
    receta = get_object_or_404(Recetas, pk=pk)

    if request.user == receta.author:
        receta.delete()

    return redirect('recetas-list')

class RecetasListView(ListView):
    model = Recetas
    template_name = 'receta_list.html'  
    context_object_name = 'recetas'  
    paginate_by = 2


class RecetasByAuthorListView(ListView):
    model = Recetas
    template_name = 'receta_list.html'
    context_object_name = 'recetas'
    paginate_by = 2

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Recetas.objects.filter(author=self.request.user).order_by('-created_date')
        else:
            # If the user is not logged in, display all recetas
            return Recetas.objects.all().order_by('-created_date')

class RecetasDetailView(DetailView):
    model = Recetas
    template_name = 'receta_detail.html' 
    context_object_name = 'receta'  

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return self.render_error_page()

    def render_error_page(self):
        return render(
            self.request,
            'receta_not_found.html',
            status=404)