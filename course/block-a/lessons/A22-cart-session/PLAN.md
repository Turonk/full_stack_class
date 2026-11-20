# Урок 22 · Корзина в session

Паспорт. Проект: [MerchShop](../../projects/05-merchshop/PROJECT.md). После [Каталог товаров](../A21-shop-catalog/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: `session` — данные на сервере, привязанные к браузеру.

## Результат

`session["cart"]` — список `{id, name, price, qty}`. Кнопка «В корзину» → `POST /api/cart/add`. Страница `/cart` — таблица товаров, сумма, удаление.

**Связь с A21:** товары на странице, теперь можно добавить в корзину.

## Не входит

Форма заказа (A23). Только корзина.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | `SHOP_ITEMS`, маршрут `/shop`, `{% for %}` |
| 5–20 | Теория | `session`, `secret_key`, добавление/удаление |
| 20–45 | I do | Стенд: `session["cart"]`, добавление, сумма |
| 45–60 | We do | Класс диктует удаление позиции |
| 60–65 | Checkpoint | ≥70% класса видят корзину |
| 65–70 | Пауза | |
| 70–100 | You do | Ученик добавляет корзину |
| 100–110 | Проверка | Сосед добавляет товар, проверяет сумму |
| 110–120 | Выход | `session` vs `localStorage`. Мост: форма заказа |

## Теория

### `session` — данные на сервере

```python
from flask import Flask, session

app = Flask(__name__)
app.secret_key = "dev-only"  # обязательно для session
```

### Добавление в корзину

```python
@app.route("/api/cart/add", methods=["POST"])
def add_to_cart():
    item_id = request.form.get("item_id")
    # Найти товар в SHOP_ITEMS
    product = None
    for item in SHOP_ITEMS:
        if item["id"] == item_id:
            product = item
            break
    if not product:
        return "Товар не найден", 404
    # Добавить в session
    if "cart" not in session:
        session["cart"] = []
    # Проверить, есть ли уже в корзине
    found = False
    for cart_item in session["cart"]:
        if cart_item["id"] == item_id:
            cart_item["qty"] += 1
            found = True
            break
    if not found:
        session["cart"].append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "qty": 1
        })
    return redirect(url_for("cart"))
```

### Страница корзины

```python
@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    total = sum(item["price"] * item["qty"] for item in cart_items)
    return render_template("cart.html", cart=cart_items, total=total)
```

### `cart.html`

```html
{% extends "base.html" %}
{% block content %}
<h1>Корзина</h1>
{% if cart|length == 0 %}
<p>Корзина пуста</p>
{% else %}
<table>
    {% for item in cart %}
    <tr>
        <td>{{ item.name }}</td>
        <td>{{ item.price }} ₽</td>
        <td>x{{ item.qty }}</td>
        <td>{{ item.price * item.qty }} ₽</td>
        <td>
            <form method="post" action="{{ url_for('remove_from_cart', item_id=item.id) }}">
                <button type="submit">Удалить</button>
            </form>
        </td>
    </tr>
    {% endfor %}
</table>
<h2>Итого: {{ total }} ₽</h2>
<a href="{{ url_for('checkout') }}">Оформить заказ</a>
{% endif %}
{% endblock %}
```

## Live-coding на стенде

```python
# Кнопка на shop.html:
<form method="post" action="{{ url_for('add_to_cart') }}">
    <input type="hidden" name="item_id" value="{{ item.id }}">
    <button type="submit">В корзину</button>
</form>
```

## Практика ученика

1. Добавить `app.secret_key = "dev-only"`.
2. Добавить маршрут `/api/cart/add` (POST).
3. Добавить маршрут `/cart` (GET).
4. Создать `cart.html` с таблицей.
5. Добавить кнопку «Удалить» для каждой позиции.
6. Проверить: добавление → `/cart` показывает товары и сумму.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| `RuntimeError: secret_key is not set` | Нет `app.secret_key` |
| Корзина пустая после обновления | `session` работает, но проверь `redirect` |
| Товар дублируется | Не проверяешь `found` перед `append` |
| Сумма не считается | `item.price * item.qty` — проверь типы |

## Домашка · 45–70 мин

Дополнить корзину:
- Добавить функцию `remove_from_cart(item_id)`.
- Добавить страницу `/cart` с суммой.
- Прислать скрин: корзина с 2 товарами.

## Мост к A23

Сегодня корзина на сервере. Завтра — форма заказа с валидацией.
