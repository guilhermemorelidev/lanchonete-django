from django.shortcuts import render

from .context import montar_contexto


def index(request):
    return render(request, 'cardapio/index.html', montar_contexto('cardapio'))
