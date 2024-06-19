from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


produtos_list = [
        {"nome": "Coca-Cola", "descricao": "bom", "preco": 10, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlm3PvdCPBSqkzNhPIKGYv_8kyrn21DwcIxA&s"},
        {"nome": "Pepsi", "descricao": "medio", "preco": 5, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSluZmJ401G7ReB_baCN175fFPlh5nPgVqVHA&s"},
        {"nome": "Doritos", "descricao": "Suja a mao", "preco": 400, "img": "https://avatars.githubusercontent.com/u/6484812?v=4"}
]

@app.route("/")
def home():
    return render_template("home.html")



@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=produtos_list)


@app.route("/produtos/<nome>")
def produto(nome):
    for produto in produtos_list:
        if produto["nome"] == nome:
            return render_template("produto.html", produto=produto)
    else:
        return "produto nao encontrado"


@app.route("/produtos/cadastro")
def cadastro():
    return render_template("cadastro-produto.html")


@app.route("/produtos", methods=['POST'])
def cadastrar_produto():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    preco = request.form["preco"]
    img = request.form["img"]

    produto = {"nome": nome, "descricao": descricao, 
               "preco": preco, "img": img}

    produtos_list.append(produto)

    return redirect(url_for("produtos"))

# um postman pra cada rota
# adicionar preço e imagem
# imagem em url

