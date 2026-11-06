from flask import Flask, render_template

app = Flask(__name__)

ITEMS = [
    {
        "id": "pixel-tide",
        "title": "Pixel Tide",
        "subtitle": "Nova Park",
        "meta": "3:14",
        "img": "pixel.svg",
    },
    {
        "id": "low-battery",
        "title": "Low Battery",
        "subtitle": "Kite Club",
        "meta": "2:47",
        "img": "battery.svg",
    },
    {
        "id": "after-bell",
        "title": "After Bell",
        "subtitle": "Школьный коридор",
        "meta": "4:02",
        "img": "bell.svg",
    },
]


@app.route("/")
def home():
    return render_template("catalog.html", items=ITEMS)


if __name__ == "__main__":
    app.run(debug=True)
