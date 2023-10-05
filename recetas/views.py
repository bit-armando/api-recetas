"""Recetas Views"""

#Django
from django.http import HttpResponse, JsonResponse
from post.models import Recetas

import random
import json


def desayuno_json(request):
    """Retorna un desayuno"""
    desayunos = Recetas.objects.filter(categoria='desayunos')
    desayunos = list(desayunos.values())
    data = random.choices(desayunos)    
    
    return JsonResponse(data[0])


def semana_json(request):
    """Retorna un desayuno por dia"""    
    respuesta = desayuno_json(request)
    data = respuesta.content.decode('utf-8')
    data = json.loads(data)
    # import pdb; pdb.set_trace()
    
    # for i in range():
    #     respuesta = desayuno_json(request)
    #     data += respuesta.content.decode('utf-8')
    
    return JsonResponse(data)


def semana_prueba(request):
    """Retorna un desayuno por dia con vista"""
    semana = semana_json(request)

    return HttpResponse(semana)