from django.urls import path
from .views import home
from .views import Login,Logout, VRegistro

urlpatterns = [
    
    path('', home, name='home'),
    path('logout/', Logout, name = 'logout'),
    path('login/',Login, name = 'login'),
    path('register/',VRegistro.as_view(), name = 'register'),

]