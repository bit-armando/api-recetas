from django.shortcuts import render

from recetas.views import semana_json


def list_semana(request):
    """Retorna un desayuno por dia con vista"""
    context = semana_json(request).content.decode('utf-8')
    return render(request, 'feed.html')