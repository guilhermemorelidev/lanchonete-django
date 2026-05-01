from django.shortcuts import render

from cardapio.context import montar_contexto


def index(request):
    return render(request, 'home/index.html', montar_contexto('home'))
