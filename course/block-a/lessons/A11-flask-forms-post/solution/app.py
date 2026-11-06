from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "pulse-secret-key-2026"

ITEMS = [
    {
        "id": "pixel-tide",
        "title": "Pixel Tide",
        "subtitle": "Nova Park",
        "meta": "3:14",
        "img": "pixel.svg",
        "blurb": "Главный ночной трек станции.",
    },
    {
        "id": "low-battery",
        "title": "Low Battery",
        "subtitle": "Kite Club",
        "meta": "2:47",
        "img": "battery.svg",
        "blurb": "Лоуфай для концентрации.",
    },
]


@app.route("/")
def home():
    return render_template("index.html", items=ITEMS)


@app.route("/catalog")
def catalog():
    return render_template("catalog.html", items=ITEMS)


@app.route("/suggest", methods=["GET", "POST"])
def suggest():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        subtitle = request.form.get("subtitle", "").strip()
        meta = request.form.get("meta", "").strip()
        blurb = request.form.get("blurb", "").strip()
        img = request.form.get("img", "pixel.svg")

        if not title:
            flash("Название трека обязательно для заполнения!")
            return redirect(url_for("suggest"))

        item_id = title.lower().replace(" ", "-")
        ITEMS.append({
            "id": item_id,
            "title": title,
            "subtitle": subtitle or "Автор неизвестен",
            "meta": meta or "Новинка",
            "img": img,
            "blurb": blurb or "Добавлено через форму эфира.",
        })
        flash(f"Трек «{title}» успешно добавлен в эфир!")
        return redirect(url_for("catalog"))

    return render_template("suggest.html")


if __name__ == "__main__":
    app.run(debug=True)
