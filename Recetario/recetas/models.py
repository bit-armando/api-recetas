from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


dificultad_choices = (
    ('Facil','Facil'),
    ('Media', 'Media'),
    ('Dificil','Dificil'),
)

categorias_choices = (
    ('Entradas', 'Entradas'),
    ('Platos Principales', 'Platos Principales'),
    ('Postres', 'Postres'),
    ('Bebidas', 'Bebidas'),
    ('Cocina Internacional', 'Cocina Internacional'),
    ('Comida Saludable', 'Comida Saludable'),
    ('Ocasiones Especiales', 'Ocasiones Especiales'),
)
  
class Recetas(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=30, choices=categorias_choices, default='Entradas')
    tiempo = models.TimeField(blank=True, null=True)
    dificultad = models.CharField(max_length=10, choices=dificultad_choices, default='Facil')
    porciones = models.PositiveIntegerField()
    ingredientes = models.TextField()
    pasos = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_created=True, auto_now_add=True,null=False, blank=False)


    def __str__(self):
        return self.nombre