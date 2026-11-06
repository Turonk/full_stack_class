from flask import Flask, abort, render_template

app = Flask(__name__)

ITEMS = [
    {
        "id": "pixel-tide",
        "title": "Pixel Tide",
        "subtitle": "Nova Park",
        "meta": "3:14",
        "img": "pixel.svg",
        "blurb": "Главный ночной трек станции. Плотный синтезаторный бит.",
    },
    {
        "id": "low-battery",
        "title": "Low Battery",
        "subtitle": "Kite Club",
        "meta": "2:47",
        "img": "battery.svg",
        "blurb": "Лоуфай-трек для ночных сессий кодинга.",
    },
    {
        "id": "after-bell",
        "title": "After Bell",
        "subtitle": "Школьный коридор",
        "meta": "4:02",
        "img": "bell.svg",
        "blurb": "Шумные гитары и звук пустой школы.",
    },
]


@app.route("/")
def home():
    return render_template("index.html", items=ITEMS)


@app.route("/catalog")
def catalog():
    return render_template("catalog.html", items=ITEMS)


@app.route("/item/<item_id>")
def item_page(item_id):
    found = None
    for it in ITEMS:
        if it["id"] == item_id:
            found = it
            break
    if found is None:
        abort(404)
    return render_template("item.html", item=found)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
