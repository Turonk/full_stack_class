# Урок 23 · Форма заказа: POST, валидация, flash

Паспорт. Проект: [MerchShop](../../projects/05-merchshop/PROJECT.md). После [Корзина](../A22-cart-session/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: форма → валидация → flash → redirect.

## Результат

Страница `/checkout` с формой: `name`, `email`, `address`. `POST /checkout` → валидация → `flash` → очистка корзины. Пустое имя → ошибка. Email без `@` → ошибка.

**Связь с A22:** корзина на сервере, теперь можно оформить заказ.

## Не входит

CSS-оформление (A25). Только логика.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | `session["cart"]`, добавление, удаление |
| 5–20 | Теория | `request.form`, валидация, `flash`, `redirect` |
| 20–45 | I do | Стенд: форма, проверка, flash, очистка корзины |
| 45–60 | We do | Класс диктует проверку email: `@` в строке |
| 60–65 | Checkpoint | ≥70% класса видят flash-сообщение |
| 65–70 | Пауза | |
| 70–100 | You do | Ученик добавляет форму заказа |
| 100–110 | Проверка | Сосед отправляет пустую форму, проверяет ошибку |
| 110–120 | Выход | `flash` требует `secret_key`. Мост: polish |

## Теория

### Форма

```html
<form method="post" action="{{ url_for('checkout') }}">
    <label>Имя: <input name="name" required></label>
    <label>Email: <input name="email" type="email"></label>
    <label>Адрес: <textarea name="address"></textarea></label>
    <button type="submit">Оформить</button>
</form>
```

### Обработчик

```python
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        address = request.form.get("address", "").strip()

        if not name:
            flash("Нужно имя")
            return redirect(url_for("checkout"))
        if "@" not in email:
            flash("Нужен корректный email")
            return redirect(url_for("checkout"))

        # Заказ принят
        flash("Заказ принят! Спасибо.")
        session["cart"] = []  # Очистить корзину
        return redirect(url_for("shop"))

    return render_template("checkout.html")
```

### Отображение flash

```html
{% for message in get_flashed_messages() %}
<p class="flash">{{ message }}</p>
{% endfor %}
```

## Live-coding на стенде

```python
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if not name:
            flash("Нужно имя")
            return redirect(url_for("checkout"))
        if "@" not in email:
            flash("Нужен email с @")
            return redirect(url_for("checkout"))

        flash("Заказ принят!")
        session["cart"] = []
        return redirect(url_for("shop"))

    return render_template("checkout.html")
```

## Практика ученика

1. Создать `checkout.html` с формой.
2. Добавить маршрут `/checkout` (GET/POST).
3. Валидация: имя не пустое, email содержит `@`.
4. `flash` с сообщением.
5. Очистка `session["cart"]` после успеха.
6. Проверить: пустая форма → ошибка, нормальная → success.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| `flash` не работает | Нет `secret_key` |
| Поля пустые | Нет `name` в форме или `request.form.get` |
| После POST форма не очищается | Нет `redirect` — ответ POST на той же странице |
| Корзина не очищается | Забыл `session["cart"] = []` |

## Домашка · 45–70 мин

Дополнить форму:
- Добавить поле `address`.
- Добавить проверку: адрес не пустой.
- Прислать скрин: ошибка и success.

## Мост к A24

Сегодня форма работает. Завтра — polish, чистка, чек-лист.
