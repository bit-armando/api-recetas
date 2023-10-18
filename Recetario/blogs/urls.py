from django.urls import path
from .views import BlogCreateView, BlogUpdateView

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),

]
