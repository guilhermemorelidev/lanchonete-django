from django.shortcuts import render

from cardapio.views import montar_contexto


def index(request):
    return render(request, 'index.html', montar_contexto('home'))
