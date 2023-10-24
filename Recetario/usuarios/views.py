from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic import View


from recetas.models import Recetas
from blogs.models import Blog

import pandas as pd

User = get_user_model()

def home(request):


    recetas_data = Recetas.objects.all().order_by('-created_date')[:6]
    blogs_data = Blog.objects.all().order_by('-created_date')[:6]

    return render(request, "home.html", {"recetas": recetas_data,
                                         "blogs":blogs_data})

def Login(request):
    if request.method=="POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            authenticated_user = authenticate(
                request,
                email=email,
                password=password
            )

            if authenticated_user:
                login(request, authenticated_user)
                return redirect("home")
            else:
                error_message = 'Contraseña o nombre de usuario incorrectos'
        else:
            error_message = 'El usuario no existe'

        context = {
            'error_message': error_message
        }
        return render(request, 'login_form.html', context)
    
    if request.method=="GET":
        return render(request, 'login_form.html')


def Logout(request):
    if request.user.is_authenticated:
        logout(request)  
        return redirect("home")
    else:
        return Response({'error': 'El usuario no está autenticado.'}, status=status.HTTP_400_BAD_REQUEST)            
        
class VRegistro(View):
    def get(self, request):
        return render(request, "register.html")
        
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password or not username:
            error_message = 'Complete todos los campos'
        elif User.objects.filter(email=email).exists():
            error_message = 'Email ya existe'
        else:
            user = User(email=email, username = username)
            user.set_password(password) 

            user.save()

            return redirect("login")

        return render(request, "register.html", {'error_message': error_message})
