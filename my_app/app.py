from threading import Thread

from flask import Flask, render_template, request, redirect, url_for
from .models import Character, Item

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        name = request.form["nome"]
        ability = int(request.form["habilidade"])
        classes = request.form.get("classe")
        life = ability * 5

        character = Character(0, name, ability, life, classes)
        character.save()

        return redirect(url_for("home"))

    characters = Character.objects()
    return render_template("home.html", characters=characters)


@app.route("/novo-personagem")
def novo_personagem():
    return render_template("novo-personagem.html")


@app.route("/personagem/<id_personagem>/<edit>", methods=["POST", "GET"])
def personagem(id_personagem, edit):
    characters = Character.objects()
    character = [c for c in characters if c.id_character == int(id_personagem)][0]
    item_list = [item for item in Item.objects() if item.character_id == character.id_character]

    if request.method == "POST":
        if request.form.get("habilidade"):
            character.name = request.form["nome"]
            character.ability = int(request.form["habilidade"])
            character.classes = request.form.get("classe")
            character.life = character.ability * 5

            character.save()
            return redirect(f"/personagem/{character.id_character}/check")

        else:
            name = request.form["nome"]
            damage = request.form["dano"]
            critic = request.form.get("critico")
            description = request.form.get("descricao")

            item = Item(0, int(id_personagem), name, damage, critic, description)
            item.save()

            return redirect(f"/personagem/{character.id_character}/check")

    if character:
        return render_template("personagem.html",
                               character=character,
                               change='' if edit == 'edit' else 'disabled',
                               edit='check' if edit == 'edit' else 'edit',
                               visible=edit == 'check',
                               method='GET' if edit == 'check' else 'POST',
                               item_list=item_list)


@app.route("/personagem/<id_personagem>/novo-item")
def novo_item(id_personagem):
    characters = Character.objects()
    return render_template("novo-item.html", id_character=id_personagem)


@app.route("/remover/<model>/<id_model>")
def remover(model, id_model):
    if model == "personagem":
        Character.exclude(id_model)
        return redirect(url_for("home"))
    if model == "item":
        items = Item.objects()
        item = [i for i in items if i.id_item == int(id_model)][0]
        Item.exclude(id_model)
        return redirect(f"/personagem/{item.character_id}/check")


def run():
    app.run(host='0.0.0.0', port=5050)


if __name__ == '__main__':
    t = Thread(target=run)
    t.start()

