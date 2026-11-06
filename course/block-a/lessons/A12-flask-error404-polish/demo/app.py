from flask import Flask, abort, render_template

app = Flask(__name__)

ITEMS = [
    {"id": "pixel-tide", "title": "Pixel Tide", "subtitle": "Nova Park", "blurb": "Сингл стенда."},
]


@app.route("/")
def home():
    return render_template("index.html", items=ITEMS)


@app.route("/item/<item_id>")
def item_page(item_id):
    found = next((it for it in ITEMS if it["id"] == item_id), None)
    if found is None:
        abort(404)
    return f"<h1>{found['title']}</h1>"


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
