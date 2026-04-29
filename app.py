from flask import Flask, render_template, request
from models import LivroModel

app = Flask(__name__)
model = LivroModel()


@app.route('/', methods=['GET'])
def index():
    titulo = request.args.get('titulo', '')
    autor = request.args.get('autor', '')

    try:
        ano_min = int(request.args.get('ano_min'))
        ano_max = int(request.args.get('ano_max'))
    except (TypeError, ValueError):
        ano_min, ano_max = None, None

    livros_filtrados = model.filtrar(titulo, autor, ano_min, ano_max)

    return render_template('index.html', livros=livros_filtrados)


if __name__ == '__main__':
    app.run(debug=True)