import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")



@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        text = request.form["animal"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un assistant intelligent"},
                {"role": "user", "content": "Explique simplement ce qu'est "+text+"?"},
                ],
            temperature=0,
            )
        return redirect(url_for("index", result=response['choices'][0]['message']['content']))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Propose trois noms pour un animal de compagnie qui est un superhéro.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
