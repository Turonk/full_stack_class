# Урок 29 · JSON API: /api/items, /api/shop, /api/cart

Паспорт. Проект: [MediaGameHub v1](../../projects/06-final/PROJECT.md). После [Навигация](../A28-navigation/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: `jsonify` превращает Python-список в JSON.

## Результат

Три API-маршрута: `/api/items` (карточки), `/api/shop` (товары), `/api/cart` (корзина). Все отдают `jsonify`. Браузер может получить данные и нарисовать их.

**Связь с A28:** навигация работает, теперь данные через API.

## Не входит

`fetch` на страницах (A30). Только маршруты.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | `url_for`, `{% extends %}`, навигация |
| 5–20 | Теория | `jsonify`, три API-маршрута |
| 20–45 | I do | Стенд: `/api/items`, `/api/shop`, `/api/cart` |
| 45–60 | We do | Класс диктует структуру JSON |
| 60–65 | Checkpoint | ≥70% класса видят JSON в браузере |
| 65–70 | Пауза | |
| 70–100 | You do | Ученик добавляет API-маршруты |
| 100–110 | Проверка | Сосед открывает `/api/items` в браузере |
| 110–120 | Выход | Завтра — `fetch`. Мост: браузер рисует |

## Теория

### `/api/items`

```python
@app.route("/api/items")
def api_items():
    return jsonify(ITEMS)
```

### `/api/shop`

```python
@app.route("/api/shop")
def api_shop():
    return jsonify(SHOP_ITEMS)
```

### `/api/cart`

```python
@app.route("/api/cart")
def api_cart():
    return jsonify(session.get("cart", []))
```

### Результат в браузере

Открыть `/api/items`:
```json
[
  {"id": "pixel", "title": "Pixel Tide", "img": "pixel.jpg"},
  {"id": "neon", "title": "Neon Wave", "img": "neon.jpg"}
]
```

Открыть `/api/cart`:
```json
[
  {"id": "tshirt", "name": "Футболка", "price": 1200, "qty": 2}
]
```

## Live-coding на стенде

```python
@app.route("/api/items")
def api_items():
    return jsonify(ITEMS)

@app.route("/api/shop")
def api_shop():
    return jsonify(SHOP_ITEMS)

@app.route("/api/cart")
def api_cart():
    return jsonify(session.get("cart", []))
```

## Практика ученика

1. Добавить `/api/items` — `jsonify(ITEMS)`.
2. Добавить `/api/shop` — `jsonify(SHOP_ITEMS)`.
3. Добавить `/api/cart` — `jsonify(session.get("cart", []))`.
4. Проверить: открыть каждый маршрут в браузере → JSON.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| `session` не работает | Нет `app.secret_key` |
| JSON пустой | `session.get("cart", [])` — проверь, есть ли товары в корзине |
| `jsonify` не найден | Импорт: `from flask import jsonify` |

## Домашка · 45–70 мин

Дополнить:
- Добавить все три API-маршрута.
- Прислать скрин: `/api/items` в браузере.

## Мост к A30

Сегодня API отдаёт JSON. Завтра — `fetch` на страницах.
