from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "demo-dev-secret-key"

ITEMS = [
    {
        "id": "pixel-tide",
        "title": "Pixel Tide",
        "subtitle": "Nova Park",
        "meta": "3:14",
    },
    {
        "id": "low-battery",
        "title": "Low Battery",
        "subtitle": "Kite Club",
        "meta": "2:47",
    },
]


@app.route("/")
def home():
    return render_template("index.html", items=ITEMS)


@app.route("/suggest", methods=["GET", "POST"])
def suggest():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        subtitle = request.form.get("subtitle", "").strip()

        if not title:
            flash("Ошибка: название обязательно!")
            return redirect(url_for("suggest"))

        item_id = title.lower().replace(" ", "-")
        ITEMS.append({
            "id": item_id,
            "title": title,
            "subtitle": subtitle or "Автор стенда",
            "meta": "Свежее",
        })
        flash(f"Карточка «{title}» успешно добавлена!")
        return redirect(url_for("home"))

    return render_template("suggest.html")


if __name__ == "__main__":
    app.run(debug=True)
