from behave import given, when, then
from models.livro_model import LivroModel

model = LivroModel()

@given('que eu tenho uma lista de livros padrão')
def step_impl(context):
    context.titulo = ""
    context.autor = ""
    context.ano = []

@when('eu filtro pelo título "{titulo}"')
def step_impl(context, titulo):
    context.titulo = titulo
    context.resultado = model.filtrar(titulo=titulo)

@when('eu filtro pelo autor "{autor}"')
def step_impl(context, autor):
    context.resultado = model.filtrar(autor=autor)

@when('eu filtro pelo intervalo de anos entre {inicio:d} e {fim:d}')
def step_impl(context, inicio, fim):
    context.resultado = model.filtrar(ano_inicio=inicio, ano_fim=fim)

@then('o sistema deve retornar {quantidade:d} livros')
def step_impl(context, quantidade):
    assert len(context.resultado) == quantidade