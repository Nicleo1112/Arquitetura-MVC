# Sistema de Livraria — Arquitetura MVC

Este projeto é um MVP (Minimum Viable Product) de um sistema de busca de livros, refatorado para seguir a arquitetura MVC (Model-View-Controller) e validado utilizando a metodologia BDD (Behavior-Driven Development).

---

## Descrição

A aplicação permite realizar buscas de livros com base em diferentes critérios, garantindo organização do código através do padrão MVC e confiabilidade por meio de testes BDD.

---

## Tecnologias Utilizadas

* Linguagem: Python 3.x
* Framework Web: Flask (Controller e Rotas)
* Template Engine: Jinja2 / HTML5 (View)
* Estilização: Bootstrap 5
* Testes BDD: Behave (Gherkin)

---

## Arquitetura MVC

O projeto foi estruturado para separar responsabilidades de forma clara:

### Model (models.py)

Responsável pelos dados e regras de negócio:

* Classe LivroModel
* Armazenamento de dados
* Lógica de filtragem

### View (templates/index.html)

Responsável pela interface do usuário:

* Formulário de busca
* Exibição dos resultados
* HTML com Bootstrap

### Controller (app.py)

Responsável pela comunicação entre Model e View:

* Recebe requisições HTTP
* Processa dados
* Renderiza a interface

---

## Metodologia BDD

O comportamento do sistema foi definido e validado utilizando arquivos `.feature` escritos em Gherkin.

### Cenários testados

1. Filtragem por título (busca parcial)
2. Filtragem por autor
3. Filtragem por intervalo de anos de publicação

---

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Nicleo1112/Arquitetura-MVC.git
cd Arquitetura-MVC
```

### 2. Configurar ambiente virtual e instalar dependências

```bash
python -m venv .venv

# Ativar no Windows
.venv\Scripts\activate

# Instalar dependências
pip install flask behave
```

### 3. Executar a aplicação

```bash
python app.py
```

Acesse no navegador:
http://127.0.0.1:5000

### 4. Executar os testes BDD

```bash
behave
```

---


## Atualização no GitHub

```bash
git add README.md
git commit -m "docs: readme padronizado"
git push
```
