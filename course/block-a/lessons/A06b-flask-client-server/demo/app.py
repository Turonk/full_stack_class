# Стенд учителя. Окружение подготовь до урока.
# Запуск из этой папки:
#   .\.venv\Scripts\python.exe -m flask --app app run --debug
# Открыть http://127.0.0.1:5000/ и http://127.0.0.1:5000/radio
# На I do маршрут /radio держи закомментированным. В We do класс диктует его обратно.

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>PulseLab жив</h1><p>Это ответ сервера, не файл с рабочего стола.</p>"


@app.route("/radio")
def radio():
    return "<h1>Night Circuit</h1><p>Станция стенда. Ученик на своём радио поставит своё имя.</p>"
