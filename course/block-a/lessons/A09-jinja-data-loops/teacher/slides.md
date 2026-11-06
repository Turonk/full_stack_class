# A09 Слайды (проектор)

---

# PulseLab · Урок 9
Данные в Python и циклы Jinja
Группа смотрит **на стену**

---

# Retrieval · 60 сек
1. В какую папку Flask смотрит при `render_template("index.html")`?
2. Что подставит `{{ url_for('static', filename='css/styles.css') }}`?

---

# Проблема
10 карточек на сайте = 10 копий `<article>` в HTML
- Изменил верстку — правишь 10 раз
- Забыл закрыть тег в 7-й карточке — сломал весь ряд
- Данные замурованы в разметке

Решение: один источник правды в Python

---

# Данные в Python · Список словарей
В `app.py` описываем список карточек:

```python
ITEMS = [
    {
        "id": "pixel-tide",
        "title": "Pixel Tide",
        "subtitle": "Nova Park",
        "meta": "3:14",
        "img": "pixel.svg",
    },
    # ... еще карточки
]
```

Каждый элемент — отдельный словарь с ключами и значениями

---

# Передача в render_template
Передаем переменную в шаблон:

```python
@app.route("/catalog")
def catalog():
    return render_template("catalog.html", items=ITEMS)
```

`items` — имя переменной внутри HTML
`ITEMS` — наш список в Python

---

# Две пары скобок в Jinja
1. `{{ переменная }}` — **Печать**
   Подставить значение в HTML:
   `{{ item.title }}`

2. `{% команда %}` — **Логика**
   Циклы и условия:
   `{% for item in items %}`
   `{% if item.meta %}`

Внутри `{% %}` скобки `{{ }}` не нужны!

---

# Цикл в действии
Один трафарет повторяется для каждого словаря:

```html
<div class="row">
  {% for item in items %}
    <article class="card">
      <img src="{{ url_for('static', filename='img/' ~ item.img) }}" alt="{{ item.title }}">
      <h3>{{ item.title }}</h3>
      <p class="muted">{{ item.subtitle }}</p>
      {% if item.meta %}
        <p>{{ item.meta }}</p>
      {% endif %}
    </article>
  {% endfor %}
</div>
```

---

# Checkpoint
1. Чем отличаются скобки `{{ }}` и `{% %}`?
2. Что произойдет, если в списке `ITEMS` будет 0 элементов?
3. Что будет, если в шаблоне написать `{{ item.titl }}` с опечаткой?

---

# You do · Критерий «готово»
- [ ] В `app.py` создан список `ITEMS` минимум из 6 карточек
- [ ] У каждой карточки есть `id`, `title`, `subtitle`, `img`
- [ ] В HTML удалена копипаста: остался ровно один `<article>` в цикле `{% for %}`
- [ ] Все карточки корректно отображаются на странице `/catalog`
- [ ] Правка названия в `app.py` меняет сайт после F5

---

# Exit ticket
1. Зачем нужен уникальный `id` карточки?
2. Скриншот `ITEMS` в Python + готовый каталог в чат
3. Прогноз: как завтра сделать так, чтобы клик по карточке открывал отдельную страницу?
