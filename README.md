Sistema de Livraria - Arquitetura MVC e BDD
Este projeto é um MVP (Minimum Viable Product) de um sistema de busca de livros, refatorado para seguir a arquitetura MVC (Model-View-Controller) e validado utilizando a metodologia BDD (Behavior-Driven Development).

Tecnologias Utilizadas
Linguagem: Python 3.x

Framework Web: Flask (Controller e Rotas)

Template Engine: Jinja2 / HTML5 (View)

Estilização: Bootstrap 5 (Front-end)

Testes BDD: Behave (Gherkin)

Arquitetura MVC
O projeto foi organizado para separar as responsabilidades de forma clara:

Model (models.py): Contém a classe LivroModel, responsável pela gestão dos dados (lista de livros) e pela lógica de filtragem de busca.

View (templates/index.html): Interface do usuário desenvolvida em HTML e Bootstrap, que exibe o formulário de busca e a tabela de resultados.

Controller (app.py): Ponto de entrada da aplicação Flask. Ele gerencia as requisições HTTP, comunica-se com o Model para obter os dados e renderiza a View.

Metodologia BDD
O comportamento do sistema foi definido e testado utilizando arquivos .feature escritos em Gherkin. Isso garante que a lógica de negócio esteja funcionando conforme o esperado antes mesmo da interface ser utilizada.

Cenários Testados:
Filtragem por título (busca parcial).

Filtragem por autor.

Filtragem por intervalo de anos de publicação.

Como Executar o Projeto
1. Clonar o repositório
git clone https://github.com/Nicleo1112/Arquitetura-MVC.git
cd Arquitetura-MVC

2. Configurar o ambiente virtual e instalar dependências
Criar ambiente virtual
python -m venv .venv

Ativar ambiente (Windows)
.venv\Scripts\activate

Instalar bibliotecas necessárias
pip install flask behave

3. Rodar a aplicação (Front-end)
python app.py
Acesse no seu navegador: http://127.0.0.1:5000

4. Rodar os testes BDD
behave
