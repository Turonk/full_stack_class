from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>PulseLab жив</h1><p>Это уже не файл, это ответ сервера.</p>"


@app.route("/about")
def about():
    return "<p>Страница ученика — подставь своё имя.</p>"
