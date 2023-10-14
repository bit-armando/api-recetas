from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Recetas(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    tiempo = models.CharField(max_length=10, blank=True, null=True)
    dificultad = models.CharField(max_length=10, blank=True, null=True)
    porciones = models.IntegerField()
    ingredientes = models.TextField()
    pasos = models.TextField()
    img = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)