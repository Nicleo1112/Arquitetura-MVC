class LivroModel:
    def __init__(self):
        self.livros = [
            {"Titulo": "Harry Potter e a Pedra Filosofal", "Autor": "J.K Rowling", "Ano": 1997},
            {"Titulo": "Harry Potter e a Câmara Secreta", "Autor": "J.K Rowling", "Ano": 1998},
            {"Titulo": "O Hobbit", "Autor": "Tolkien", "Ano": 1937},
            {"Titulo": "O Senhor dos Anéis", "Autor": "Tolkien", "Ano": 1954},
            {"Titulo": "Dom Casmurro", "Autor": "Machado de Assis", "Ano": 1899},
            {"Titulo": "Memórias Póstumas de Brás Cubas", "Autor": "Machado de Assis", "Ano": 1881},
            {"Titulo": "Clean Code", "Autor": "Robert C. Martin", "Ano": 2008},
            {"Titulo": "Clean Architecture", "Autor": "Robert C. Martin", "Ano": 2017},
            {"Titulo": "Python Crash Course", "Autor": "Eric Matthes", "Ano": 2015},
            {"Titulo": "Automate the Boring Stuff", "Autor": "Al Sweigart", "Ano": 2015},
            {"Titulo": "The Pragmatic Programmer", "Autor": "Andrew Hunt", "Ano": 1999},
            {"Titulo": "Design Patterns", "Autor": "Erich Gamma", "Ano": 1994},
            {"Titulo": "Refactoring", "Autor": "Martin Fowler", "Ano": 1999},
            {"Titulo": "Código Limpo", "Autor": "Robert C. Martin", "Ano": 2009},
            {"Titulo": "Algoritmos", "Autor": "Thomas H. Cormen", "Ano": 2009},
            {"Titulo": "Estruturas de Dados", "Autor": "Narasimha Karumanchi", "Ano": 2011},
            {"Titulo": "Redes de Computadores", "Autor": "Andrew S. Tanenbaum", "Ano": 2010},
            {"Titulo": "Sistemas Operacionais", "Autor": "Andrew S. Tanenbaum", "Ano": 2015},
            {"Titulo": "Engenharia de Software", "Autor": "Ian Sommerville", "Ano": 2011},
            {"Titulo": "Introdução à Programação", "Autor": "Deitel", "Ano": 2012},
            {"Titulo": "Java: Como Programar", "Autor": "Deitel", "Ano": 2016},
            {"Titulo": "C Programming Language", "Autor": "Kernighan", "Ano": 1988},
            {"Titulo": "Artificial Intelligence", "Autor": "Stuart Russell", "Ano": 2010},
            {"Titulo": "Deep Learning", "Autor": "Ian Goodfellow", "Ano": 2016},
            {"Titulo": "Banco de Dados", "Autor": "Elmasri", "Ano": 2015},
            {"Titulo": "Compiladores", "Autor": "Aho", "Ano": 2006},
            {"Titulo": "Computer Organization", "Autor": "Patterson", "Ano": 2013},
            {"Titulo": "Digital Design", "Autor": "Morris Mano", "Ano": 2012},
            {"Titulo": "Data Science Handbook", "Autor": "Jake VanderPlas", "Ano": 2016},
            {"Titulo": "Fluent Python", "Autor": "Luciano Ramalho", "Ano": 2015},
        ]

    def filtrar(self, titulo="", autor="", ano_inicio=None, ano_fim=None):
        resultado = []
        for livro in self.livros:
            if titulo and titulo.lower() not in livro["Titulo"].lower():
                continue
            if autor and autor.lower() not in livro["Autor"].lower():
                continue
            if ano_inicio is not None and ano_fim is not None:
                if livro["Ano"] < ano_inicio or livro["Ano"] > ano_fim:
                    continue
            resultado.append(livro)
        return resultado