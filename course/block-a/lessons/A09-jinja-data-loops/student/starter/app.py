from flask import Flask, render_template

app = Flask(__name__)

# ТВОЯ ЗАДАЧА 1: Создай список ITEMS = [ {...}, {...} ] минимум из 6 карточек
ITEMS = [
    {
        "id": "demo-track",
        "title": "Первый трек",
        "subtitle": "Исполнитель",
        "meta": "3:00",
        "img": "cover.svg",
        "blurb": "Описание трека",
    },
]


@app.route("/")
def home():
    # ТВОЯ ЗАДАЧА 2: передай items=ITEMS в render_template
    return render_template("catalog.html", items=ITEMS)


if __name__ == "__main__":
    app.run(debug=True)
