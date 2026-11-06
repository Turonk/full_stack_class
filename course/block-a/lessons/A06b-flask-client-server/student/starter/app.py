from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>PulseLab жив</h1><p>Поменяй эту строку и обнови вкладку.</p>"


@app.route("/radio")
def radio():
    # Этот маршрут мы собрали на стенде. Дома замени название на свою станцию.
    return "<h1>Night Circuit</h1><p>Станция стенда. Дома поставь имя своего радио.</p>"


# Зарегистрируй маршрут /about через @app.route("/about").
# Функция-обработчик возвращает твоё имя и одну фразу про твоё радио.
