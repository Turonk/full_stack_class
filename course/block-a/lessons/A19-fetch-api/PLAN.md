# Урок 19 · /api/items + fetch: браузер говорит с Flask

Паспорт. Проект: [Interactive Hub](../../projects/04-interactive-hub/PROJECT.md). После [localStorage](../A18-localstorage/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: сервер отдаёт JSON, браузер рисует карточки через `fetch`.

## Результат

Маршрут `@app.route("/api/items")` отдаёт `ITEMS` через `jsonify`. В `api.js` — `fetch("/api/items")`, функция `renderCards(items)` рисует карточки. Каталог `/catalog` больше не использует `{% for %}` — всё на JS.

**Связь с A18:** сегодня данные приходят с сервера, не из localStorage.

## Не входит

Корзина, session, MerchShop (Спринт 5). Только каталог карточек.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | `localStorage.setItem`, `getItem`, `removeItem` |
| 5–20 | Теория | `jsonify`, `fetch`, `async/await`, `renderCards` |
| 20–45 | I do | Стенд: `/api/items` → JSON, `fetch` → рендер |
| 45–60 | We do | Класс диктует функцию `renderCards(items, container)` |
| 60–65 | Checkpoint | ≥70% класса видят карточки, загруженные через fetch |
| 65–70 | Пауза | |
| 70–100 | You do | Ученик заменяет `{% for %}` на `fetch` |
| 100–110 | Проверка | Сосед открывает Network → JSON |
| 110–120 | Выход | `jsonify` превращает Python-список в JSON. Мост: Showcase |

## Теория

### `jsonify` — Python → JSON

```python
from flask import jsonify

@app.route("/api/items")
def api_items():
    return jsonify(ITEMS)
```

Результат в браузере (открыть `/api/items`):
```json
[
  {"id": "pixel", "title": "Pixel Tide", "img": "pixel.jpg"},
  {"id": "neon", "title": "Neon Wave", "img": "neon.jpg"}
]
```

### `fetch` — JavaScript → сервер

```javascript
fetch("/api/items")
    .then(response => response.json())
    .then(items => {
        console.log(items);
        renderCards(items);
    });
```

### `async/await` — современный синтаксис

```javascript
async function loadItems() {
    const response = await fetch("/api/items");
    const items = await response.json();
    renderCards(items);
}

loadItems();
```

### `renderCards` — рисовать карточки

```javascript
function renderCards(items, containerId = "#catalog") {
    const container = document.querySelector(containerId);
    container.innerHTML = "";

    items.forEach(function(item) {
        const card = document.createElement("article");
        card.className = "card";
        card.innerHTML = `
            <img src="/static/img/${item.img}" alt="${item.title}">
            <h2>${item.title}</h2>
            <p>${item.subtitle || ""}</p>
        `;
        container.append(card);
    });
}
```

## Live-coding на стенде

**app.py:**
```python
from flask import jsonify

@app.route("/api/items")
def api_items():
    return jsonify(ITEMS)
```

**static/js/api.js:**
```javascript
async function loadItems() {
    const response = await fetch("/api/items");
    const items = await response.json();
    renderCards(items);
}

function renderCards(items) {
    const container = document.querySelector("#catalog");
    container.innerHTML = "";
    items.forEach(function(item) {
        const card = document.createElement("article");
        card.className = "card";
        card.innerHTML = `
            <img src="/static/img/${item.img}" alt="${item.title}">
            <h2>${item.title}</h2>
        `;
        container.append(card);
    });
}

loadItems();
```

**catalog.html:**
```html
{% extends "base.html" %}
{% block content %}
<h1>Каталог</h1>
<div id="catalog"></div>
<script src="{{ url_for('static', filename='js/api.js') }}"></script>
{% endblock %}
```

## Практика ученика

1. В `app.py` добавить `@app.route("/api/items")` с `jsonify(ITEMS)`.
2. Создать `static/js/api.js` с `loadItems()` и `renderCards()`.
3. В `catalog.html` заменить `{% for %}` на `<div id="catalog"></div>`.
4. Подключить `api.js`.
5. Проверить: `/api/items` → JSON, `/catalog` → карточки на JS.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| `CORS` ошибка | Не нужно для локалки, но проверь путь: `/api/items`, не `http://...` |
| Карточки не появляются | `renderCards` вызывается после `fetch`, проверь `console.log` |
| Картинки 404 | Путь `src="/static/img/${item.img}"` — проверь `item.img` |
| `innerHTML` пустой | `container.innerHTML = ""` вызван до `append` |
| `fetch` не работает | Сервер запущен? `127.0.0.1:5000`, не `file://` |

## Домашка · 45–70 мин

Дополнить `api.js`:
- Добавить функцию `loadItemById(id)` — загружает одну карточку.
- Добавить функцию `renderSingleCard(item, containerId)` — рисует одну карточку.
- Прислать скрин: `/api/items` в браузере.

## Мост к A20

Сегодня каталог загружается через `fetch`. Завтра — Showcase: сервер, JS-игра, каталог без перезагрузки.
