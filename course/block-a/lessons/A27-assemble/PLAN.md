# Урок 27 · Склейка: маршруты Hub + Shop в одном app.py

Паспорт. Проект: [MediaGameHub v1](../../projects/06-final/PROJECT.md). После [Showcase MerchShop](../A26-showcase-merchshop/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: склейка — не переписывание, а объединение маршрутов.

## Результат

Один `app.py` содержит маршруты Hub (`/`, `/catalog`, `/game`, `/api/items`) и Shop (`/shop`, `/cart`, `/checkout`, `/api/cart`). Оба проекта работают вместе.

**Связь с A26:** у ученика есть два мини-проекта. Сегодня они становятся одним.

## Не входит

Навигация (A28), JSON API (A29). Только маршруты.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | Маршруты Hub и Shop, что было в Спринтах 4 и 5 |
| 5–20 | Теория | Объединение `app.py`, копирование маршрутов |
| 20–45 | I do | Стенд: копирую Shop-маршруты в Hub-проект |
| 45–60 | We do | Класс диктует структуру: Hub → Shop → API |
| 60–65 | Checkpoint | ≥70% класса видят оба проекта в одном `app.py` |
| 65–70 | Пауза | |
| 70–100 | You do | Ученик склеивает Hub + Shop |
| 100–110 | Проверка | Сосед открывает `/game` и `/shop` |
| 110–120 | Выход | Завтра — единая навигация. Мост: base.html |

## Теория

### Структура объединённого `app.py`

```python
from flask import Flask, render_template, session, request, redirect, url_for, jsonify, flash

app = Flask(__name__)
app.secret_key = "dev-only"

# === Данные ===
ITEMS = [...]       # из Hub
SHOP_ITEMS = [...]  # из Shop

# === Hub-маршруты ===
@app.route("/")
def home(): ...

@app.route("/catalog")
def catalog(): ...

@app.route("/game")
def game(): ...

@app.route("/api/items")
def api_items(): ...

# === Shop-маршруты ===
@app.route("/shop")
def shop(): ...

@app.route("/cart")
def cart(): ...

@app.route("/checkout", methods=["GET", "POST"])
def checkout(): ...

@app.route("/api/cart/add", methods=["POST"])
def add_to_cart(): ...

# === 404 ===
@app.errorhandler(404)
def not_found(_error): ...
```

### Копирование

Ученик открывает свой Hub-проект и копирует в него:
1. `SHOP_ITEMS` из Shop-проекта.
2. Shop-маршруты из Shop-проекта.
3. Шаблоны `shop.html`, `cart.html`, `checkout.html`.

## Live-coding на стенде

```python
# 1. Копируем SHOP_ITEMS
SHOP_ITEMS = [
    {"id": "tshirt", "name": "Футболка", "price": 1200, "img": "tshirt.jpg"},
    # ...
]

# 2. Копируем маршруты
@app.route("/shop")
def shop():
    return render_template("shop.html", shop_items=SHOP_ITEMS)

@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    total = sum(item["price"] * item["qty"] for item in cart_items)
    return render_template("cart.html", cart=cart_items, total=total)
```

## Практика ученика

1. Открыть Hub-проект (свой из Спринта 4).
2. Скопировать `SHOP_ITEMS` из Shop-проекта.
3. Скопировать все Shop-маршруты.
4. Скопировать шаблоны `shop.html`, `cart.html`, `checkout.html`.
5. Проверить: `/game` и `/shop` работают.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| Дубли маршрутов | Проверяй имена функций: `home`, `shop`, `cart` — не должны дублироваться |
| `session` не работает | Нет `app.secret_key` |
| Шаблоны не найдены | Файлы не в `templates/` |

## Домашка · 45–70 мин

Дополнить:
- Добавить `SHOP_ITEMS` и `/shop` в Hub-проект.
- Проверить: оба проекта работают.
- Прислать скрин: `/game` и `/shop`.

## Мост к A28

Сегодня маршруты в одном файле. Завтра — единая навигация в `base.html`.
