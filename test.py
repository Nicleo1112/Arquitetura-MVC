from models.livro_model import LivroModel

model = LivroModel()

def teste_filtrar_por_nome():
    resultado = model.filtrar(titulo="Harry Potter")
    assert len(resultado) == 2

def teste_filtrar_por_autor():
    resultado = model.filtrar(autor="J.K Rowling")
    assert len(resultado) == 2

def teste_filtrar_por_ano():
    resultado = model.filtrar(ano_inicio=1970, ano_fim=2000)
    assert len(resultado) == 2

def teste_filtrar_combinado():
    resultado = model.filtrar(titulo="Harry Potter", autor="J.K Rowling", ano_inicio=1970, ano_fim=2000)
    assert len(resultado) == 2

if __name__ == "__main__":
    teste_filtrar_por_nome()
    teste_filtrar_por_autor()
    teste_filtrar_por_ano()
    teste_filtrar_combinado()
    print("Todos os testes passaram")