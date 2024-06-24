from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF, CNPJ

app = Flask(__name__)
cpf = CPF()
cnpj = CNPJ()

@app.route("/gerador/<name>")
def gerador(name):
    cod = ''
    if name == "cpf":
        cod = cpf.generate(True)
    if name == "cnpj":
        cod = cnpj.generate(True)
    
    return render_template("gerador.html", name=name, cod=cod)

@app.route("/validador/<name>")
def validador(name):
    return render_template("validador.html", name=name)

@app.route("/resultado/<name>", methods=["POST"])
def resultado(name):
    cod = ''
    resultado = "Inválido"
    if name == "cpf":
        cod = request.form["cpf-form"]
        resultado = "Válido" if cpf.validate(cod) else "Inválido"
    if name == "cnpj":
        cod = request.form["cnpj-form"]
        resultado = "Válido" if cnpj.validate(cod) else "Inválido"
    
    return render_template("resultado.html", 
                           name=name,
                           cod=cod,
                           resul=resultado)
