from django.shortcuts import render

from cardapio.context import montar_contexto


def index(request):
    return render(request, 'produtos/index.html', montar_contexto('produtos'))
