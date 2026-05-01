PRODUTOS = [
    {
        'nome': 'Sanduiche Natural',
        'categoria': 'Lanches',
        'descricao': 'Pao integral, frango temperado, cenoura e folhas frescas.',
        'preco': 'R$ 9,90',
        'imagem': 'https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=900&q=80',
        'destaque': 'Mais pedido',
    },
    {
        'nome': 'Suco de Laranja',
        'categoria': 'Bebidas',
        'descricao': 'Suco gelado preparado para acompanhar o intervalo.',
        'preco': 'R$ 5,50',
        'imagem': 'https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?auto=format&fit=crop&w=900&q=80',
        'destaque': 'Natural',
    },
    {
        'nome': 'Pao de Queijo',
        'categoria': 'Assados',
        'descricao': 'Porcao quentinha, crocante por fora e macia por dentro.',
        'preco': 'R$ 6,00',
        'imagem': 'https://images.unsplash.com/photo-1606755962773-d324e0a13086?auto=format&fit=crop&w=900&q=80',
        'destaque': 'Quentinho',
    },
    {
        'nome': 'Bolo de Chocolate',
        'categoria': 'Doces',
        'descricao': 'Fatia macia com cobertura simples para o lanche da tarde.',
        'preco': 'R$ 7,50',
        'imagem': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=900&q=80',
        'destaque': 'Do dia',
    },
]

CATEGORIAS = [
    {'nome': 'Lanches', 'icone': 'bi-basket2-fill', 'total': '8 opcoes'},
    {'nome': 'Bebidas', 'icone': 'bi-cup-straw', 'total': '6 opcoes'},
    {'nome': 'Assados', 'icone': 'bi-fire', 'total': '5 opcoes'},
    {'nome': 'Doces', 'icone': 'bi-stars', 'total': '4 opcoes'},
]

PEDIDO_EXEMPLO = [
    {'quantidade': 2, 'nome': 'Sanduiche Natural', 'subtotal': 'R$ 19,80'},
    {'quantidade': 1, 'nome': 'Suco de Laranja', 'subtotal': 'R$ 5,50'},
    {'quantidade': 1, 'nome': 'Pao de Queijo', 'subtotal': 'R$ 6,00'},
]

ETAPAS_PEDIDO = [
    {'titulo': 'Escolha os itens', 'texto': 'Monte o pedido olhando as categorias do cardapio.'},
    {'titulo': 'Revise o resumo', 'texto': 'Confira quantidades, produtos e total antes de finalizar.'},
    {'titulo': 'Retire no balcao', 'texto': 'O pedido fica organizado para a lanchonete preparar.'},
]

PAGINAS = {
    'home': {
        'titulo_pagina': 'Home',
        'kicker': 'Lanchonete escolar digital',
        'titulo': 'School Snack',
        'subtitulo': 'Uma experiencia simples para ver o cardapio, escolher produtos e acompanhar pedidos.',
        'hero_imagem': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1800&q=80',
    },
    'cardapio': {
        'titulo_pagina': 'Cardapio',
        'kicker': 'Cardapio do dia',
        'titulo': 'Escolhas rapidas para o recreio.',
        'subtitulo': 'Categorias organizadas para o aluno encontrar lanches, bebidas, assados e doces sem complicacao.',
        'hero_imagem': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=1800&q=80',
    },
    'produtos': {
        'titulo_pagina': 'Produtos',
        'kicker': 'Produtos disponiveis',
        'titulo': 'Itens com preco claro e visual direto.',
        'subtitulo': 'Uma vitrine responsiva para apresentar produtos, categorias, destaques e valores.',
        'hero_imagem': 'https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=1800&q=80',
    },
    'pedidos': {
        'titulo_pagina': 'Pedidos',
        'kicker': 'Pedido organizado',
        'titulo': 'Resumo do pedido antes de finalizar.',
        'subtitulo': 'Itens, quantidades e total ficam visiveis para reduzir erro na hora da retirada.',
        'hero_imagem': 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1800&q=80',
    },
}

SLIDES = {
    'home': [
        {
            'titulo': 'Intervalo mais rapido',
            'texto': 'Acesse produtos e pedido em poucos cliques.',
            'imagem': 'https://images.unsplash.com/photo-1543352634-a1c51d9f1fa7?auto=format&fit=crop&w=1200&q=80',
        },
        {
            'titulo': 'Cardapio visual',
            'texto': 'Fotos, categorias e precos organizados.',
            'imagem': 'https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=1200&q=80',
        },
        {
            'titulo': 'Pedido conferido',
            'texto': 'Resumo simples antes de retirar na lanchonete.',
            'imagem': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=1200&q=80',
        },
    ],
    'cardapio': [
        {
            'titulo': 'Lanches',
            'texto': 'Opcoes praticas para o recreio.',
            'imagem': 'https://images.unsplash.com/photo-1528736235302-52922df5c122?auto=format&fit=crop&w=1200&q=80',
        },
        {
            'titulo': 'Bebidas',
            'texto': 'Sucos e bebidas para acompanhar o lanche.',
            'imagem': 'https://images.unsplash.com/photo-1544145945-f90425340c7e?auto=format&fit=crop&w=1200&q=80',
        },
        {
            'titulo': 'Assados e doces',
            'texto': 'Itens quentinhos e sobremesas do dia.',
            'imagem': 'https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=80',
        },
    ],
    'produtos': [
        {
            'titulo': 'Produtos em destaque',
            'texto': 'Itens principais com preco e categoria.',
            'imagem': 'https://images.unsplash.com/photo-1551782450-a2132b4ba21d?auto=format&fit=crop&w=1200&q=80',
        },
        {
            'titulo': 'Fotos grandes',
            'texto': 'Visual direto para escolher com facilidade.',
            'imagem': 'https://images.unsplash.com/photo-1551024506-0bccd828d307?auto=format&fit=crop&w=1200&q=80',
        },
        {
            'titulo': 'Catalogo simples',
            'texto': 'Cards responsivos com informacoes essenciais.',
            'imagem': 'https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?auto=format&fit=crop&w=1200&q=80',
        },
    ],
    'pedidos': [
        {
            'titulo': 'Resumo do pedido',
            'texto': 'Quantidades, itens e total em um painel claro.',
            'imagem': 'https://images.unsplash.com/photo-1555992336-03a23c7b20ee?auto=format&fit=crop&w=1200&q=80',
        },
        {
            'titulo': 'Fluxo de retirada',
            'texto': 'Pedido revisado antes de ir para o balcao.',
            'imagem': 'https://images.unsplash.com/photo-1515003197210-e0cd71810b5f?auto=format&fit=crop&w=1200&q=80',
        },
        {
            'titulo': 'Controle visual',
            'texto': 'Status simples para acompanhar o processo.',
            'imagem': 'https://images.unsplash.com/photo-1552566626-52f8b828add9?auto=format&fit=crop&w=1200&q=80',
        },
    ],
}


def montar_contexto(pagina_atual='home'):
    pagina = PAGINAS.get(pagina_atual, PAGINAS['home'])

    return {
        'pagina_atual': pagina_atual,
        'titulo_pagina': pagina['titulo_pagina'],
        'kicker': pagina['kicker'],
        'titulo': pagina['titulo'],
        'subtitulo': pagina['subtitulo'],
        'hero_imagem': pagina['hero_imagem'],
        'slides': SLIDES[pagina_atual],
        'produtos': PRODUTOS,
        'categorias': CATEGORIAS,
        'pedido_itens': PEDIDO_EXEMPLO,
        'pedido_total': 'R$ 31,30',
        'etapas_pedido': ETAPAS_PEDIDO,
    }
