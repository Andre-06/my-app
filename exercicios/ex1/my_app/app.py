from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF, CNPJ

app = Flask(__name__)
cpf = CPF()
cnpj = CNPJ()


@app.route("/")
def home():
    return redirect(url_for("gerador", name="cpf"))


@app.route("/gerador/<name>")
def gerador(name):
    cod = ''
    if name == "cpf":
        cod = cpf.generate(True)
    if name == "cnpj":
        cod = cnpj.generate(True)
    
    return render_template("gerador.html", name=name.upper(), cod=cod)


@app.route("/validador/<name>")
def validador(name):
    return render_template("validador.html", name=name.upper())


@app.route("/resultado/<name>", methods=["POST"])
def resultado(name):
    cod = ''
    resultado = "Inválido"
    if name == "CPF":
        cod = request.form["CPF-form"]
        resultado = "Válido" if cpf.validate(cod) else "Inválido"
    if name == "CNPJ":
        cod = request.form["CNPJ-form"]
        resultado = "Válido" if cnpj.validate(cod) else "Inválido"
    
    return render_template("resultado.html", 
                           name=name.upper(),
                           cod=cod,
                           resul=resultado)
