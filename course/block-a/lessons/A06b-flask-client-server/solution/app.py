from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>PulseLab жив</h1><p>Это ответ сервера, не файл с рабочего стола.</p>"


@app.route("/radio")
def radio():
    return "<h1>Полуночный причал</h1><p>Моё радио играет, когда город уже спит.</p>"


@app.route("/about")
def about():
    return "<h1>Аня</h1><p>Веду ночной эфир и собираю треки сама.</p>"
