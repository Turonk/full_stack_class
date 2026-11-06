from flask import Flask, render_template

app = Flask(__name__)

ITEMS = [
    {
        "id": "track-1",
        "title": "Первый трек",
        "subtitle": "Автор",
        "meta": "3:00",
        "img": "cover.svg",
        "blurb": "Описание трека для детальной страницы.",
    },
]


@app.route("/")
def home():
    return render_template("index.html", items=ITEMS)


# ТВОЯ ЗАДАЧА:
# Напиши маршрут @app.route("/item/<item_id>")
# Найди элемент в ITEMS по item["id"] == item_id
# Верни render_template("item.html", item=found)
