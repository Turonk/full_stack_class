# A11 · Задача ученика

Создай страницу `/suggest` с формой добавления трека в эфир и настрой серверный обработчик `POST`.

## Результат
1. В меню сайта появилась ссылка «Предложить трек».
2. На странице `/suggest` работает HTML-форма с полями ввода и кнопкой отправки.
3. Сервер проверяет обязательное поле названия: если поле пустое — возвращает уведомление об ошибке.
4. При успешном заполнении карточка сразу добавляется в список `ITEMS`, а браузер перенаправляется в каталог.
5. Нажатие F5 в каталоге не дублирует отправку формы.

## Шаги выполнения

1. В `app.py` объяви секретный ключ для flash-сообщений:
   ```python
   app.secret_key = "твой-учебный-секрет"
   ```
2. В `templates/base.html` добавь вывод flash-сообщений:
   ```html
   {% with messages = get_flashed_messages() %}
     {% if messages %}
       <div class="flash-messages">
         {% for msg in messages %}
           <p class="flash">{{ msg }}</p>
         {% endfor %}
       </div>
     {% endif %}
   {% endwith %}
   ```
3. Создай шаблон `templates/suggest.html`, наследующий `base.html`:
   ```html
   {% extends "base.html" %}

   {% block content %}
   <section class="form-box">
     <h1>Предложить трек в эфир</h1>
     <form method="post" action="{{ url_for('suggest') }}">
       <div class="field">
         <label for="title">Название трека *</label>
         <input type="text" id="title" name="title" required>
       </div>
       <div class="field">
         <label for="subtitle">Исполнитель / игра</label>
         <input type="text" id="subtitle" name="subtitle">
       </div>
       <div class="field">
         <label for="meta">Длительность / год</label>
         <input type="text" id="meta" name="meta">
       </div>
       <div class="field">
         <label for="img">Обложка</label>
         <select id="img" name="img">
           <!-- Подставь имена файлов, которые реально есть в твоей папке static/img/ -->
           <option value="cover1.svg">Обложка 1</option>
           <option value="cover2.svg">Обложка 2</option>
         </select>
       </div>
       <div class="field">
         <label for="blurb">Описание трека</label>
         <textarea id="blurb" name="blurb" rows="3"></textarea>
       </div>
       <button type="submit" class="btn">Отправить в ротацию</button>
     </form>
   </section>
   {% endblock %}
   ```
4. В `app.py` напиши обработчик маршрута с методами `GET` и `POST`:
   ```python
   from flask import flash, redirect, request, url_for

   @app.route("/suggest", methods=["GET", "POST"])
   def suggest():
       if request.method == "POST":
           title = request.form.get("title", "").strip()
           subtitle = request.form.get("subtitle", "").strip()
           meta = request.form.get("meta", "").strip()
           blurb = request.form.get("blurb", "").strip()
           img = request.form.get("img", "default.svg")

           if not title:
               flash("Название трека не может быть пустым!")
               return redirect(url_for("suggest"))

           item_id = title.lower().replace(" ", "-")
           ITEMS.append({
               "id": item_id,
               "title": title,
               "subtitle": subtitle or "Автор неизвестен",
               "meta": meta or "Новинка",
               "img": img,
               "blurb": blurb or "Добавлено слушателем через форму.",
           })
           flash(f"Трек «{title}» успешно добавлен в каталог!")
           return redirect(url_for("catalog"))

       return render_template("suggest.html")
   ```
5. Проверь работу: отправь форму и найди свою новую карточку в общем каталоге!

## Готово, когда
- [ ] Форма отправляет данные методом `POST`
- [ ] У каждого поля есть атрибут `name`
- [ ] Сервер валидирует пустые названия
- [ ] После успешного добавления срабатывает `redirect` на каталог
- [ ] Карточка появляется на странице каталога и открывается по клику
