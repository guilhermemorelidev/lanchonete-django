<div align="center">

# 🍔 School Snack

### Aplicativo de compras para lanchonete escolar feito com Django

Uma aplicação web simples, elegante e organizada para simular o fluxo de pedidos de uma lanchonete dentro da escola, com foco em experiência do usuário, separação de responsabilidades e estrutura limpa de projeto.

<br />

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

<br />

> Um projeto acadêmico desenvolvido para transformar a experiência de compra na lanchonete escolar em algo mais rápido, organizado e moderno.

</div>

---

## ✨ Sobre o projeto

O **School Snack** é um aplicativo web desenvolvido em **Django** para representar o funcionamento de uma lanchonete escolar digital.

A ideia é permitir que alunos visualizem produtos, consultem o cardápio, montem seus pedidos e naveguem por uma interface simples e intuitiva.

O projeto foi pensado com uma arquitetura modular, separando cada responsabilidade em um app Django específico. Isso torna o código mais organizado, fácil de manter e mais próximo de uma estrutura profissional.

---

## 🎯 Objetivo

O objetivo principal do projeto é criar uma aplicação funcional e bem estruturada para uma lanchonete escolar, priorizando:

- organização do código;
- clareza na navegação;
- interface moderna;
- separação por responsabilidades;
- simplicidade no funcionamento;
- facilidade de manutenção;
- boa apresentação para portfólio e GitHub.

---

## 🧩 Apps do projeto

O sistema será dividido em quatro apps principais:

| App | Responsabilidade |
| --- | --- |
| **home** | Página inicial, apresentação do sistema e navegação principal. |
| **cardapio** | Exibição do cardápio da lanchonete, categorias e itens disponíveis. |
| **produtos** | Organização dos produtos, detalhes, preços e informações visuais. |
| **pedidos** | Fluxo de montagem e visualização dos pedidos do usuário. |

Essa divisão deixa o projeto mais limpo e evita que toda a lógica fique concentrada em apenas um lugar.

---

## 🛒 Funcionalidades previstas

- Página inicial com apresentação da lanchonete;
- listagem de produtos disponíveis;
- cardápio separado por categorias;
- visualização de detalhes dos produtos;
- montagem de pedidos;
- resumo do pedido antes da finalização;
- layout responsivo;
- navegação simples e direta;
- estrutura organizada seguindo boas práticas do Django.

---

## 🚫 O que o projeto não utiliza

Este projeto foi planejado para ser direto e leve, sem dependências externas complexas.

Ele **não utiliza**:

- banco de dados SQL personalizado;
- APIs externas;
- integrações com pagamento;
- autenticação obrigatória;
- serviços de terceiros.

O foco está em aprender e demonstrar a estrutura de uma aplicação Django bem organizada, com páginas funcionais e uma boa experiência visual.

---

## 🧠 Conceitos aplicados

Durante o desenvolvimento, o projeto explora conceitos importantes de desenvolvimento web com Django:

- criação e organização de apps;
- rotas com `urls.py`;
- views responsáveis por renderizar páginas;
- templates HTML reutilizáveis;
- arquivos estáticos;
- separação entre estrutura, estilo e lógica;
- componentização visual com templates;
- organização de pastas;
- padrão MTV do Django.

---

## 🏗️ Estrutura sugerida do projeto

```bash
school-snack/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── home/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── home/
│           └── index.html
│
├── cardapio/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── cardapio/
│           └── cardapio.html
│
├── produtos/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── produtos/
│           └── produtos.html
│
├── pedidos/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── pedidos/
│           └── pedidos.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── img/
│
├── templates/
│   └── base.html
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🖥️ Prévia da experiência

A aplicação foi pensada para ter uma navegação simples:

```txt
Home → Cardápio → Produtos → Pedido → Resumo
```

O usuário entra na página inicial, acessa o cardápio, escolhe os produtos desejados e visualiza o pedido montado.

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/school-snack.git
```

### 2. Acesse a pasta do projeto

```bash
cd school-snack
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
source venv/bin/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute o servidor

```bash
python manage.py runserver
```

### 7. Abra no navegador

```txt
http://127.0.0.1:8000/
```

---

## 📦 Dependências principais

```txt
Django
```

O projeto foi desenvolvido para ser leve e fácil de rodar, sem pacotes desnecessários.

---

## 🎨 Interface

A identidade visual do projeto busca transmitir uma sensação moderna, jovem e agradável, combinando com o ambiente escolar.

A interface pode incluir:

- cards para produtos;
- cores vibrantes;
- botões destacados;
- layout responsivo;
- seções bem divididas;
- tipografia limpa;
- navegação intuitiva.

---

## 🔮 Melhorias futuras

Algumas ideias para evolução do projeto:

- sistema de login para alunos;
- histórico de pedidos;
- painel administrativo para a lanchonete;
- carrinho persistente;
- favoritos;
- filtro por categoria;
- busca por produtos;
- controle de estoque;
- integração com pagamentos;
- versão mobile aprimorada.

---

## 📚 Aprendizados

Este projeto ajuda a praticar desde a base do Django até a organização de uma aplicação maior.

Principais aprendizados:

- como dividir um projeto em apps;
- como criar templates reutilizáveis;
- como organizar arquivos estáticos;
- como estruturar rotas;
- como pensar no fluxo do usuário;
- como apresentar um projeto de forma profissional no GitHub.

---

## 🤝 Contribuição

Este é um projeto acadêmico, mas sugestões são sempre bem-vindas.

Para contribuir:

1. Faça um fork do projeto;
2. crie uma branch com sua melhoria;
3. faça o commit das alterações;
4. envie um pull request.

```bash
git checkout -b minha-melhoria
```

---

## 👨‍💻 Autor

Desenvolvido por **Guilherme Moreli**.

Projeto criado com foco em aprendizado, organização e evolução como desenvolvedor.

---

## 📄 Licença

Este projeto está sob a licença MIT.

Sinta-se livre para estudar, modificar e usar como base para seus próprios projetos.

---

<div align="center">

### ⭐ Se este projeto te inspirou, considere deixar uma estrela no repositório.

Feito com dedicação, estudo e vontade de evoluir.

</div>
