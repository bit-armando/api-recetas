from django.urls import path
from .views import home
from .views import Login,Logout, Register

urlpatterns = [
    path('home/', home, name='home'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('login/',Login.as_view(), name = 'login'),
    path('register/',Register.as_view(), name = 'register'),

]