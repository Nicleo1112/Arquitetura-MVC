from flask import Blueprint, render_template, request
from models.livro_model import LivroModel

livro_bp = Blueprint('livro', __name__)
model = LivroModel()

@livro_bp.route('/', methods=['GET'])
def index():
    titulo = request.args.get('titulo', '')
    autor = request.args.get('autor', '')
    try:
        ano_min = int(request.args.get('ano_min'))
        ano_max = int(request.args.get('ano_max'))
    except (TypeError, ValueError):
        ano_min, ano_max = None, None

    livros = model.filtrar(titulo, autor, ano_min, ano_max)
    return render_template('index.html', livros=livros)