# A10 · Задача ученика

Выдели единый каркас сайта в `base.html` и настрой динамические страницы карточек по адресу `/item/<item_id>`.

## Результат
1. Шапка и подвал описаны один раз в `base.html` и не дублируются в других шаблонах.
2. В каталоге каждая карточка содержит ссылку «Подробнее →».
3. При клике на карточку открывается отдельная страница с её заголовком, картинкой и текстом `blurb`.
4. URL страницы соответствует `id` карточки: например `http://127.0.0.1:5000/item/pixel-tide`.

## Шаги выполнения

1. В папке `templates/` создай файл `base.html`:
   - Перенеси туда теги `<html>`, `<head>`, подключение CSS через `url_for`, свою шапку `<header>` и меню.
   - Внутри тега `<main>` объяви блок контента:
     ```html
     <main>
       {% block content %}{% endblock %}
     </main>
     ```
2. Отредактируй `index.html` и `catalog.html`:
   - Удали дублирующиеся теги шапки и стилей.
   - Первой строкой поставь `{% extends "base.html" %}`.
   - Оберни содержимое страницы в `{% block content %} ... {% endblock %}`.
3. В `app.py` добавь маршрут с динамическим параметром:
   ```python
   @app.route("/item/<item_id>")
   def item_page(item_id):
       found = None
       for it in ITEMS:
           if it["id"] == item_id:
               found = it
               break
       if found is None:
           return "Карточка не найдена", 404
       return render_template("item.html", item=found)
   ```
4. Создай шаблон `templates/item.html`, наследующий `base.html`:
   ```html
   {% extends "base.html" %}

   {% block content %}
   <section class="item-view">
     <img class="cover-img" src="{{ url_for('static', filename='img/' ~ item.img) }}" alt="{{ item.title }}">
     <h1>{{ item.title }}</h1>
     <p class="muted">{{ item.subtitle }} · {{ item.meta }}</p>
     <p class="blurb">{{ item.blurb }}</p>
     <a class="card-link" href="{{ url_for('home') }}">← Назад к каталогу</a>
   </section>
   {% endblock %}
   ```
5. В цикле каталога добавь ссылку на страницу карточки:
   ```html
   <a class="card-link" href="{{ url_for('item_page', item_id=item.id) }}">Подробнее →</a>
   ```
6. Проверь переходы: кликни по нескольким карточкам и вернись обратно.

## Готово, когда
- [ ] Шапка сайта едина на всех страницах и задана в `base.html`
- [ ] Маршрут `/item/<item_id>` открывает нужную карточку
- [ ] По ссылке «Назад» происходит возврат в каталог
- [ ] Несуществующий `id` (например `/item/test12345`) возвращает ошибку 404
