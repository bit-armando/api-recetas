from django.urls import path
from .views import BlogCreateView, BlogUpdateView, BlogListView, BlogDetailView
from .views import BlogByAuthorListView, blog_delete

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),
    path('blogs/<int:pk>/delete/', blog_delete, name='blog-delete'),
    path('', BlogListView.as_view(), name='blog-list'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('my-blogs/', BlogByAuthorListView.as_view(), name='my-blogs'),
]

