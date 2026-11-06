from flask import Flask, render_template

app = Flask(__name__)

ITEMS = [
    {"id": "demo-track", "title": "Демо трек", "subtitle": "Автор"},
]


@app.route("/")
def home():
    return render_template("index.html", items=ITEMS)


@app.route("/item/<item_id>")
def item_page(item_id):
    # ТВОЯ ЗАДАЧА: если элемент не найден -> abort(404)
    found = next((it for it in ITEMS if it["id"] == item_id), None)
    if found is None:
        return "Не найдено", 404
    return f"<h1>{found['title']}</h1>"


# ТВОЯ ЗАДАЧА: Напиши @app.errorhandler(404)
# Верни render_template("404.html"), 404
