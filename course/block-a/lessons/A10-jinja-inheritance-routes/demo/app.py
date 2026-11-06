from flask import Flask, abort, render_template

app = Flask(__name__)

ITEMS = [
    {
        "id": "pixel-tide",
        "title": "Pixel Tide",
        "subtitle": "Nova Park",
        "meta": "3:14",
        "blurb": "Главный ночной трек стенда с глубоким синтовым басом.",
    },
    {
        "id": "low-battery",
        "title": "Low Battery",
        "subtitle": "Kite Club",
        "meta": "2:47",
        "blurb": "Спокойный лоуфай для концентрации над кодом.",
    },
]


@app.route("/")
def home():
    return render_template("index.html", items=ITEMS)


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


if __name__ == "__main__":
    app.run(debug=True)
