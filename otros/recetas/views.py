"""Recetas Views"""

#Django
from django.http import HttpResponse, JsonResponse
from post.models import Recetas

import random
import json
    

def get_receta(request, category):
    """Retorna un desayuno"""
    recetas = Recetas.objects.filter(categoria=category)
    recetas = list(recetas.values())
    data = random.choices(recetas)    
    
    return JsonResponse(data[0])


def semana_json(request):
    """Retorna un desayuno por dia"""    
    desayunos = {}
    bebidas = {}
    
    for i in range(5):
        respuesta = get_receta(request, 'desayunos')
        desayuno = respuesta.content.decode('utf-8')
        desayuno = json.loads(desayuno)
        desayunos[i] = desayuno
        
        respuesta = get_receta(request, 'bebidas')
        bebida = respuesta.content.decode('utf-8')
        bebida = json.loads(bebida)
        bebidas[i] = bebida
    
    data = {
            'desayunos': desayunos,
            # 'bebidas': bebidas
            }
    return JsonResponse(data)


def semana_prueba(request):
    """Retorna un desayuno por dia con vista"""
    semana = semana_json(request)

    return HttpResponse(semana)