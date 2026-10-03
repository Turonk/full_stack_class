from flask import Flask, flash, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "pulselab-dev-only-change-me"

HITS = [
    {"id": "pixel", "title": "Pixel Tide", "artist": "Nova Park", "length": "3:14"},
    {"id": "battery", "title": "Low Battery", "artist": "Kite Club", "length": "2:47"},
    {"id": "bell", "title": "After Bell", "artist": "Школьный коридор", "length": "4:02"},
]

PRODUCTS = [
    {"id": "hoodie", "title": "Худи Pulse", "price": 2490},
    {"id": "cap", "title": "Кепка Night Circuit", "price": 990},
    {"id": "sticker", "title": "Стикеры эквалайзер", "price": 250},
]

MESSAGES = []


@app.route("/")
def home():
    return render_template("index.html", hits=HITS)


@app.route("/music")
def music():
    return render_template("music.html", tracks=HITS)


@app.route("/game")
def game():
    return render_template("game.html")


@app.route("/shop")
def shop():
    return render_template("shop.html", products=PRODUCTS)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        text = request.form.get("text", "").strip()
        if not name:
            flash("Имя нельзя оставлять пустым")
            return redirect(url_for("contact"))
        MESSAGES.append({"name": name, "text": text})
        flash("Спасибо, сообщение ушло в учебный список")
        return redirect(url_for("contact"))
    return render_template("contact.html")


@app.route("/api/hits")
def api_hits():
    return jsonify(HITS)


@app.route("/api/products")
def api_products():
    return jsonify(PRODUCTS)


@app.errorhandler(404)
def not_found(_e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
