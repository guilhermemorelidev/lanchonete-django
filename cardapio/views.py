from django.shortcuts import render

PRODUTOS = [
    {
        'nome': 'Sanduiche Natural',
        'categoria': 'Lanches',
        'descricao': 'Pao integral, frango temperado, cenoura e folhas frescas.',
        'preco': 'R$ 9,90',
        'imagem': 'https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=800&q=80',
        'destaque': 'Mais pedido',
    },
    {
        'nome': 'Suco de Laranja',
        'categoria': 'Bebidas',
        'descricao': 'Suco gelado preparado para acompanhar o intervalo.',
        'preco': 'R$ 5,50',
        'imagem': 'https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?auto=format&fit=crop&w=800&q=80',
        'destaque': 'Natural',
    },
    {
        'nome': 'Pao de Queijo',
        'categoria': 'Assados',
        'descricao': 'Porcao quentinha, crocante por fora e macia por dentro.',
        'preco': 'R$ 6,00',
        'imagem': 'https://images.unsplash.com/photo-1606755962773-d324e0a13086?auto=format&fit=crop&w=800&q=80',
        'destaque': 'Quentinho',
    },
]

PEDIDO_EXEMPLO = [
    {'quantidade': 2, 'nome': 'Sanduiche Natural', 'subtotal': 'R$ 19,80'},
    {'quantidade': 1, 'nome': 'Suco de Laranja', 'subtotal': 'R$ 5,50'},
    {'quantidade': 1, 'nome': 'Pao de Queijo', 'subtotal': 'R$ 6,00'},
]


def montar_contexto(pagina_atual='cardapio'):
    return {
        'pagina_atual': pagina_atual,
        'titulo_pagina': {
            'home': 'Home',
            'cardapio': 'Cardapio',
            'produtos': 'Produtos',
            'pedidos': 'Pedidos',
        }.get(pagina_atual, 'Cardapio'),
        'produtos': PRODUTOS,
        'pedido_itens': PEDIDO_EXEMPLO,
        'pedido_total': 'R$ 31,30',
    }


def index(request):
    return render(request, 'index.html', montar_contexto('cardapio'))
