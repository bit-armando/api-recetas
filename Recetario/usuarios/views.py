from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from usuarios.api.serializers import (
    CustomTokenObtainPairSerializer, CustomUserSerializer,UserSerializer
)
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse


User = get_user_model()
def home(request):
    return render(request, "home.html")


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        user = authenticate(
            email=email,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                context = {
                    'access_token': login_serializer.validated_data.get('access'),
                    'refresh_token': login_serializer.validated_data.get('refresh'),
                    'user_data': user_serializer.data,
                    'message': 'Inicio de Sesion Existoso'
                }
                return redirect("home")
            else:
                error_message = 'Contraseña o nombre de usuario incorrectos'
        else:
            error_message = 'Contraseña o nombre de usuario incorrectos'

        context = {
            'error_message': error_message
        }
        return render(request, 'login_error.html', context)
    def get(self, request, *args, **kwargs):
        return render(request, 'login_form.html')



class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)

class Register(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            validated_data = serializer.validated_data
            serializer.create(validated_data) 
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
            return redirect("login")
        else:
            error_message = 'Contraseña o nombre de usuario incorrectos'

            context = {
                'error_message': error_message
            }
            return render(request, 'register.html', context)
    
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')
