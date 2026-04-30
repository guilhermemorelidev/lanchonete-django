<div align="center">

# 🍔 Esther

### Sistema web para pedidos de uma lanchonete escolar

Uma aplicação desenvolvida em **Django** para organizar o cardápio, visualizar produtos e simular pedidos de uma lanchonete dentro do ambiente escolar, com uma experiência simples, bonita e direta.

<br>

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Django" src="https://img.shields.io/badge/Django-Web%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img alt="Status" src="https://img.shields.io/badge/Status-Em%20desenvolvimento-f59e0b?style=for-the-badge">
  <img alt="Projeto" src="https://img.shields.io/badge/Projeto-Lanchonete%20Escolar-ef4444?style=for-the-badge">
</p>

<br>

> **Esther** não é apenas uma página de cardápio.  
> É uma proposta de sistema organizado, modular e elegante para digitalizar a experiência de compra em uma lanchonete escolar.

</div>

---

## ✨ Visão geral

O **Esther** é um aplicativo web criado para facilitar a visualização de produtos, organização de cardápio e simulação de pedidos em uma lanchonete de escola.

A ideia do projeto é trazer uma experiência mais moderna para algo comum no dia a dia escolar: comprar um lanche.  
Com uma interface clara e uma estrutura bem dividida em apps Django, o sistema foi pensado para ser simples de entender, fácil de manter e bonito o suficiente para se destacar em um portfólio.

---

## 🎯 Objetivo do projeto

O objetivo do **Esther** é construir uma aplicação web que permita:

- visualizar os produtos disponíveis;
- acessar um cardápio organizado;
- simular pedidos de forma simples;
- separar responsabilidades em apps Django;
- criar uma base limpa para futuras melhorias;
- apresentar um projeto escolar com aparência profissional.

---

## 🧩 Apps do projeto

A aplicação é dividida em quatro apps principais:

| App | Responsabilidade |
| --- | --- |
| `home` | Página inicial, apresentação do sistema e navegação principal |
| `cardapio` | Exibição dos itens disponíveis para compra |
| `produtos` | Organização das informações dos produtos |
| `pedidos` | Fluxo de criação e visualização dos pedidos |

Essa separação deixa o projeto mais limpo, organizado e fácil de evoluir.

---

## 🏠 Home

O app `home` funciona como a porta de entrada do sistema.

Ele pode conter:

- apresentação da lanchonete;
- chamada para ver o cardápio;
- destaques do dia;
- informações rápidas;
- navegação para as principais áreas do site.

A proposta é que o usuário entre no sistema e entenda imediatamente o que pode fazer.

---

## 📋 Cardápio

O app `cardapio` é responsável por exibir os lanches, bebidas e demais produtos disponíveis.

Exemplos de categorias:

- salgados;
- doces;
- bebidas;
- combos;
- promoções;
- itens mais vendidos.

A ideia é tornar a escolha mais rápida e visual, evitando uma lista bagunçada de produtos.

---

## 🛒 Produtos

O app `produtos` concentra as informações dos itens da lanchonete.

Cada produto pode ter dados como:

- nome;
- descrição;
- preço;
- categoria;
- imagem;
- disponibilidade.

Mesmo sem uso de SQL ou APIs externas, a estrutura do projeto pode ser preparada para representar os produtos de forma organizada dentro do próprio código ou por dados locais simples.

---

## 📦 Pedidos

O app `pedidos` representa a parte mais importante da experiência: a simulação da compra.

Ele pode conter:

- seleção de produtos;
- resumo do pedido;
- cálculo do valor total;
- confirmação do pedido;
- tela de pedido finalizado.

Como o projeto não utiliza SQL nem APIs, o foco está na lógica interna, nas views, templates e organização visual da jornada do usuário.

---

## 🚫 O que este projeto não utiliza

Este projeto foi pensado para ser direto, leve e acessível.

Por isso, nesta versão, ele **não utiliza**:

- banco de dados SQL;
- APIs externas;
- integrações de pagamento;
- autenticação obrigatória;
- painel administrativo complexo;
- serviços de terceiros.

Isso torna o projeto ideal para aprendizado, apresentação escolar e evolução gradual.

---

## 🧠 Conceito técnico

Mesmo sendo um projeto simples em recursos, a estrutura pode seguir boas práticas profissionais:

```text
esther/
│
├── home/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── cardapio/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── produtos/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── pedidos/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── esther/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
├── templates/
│   └── base.html
│
├── manage.py
└── README.md
```

---

## 🖼️ Experiência visual esperada

O Esther pode seguir uma identidade visual moderna, inspirada em aplicativos de delivery e interfaces minimalistas.

Sugestões de estilo:

- layout limpo;
- cards de produtos;
- botões bem destacados;
- cores quentes;
- cantos arredondados;
- sombras suaves;
- destaque para preços;
- navegação simples;
- visual responsivo.

A experiência deve parecer leve, rápida e agradável.

---

## 🧱 Tecnologias utilizadas

| Tecnologia | Uso no projeto |
| --- | --- |
| Python | Linguagem principal |
| Django | Framework web |
| HTML | Estrutura das páginas |
| CSS | Estilização da interface |
| JavaScript | Interações simples, se necessário |
| Static Files | Imagens, estilos e scripts locais |

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/esther.git
```

### 2. Acesse a pasta do projeto

```bash
cd esther
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
pip install django
```

### 6. Execute o servidor local

```bash
python manage.py runserver
```

### 7. Acesse no navegador

```text
http://127.0.0.1:8000/
```

---

## 🧭 Rotas sugeridas

| Rota | Descrição |
| --- | --- |
| `/` | Página inicial |
| `/cardapio/` | Página do cardápio |
| `/produtos/` | Lista ou vitrine de produtos |
| `/pedidos/` | Área de pedidos |
| `/pedidos/confirmar/` | Confirmação do pedido |
| `/pedidos/finalizado/` | Pedido concluído |

---

## 💡 Ideias de funcionalidades

### Versão inicial

- página inicial com apresentação;
- listagem de produtos;
- cardápio dividido por categorias;
- simulação de pedido;
- tela de resumo;
- cálculo do total;
- layout responsivo.

### Melhorias futuras

- carrinho mais completo;
- filtros por categoria;
- busca por produto;
- sistema de favoritos;
- painel simples para editar itens;
- armazenamento local em arquivo;
- modo escuro;
- animações na interface;
- página de promoções do dia.

---

## 📌 Diferenciais do Esther

O que torna este projeto especial:

- arquitetura separada por apps;
- proposta clara e útil;
- visual com foco em experiência;
- código simples de entender;
- projeto ideal para portfólio inicial;
- escopo realista para ambiente escolar;
- possibilidade de evolução sem reescrever tudo.

---

## 🧪 Possível fluxo do usuário

```text
Usuário acessa o site
        ↓
Visualiza a página inicial
        ↓
Abre o cardápio
        ↓
Escolhe os produtos
        ↓
Monta um pedido
        ↓
Confere o resumo
        ↓
Finaliza a simulação do pedido
```

---

## 📁 Organização visual dos templates

Uma sugestão elegante para os templates:

```text
templates/
│
├── base.html
├── home/
│   └── index.html
├── cardapio/
│   └── cardapio.html
├── produtos/
│   └── produtos.html
└── pedidos/
    ├── pedidos.html
    ├── confirmar.html
    └── finalizado.html
```

---

## 🎨 Identidade do projeto

O nome **Esther** foi escolhido para dar personalidade ao projeto.

Em vez de parecer apenas mais um sistema genérico de lanchonete, o nome traz uma identidade mais memorável, elegante e fácil de apresentar.

> Um bom projeto não precisa ser gigantesco.  
> Ele precisa ser bem pensado, bem organizado e bem apresentado.

---

## 📸 Screenshots

Adicione aqui imagens do projeto quando a interface estiver pronta.

```text
/assets/screenshots/home.png
/assets/screenshots/cardapio.png
/assets/screenshots/pedido.png
```

Exemplo de organização:

```markdown
![Página inicial](assets/screenshots/home.png)
![Cardápio](assets/screenshots/cardapio.png)
![Resumo do pedido](assets/screenshots/pedido.png)
```

---

## 🛠️ Status do projeto

```text
🚧 Em desenvolvimento
```

O projeto está sendo construído com foco em organização, aprendizado e apresentação profissional.

---

## 👨‍💻 Autor

Desenvolvido por **Guilherme Moreli**.

Este projeto representa uma etapa de aprendizado com Django, organização de sistemas web e construção de interfaces voltadas para usuários reais.

---

## ⭐ Considerações finais

O **Esther** é um projeto escolar com mentalidade profissional.

Ele une uma necessidade simples, uma estrutura organizada e uma proposta visual moderna para criar uma aplicação que pode crescer com o tempo.

Mais do que apenas vender lanches, a ideia é mostrar como um problema comum pode ser transformado em uma solução digital limpa, bonita e funcional.

<div align="center">

<br>

### 🍔 Esther  
#### Uma lanchonete escolar, agora com experiência digital.

<br>

**Se este projeto te inspirou, deixe uma estrela no repositório.**

</div>
