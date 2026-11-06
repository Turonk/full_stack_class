from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# ТВОЯ ЗАДАЧА 1: Установи app.secret_key = "..." для работы flash-сообщений
app.secret_key = "pulse-secret-key"

ITEMS = [
    {
        "id": "demo-item",
        "title": "Демо трек",
        "subtitle": "Автор",
        "meta": "3:00",
        "img": "cover.svg",
        "blurb": "Описание",
    },
]


@app.route("/")
def home():
    return render_template("index.html", items=ITEMS)


@app.route("/catalog")
def catalog():
    return render_template("index.html", items=ITEMS)


# ТВОЯ ЗАДАЧА 2: Напиши @app.route("/suggest", methods=["GET", "POST"])
# Считай request.form.get("title")
# Проверь if not title -> redirect
# Добавь ITEMS.append(...) и сделай redirect(url_for('catalog'))
