# A10 Слайды (проектор)

---

# PulseLab · Урок 10
Каркас и страница карточки
Группа смотрит **на стену**

---

# Retrieval · 60 сек
1. Как передать список `ITEMS` внутрь шаблона каталога?
2. В каких скобках пишется цикл `for` в Jinja?

---

# Проблема
На сайте 4 страницы: главная, каталог, карточка, об авторе
- Копировать шапку и стили в 4 файла?
- Изменили логотип — переписывать 4 файла?
- А если страниц будет 50?

Решение: каркас `base.html` и наследование

---

# Каркас: base.html
Один файл хранит всё общее:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
  <header class="top">
    <!-- Шапка и логотип для всего сайта -->
  </header>

  <main>
    {% block content %}{% endblock %}
  </main>

  <footer>...</footer>
</body>
</html>
```

---

# Наследование: extends
Дочерняя страница становится ультракороткой:

```html
{% extends "base.html" %}

{% block content %}
  <h1>Каталог эфира</h1>
  <!-- Только уникальный контент этой страницы! -->
{% endblock %}
```

Первая строка файла — всегда `{% extends "base.html" %}`

---

# Динамический маршрут
Один маршрут для сотен разных карточек:

```python
@app.route("/item/<item_id>")
def item_page(item_id):
    # Flask передает точную строку из URL в переменную item_id!
    found = None
    for it in ITEMS:
        if it["id"] == item_id:
            found = it
            break
    if found is None:
        return "Не найдено", 404
    return render_template("item.html", item=found)
```

---

# Ссылка на карточку в Jinja
Как в каталоге сослаться на динамическую страницу?

```html
<a href="{{ url_for('item_page', item_id=item.id) }}">
  Подробнее →
</a>
```

Flask сам подставит значение `item.id`:
`href="/item/pixel-tide"`

---

# Checkpoint
1. Что должно стоять первой строкой в `catalog.html`?
2. Что попадет в аргумент `item_id`, если URL `/item/after-bell`?
3. Что вернет сервер, если запрошен неизвестный `id`?

---

# You do · Критерий «готово»
- [ ] Создан общий каркас `base.html`
- [ ] `index.html` и `catalog.html` наследуют `base.html` через `extends`
- [ ] Работает маршрут `@app.route("/item/<item_id>")`
- [ ] Из каталога можно кликнуть на любую карточку и открыть её детальную страницу
- [ ] Шапка и стили работают на всех страницах одинаково

---

# Exit ticket
1. Термин дня: `extends`, `block`, параметр URL
2. Скриншот детальной страницы трека в чат группы
3. Прогноз: как завтра добавить новую карточку на сайт через браузер?
