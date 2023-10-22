from django.urls import path
from .views import RecetasCreateView, RecetasUpdateView, RecetasListView, RecetasDetailView
from .views import RecetasByAuthorListView, receta_delete

urlpatterns = [
    path('create/', RecetasCreateView.as_view(), name='receta-create'),
    path('update/<int:pk>/', RecetasUpdateView.as_view(), name='receta-update'),
    path('recetas/<int:pk>/delete/', receta_delete, name='receta-delete'),
    path('', RecetasListView.as_view(), name='recetas-list'),
    path('<int:pk>', RecetasDetailView.as_view(), name='receta-detail'),
    path('my-recetas/', RecetasByAuthorListView.as_view(), name='my-recetas'),
]

