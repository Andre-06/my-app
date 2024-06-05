from flask import Flask, render_template

app = Flask(__name__)


produtos_list = [
        {"nome": "Coca-Cola", "descricao": "bom"},
        {"nome": "Pepsi", "descricao": "medio"},
        {"nome": "Doritos", "descricao": "Suja a mao"},
        {"nome": "Caviar", "descricao": "nn sei"},
        {"nome": "Monster", "descricao": "gosto nao"},
    ]

@app.route("/")
def index():
    return '''<h1>Hello Word</h2> 
<br> 
<a href="/produtos">Produtos</a>'''

@app.route("/produtos")
def produtos():
    
    return render_template("produtos.html", produtos=produtos_list)

@app.route("/produtos/<nome>")
def produto(nome):
    if any([True for prod in produtos_list if prod["nome"] != nome]):
        return "Produto Nao Encontrado"
    return nome
