from flask import Flask, render_template

app = Flask(__name__)

ITEMS = [
    {
        "id": "pixel-tide",
        "title": "Pixel Tide",
        "subtitle": "Nova Park",
        "meta": "3:14",
        "img": "pixel.svg",
        "blurb": "Главный ночной сингл станции.",
    },
    {
        "id": "low-battery",
        "title": "Low Battery",
        "subtitle": "Kite Club",
        "meta": "2:47",
        "img": "battery.svg",
        "blurb": "Лоуфай-трек для ночных сессий.",
    },
    {
        "id": "after-bell",
        "title": "After Bell",
        "subtitle": "Школьный коридор",
        "meta": "4:02",
        "img": "bell.svg",
        "blurb": "Шумные гитары и звук пустой школы.",
    },
    {
        "id": "cyber-drift",
        "title": "Cyber Drift",
        "subtitle": "Night Circuit",
        "meta": "3:50",
        "img": "drift.svg",
        "blurb": "Синтвейв саундтрек лаунчера.",
    },
    {
        "id": "echo-pulse",
        "title": "Echo Pulse",
        "subtitle": "Modular Unit",
        "meta": "1:58",
        "img": "echo.svg",
        "blurb": "Минималистичный эмбиент.",
    },
    {
        "id": "signal-lost",
        "title": "Signal Lost",
        "subtitle": "Radio 404",
        "meta": "2:15",
        "img": "signal.svg",
        "blurb": "Шум радиоприемника между волнами.",
    },
]


@app.route("/")
def home():
    return render_template("catalog.html", items=ITEMS)


if __name__ == "__main__":
    app.run(debug=True)
