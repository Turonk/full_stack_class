# A08 Слайды (проектор)

---

# PulseLab · Урок 8
Шаблоны и статика: переезд сайта на сервер
Группа смотрит **на стену**

---

# Retrieval · 60 сек
Сервер вернул строку: `return "<h1>PulseLab</h1>"`
1. Кто превратил теги в заголовок?
2. Удобно ли так возвращать сайт на 500 строк?

---

# Проблема
Разметка внутри кода Python — тупик
- Ломаются кавычки
- Нет подсветки HTML
- Невозможно поддерживать большой сайт

Решение: разделить код и верстку

---

# Архитектура папок Flask
```text
my_site/
  app.py            <- логика на Python
  templates/        <- HTML-шаблоны
    index.html
  static/           <- стили, картинки, звуки
    css/styles.css
    img/cover.svg
```

---

# render_template()
В Python импортируем функцию из Flask:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
```

Flask сам находит файл в папке `templates/`

---

# Ловушка относительных путей
Если написать в HTML просто:
`<link rel="stylesheet" href="style.css">`

- На главной `/` браузер запросит `/style.css` (404!)
- На странице `/item/track` браузер запросит `/item/style.css` (404!)

Статическим файлам нужен постоянный абсолютный адрес!

---

# url_for('static', filename=...)
Flask строит надежный веб-путь к любому файлу из папки `static/`:

```html
<!-- Подключение стилей -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">

<!-- Подключение картинки -->
<img src="{{ url_for('static', filename='img/cover.svg') }}" alt="Обложка">
```

Правило: `filename` указывает путь **внутри** папки `static/`

---

# Сеть под микроскопом
Один клик — серия HTTP-запросов:
1. `GET /` -> `200 OK` (получен HTML)
2. `GET /static/css/styles.css` -> `200 OK` (стили)
3. `GET /static/img/cover.svg` -> `200 OK` (картинка)

DevTools -> Network: все полоски должны быть зелеными!

---

# Checkpoint
1. В какую папку Flask смотрит при `render_template`?
2. Что подставит Flask вместо `{{ url_for('static', filename='css/styles.css') }}`?
3. Почему нельзя писать `filename='static/css/styles.css'`?

---

# You do · Критерий «готово»
- [ ] Создана структура `templates/` и `static/`
- [ ] `app.py` отдает `index.html` через `render_template`
- [ ] Все стили и картинки подключены через `url_for('static', ...)`
- [ ] Адрес в строке — `http://127.0.0.1:5000/` (не `file://`)
- [ ] В DevTools Network нет красных ошибок 404

---

# Exit ticket
1. Термин дня: `render_template` и `url_for`
2. Скриншот сайта на `127.0.0.1:5000` в чат группы
3. Прогноз: как завтра убрать копипасту 10 одинаковых карточек?
