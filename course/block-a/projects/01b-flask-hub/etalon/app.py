from flask import Flask, abort, flash, redirect, render_template, request, url_for

app = Flask(__name__)
# Учебный ключ для подписи сессии и flash-сообщений
app.secret_key = "pulselab-dev-secret-key-2026"

ITEMS = [
    {
        "id": "pixel-tide",
        "title": "Pixel Tide",
        "subtitle": "Nova Park",
        "meta": "3:14",
        "img": "pixel.svg",
        "blurb": "Главный ночной сингл станции. Плотный синтезаторный бит и неоновый вайб.",
    },
    {
        "id": "low-battery",
        "title": "Low Battery",
        "subtitle": "Kite Club",
        "meta": "2:47",
        "img": "battery.svg",
        "blurb": "Лоуфай-трек для ночных сессий кодинга, когда на часах уже за полночь.",
    },
    {
        "id": "after-bell",
        "title": "After Bell",
        "subtitle": "Школьный коридор",
        "meta": "4:02",
        "img": "bell.svg",
        "blurb": "Шумные гитары и звук захлопывающихся дверей пустой школы.",
    },
    {
        "id": "cyber-drift",
        "title": "Cyber Drift",
        "subtitle": "Night Circuit",
        "meta": "3:50",
        "img": "drift.svg",
        "blurb": "Саундтрек ночного лаунчера PulseDeck: чистый синтвейв и скорость.",
    },
    {
        "id": "echo-pulse",
        "title": "Echo Pulse",
        "subtitle": "Modular Unit",
        "meta": "1:58",
        "img": "echo.svg",
        "blurb": "Минималистичный эмбиент для концентрации над сложными алгоритмами.",
    },
    {
        "id": "signal-lost",
        "title": "Signal Lost",
        "subtitle": "Radio 404",
        "meta": "2:15",
        "img": "signal.svg",
        "blurb": "Шум радиоприёмника на границе города, пойманный между частотами.",
    },
]


def make_slug(title: str) -> str:
    """Генерирует простой безопасный URL-slug из названия."""
    slug = "".join(ch.lower() if ch.isalnum() else "-" for ch in title).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "track"


@app.route("/")
def home():
    # На главной показываем топ-3 карточки из единого списка
    return render_template("index.html", items=ITEMS[:3])


@app.route("/catalog")
def catalog():
    # В каталоге отдаём весь список карточек
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


@app.route("/suggest", methods=["GET", "POST"])
def suggest():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        subtitle = request.form.get("subtitle", "").strip()
        meta = request.form.get("meta", "").strip()
        blurb = request.form.get("blurb", "").strip()
        img = request.form.get("img", "pixel.svg").strip()

        # Серверная валидация
        if not title:
            flash("Ошибка: название трека не может быть пустым.")
            return redirect(url_for("suggest"))

        # Создаём уникальный id
        base_id = make_slug(title)
        item_id = base_id
        counter = 2
        existing_ids = {it["id"] for it in ITEMS}
        while item_id in existing_ids:
            item_id = f"{base_id}-{counter}"
            counter += 1

        new_item = {
            "id": item_id,
            "title": title,
            "subtitle": subtitle or "Автор неизвестен",
            "meta": meta or "Новинка",
            "img": img,
            "blurb": blurb or "Добавлено слушателем через форму эфира.",
        }

        ITEMS.append(new_item)
        flash(f"Трек «{title}» успешно добавлен в эфир!")
        return redirect(url_for("catalog"))

    return render_template("suggest.html")


@app.errorhandler(404)
def page_not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
