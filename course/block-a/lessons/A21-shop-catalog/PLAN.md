# Урок 21 · Новый проект: каталог товаров

Паспорт. Проект: [MerchShop](../../projects/05-merchshop/PROJECT.md). После [Showcase Interactive Hub](../A20-showcase-interactive/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: клонируем Hub — добавляем каталог товаров.

## Результат

Ученик копирует свой `app.py` из Спринта 4. Добавляет `SHOP_ITEMS` (6+ товаров), маршрут `/shop`, шаблон `shop.html` с циклом `{% for item in shop_items %}`. На странице — карточки товаров с ценой и кнопкой «В корзину».

**Связь с A20:** ученик берёт **свой же** Interactive Hub. Не начинает с нуля — клонирует.

## Не входит

Корзина (A22), форма заказа (A23). Только каталог.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | Что делает `fetch`, `jsonify`, `localStorage` |
| 5–20 | Теория | Копирование проекта, `SHOP_ITEMS`, новый маршрут |
| 20–45 | I do | Стенд: копируем Hub, добавляем `/shop`, рендерим товары |
| 45–60 | We do | Класс диктует структуру товара: `id`, `name`, `price`, `img` |
| 60–65 | Checkpoint | ≥70% класса видят `/shop` с товарами |
| 65–70 | Пауза | |
| 70–100 | You do | Ученик клонирует Hub, добавляет `/shop` |
| 100–110 | Проверка | Сосед открывает `/shop` и проверяет товары |
| 110–120 | Выход | `session` — следующий урок. Мост: корзина |

## Теория

### Копирование проекта

```
copy app.py app_backup.py
copy templates/* templates_backup/
copy static/* static_backup/
```

Ученик копирует **свой** Hub-проект в новую папку (или добавляет маршруты в существующий `app.py`).

### `SHOP_ITEMS`

```python
SHOP_ITEMS = [
    {
        "id": "tshirt-pulse",
        "name": "Футболка Pulse",
        "price": 1200,
        "description": "Хлопок, чёрный",
        "img": "tshirt-pulse.jpg",
    },
    # ещё 5+ товаров
]
```

### Маршрут `/shop`

```python
@app.route("/shop")
def shop():
    return render_template("shop.html", shop_items=SHOP_ITEMS)
```

### `shop.html`

```html
{% extends "base.html" %}
{% block content %}
<h1>Магазин</h1>
<div class="shop-grid">
    {% for item in shop_items %}
    <article class="card">
        <img src="{{ url_for('static', filename='img/shop/' ~ item.img) }}" alt="{{ item.name }}">
        <h2>{{ item.name }}</h2>
        <p class="price">{{ item.price }} ₽</p>
        <p>{{ item.description }}</p>
        <button class="add-to-cart" data-id="{{ item.id }}">В корзину</button>
    </article>
    {% endfor %}
</div>
{% endblock %}
```

## Live-coding на стенде

```python
# app.py
SHOP_ITEMS = [
    {"id": "tshirt", "name": "Футболка", "price": 1200, "description": "Чёрная", "img": "tshirt.jpg"},
    {"id": "hoodie", "name": "Худи", "price": 3500, "description": "Серое", "img": "hoodie.jpg"},
    {"id": "cap", "name": "Кепка", "price": 800, "description": "Синяя", "img": "cap.jpg"},
]

@app.route("/shop")
def shop():
    return render_template("shop.html", shop_items=SHOP_ITEMS)
```

## Практика ученика

1. Скопировать свой Hub-проект (или добавить маршруты в существующий `app.py`).
2. Добавить `SHOP_ITEMS` — минимум 6 товаров.
3. Добавить маршрут `/shop`.
4. Создать `templates/shop.html` с циклом `{% for %}`.
5. Добавить картинки товаров в `static/img/shop/`.
6. Проверить: `/shop` показывает 6+ товаров.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| `TemplateNotFound` | Файл не в `templates/` |
| Картинки 404 | Путь `static/img/shop/` — проверь `item.img` |
| Цена не показывается | `{{ item.price }}` — проверь поле в `SHOP_ITEMS` |
| Кнопка «В корзину» не работает | Ещё нет обработчика — это следующий урок |

## Домашка · 45–70 мин

Дополнить `shop.html`:
- Добавить CSS для сетки товаров (2–3 колонки).
- Добавить цену с символом ₽.
- Прислать скрин: `/shop` с 6 товарами.

## Мост к A22

Сегодня товары на странице. Завтра — корзина: `session["cart"]`, добавление/удаление.
