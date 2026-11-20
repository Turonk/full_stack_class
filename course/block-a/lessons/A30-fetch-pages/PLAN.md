# Урок 30 · Fetch на всех страницах: каталог, shop, cart

Паспорт. Проект: [MediaGameHub v1](../../projects/06-final/PROJECT.md). После [JSON API](../A29-json-api/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: `fetch` читает JSON, JS рисует карточки.

## Результат

`/catalog` — `fetch("/api/items")`. `/shop` — `fetch("/api/shop")`. `/cart` — `fetch("/api/cart")`. Все страницы без `{% for %}` — всё на JS.

**Связь с A29:** API отдаёт JSON, сегодня браузер его использует.

## Не входит

CSS-токены (A31). Только fetch.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | `jsonify`, `/api/items`, `/api/shop`, `/api/cart` |
| 5–20 | Теория | `fetch`, `async/await`, `renderCards` |
| 20–45 | I do | Стенд: fetch для каталога, shop, cart |
| 45–60 | We do | Класс диктует универсальный `renderCards(items, container)` |
| 60–65 | Checkpoint | ≥70% класса видят карточки на fetch |
| 65–70 | Пауза | |
| 70–100 | You do | Ученик заменяет `{% for %}` на `fetch` |
| 100–110 | Проверка | Сосед открывает Network → JSON |
| 110–120 | Выход | CSS-токены завтра. Мост: единый стиль |

## Теория

### Универсальный `renderCards`

```javascript
function renderCards(items, containerId = "#list") {
    const container = document.querySelector(containerId);
    container.innerHTML = "";
    items.forEach(function(item) {
        const card = document.createElement("article");
        card.className = "card";
        card.innerHTML = `
            <img src="/static/img/${item.img || ''}" alt="${item.title || item.name}">
            <h2>${item.title || item.name}</h2>
            <p>${item.subtitle || item.description || ''}</p>
            ${item.price ? `<p class="price">${item.price} ₽</p>` : ''}
        `;
        container.append(card);
    });
}
```

### Загрузка каталога

```javascript
async function loadCatalog() {
    const response = await fetch("/api/items");
    const items = await response.json();
    renderCards(items, "#catalog");
}
loadCatalog();
```

### Загрузка shop

```javascript
async function loadShop() {
    const response = await fetch("/api/shop");
    const items = await response.json();
    renderCards(items, "#shop-grid");
}
loadShop();
```

### Загрузка cart

```javascript
async function loadCart() {
    const response = await fetch("/api/cart");
    const cart = await response.json();
    renderCart(cart);
}
loadCart();
```

## Live-coding на стенде

```javascript
// static/js/api.js
async function loadAll() {
    // Каталог
    const itemsRes = await fetch("/api/items");
    const items = await itemsRes.json();
    renderCards(items, "#catalog");

    // Shop
    const shopRes = await fetch("/api/shop");
    const shop = await shopRes.json();
    renderCards(shop, "#shop-grid");

    // Cart
    const cartRes = await fetch("/api/cart");
    const cart = await cartRes.json();
    renderCart(cart, "#cart-table");
}

loadAll();
```

## Практика ученика

1. Создать `static/js/api.js` с `renderCards` и `loadAll`.
2. В `catalog.html` заменить `{% for %}` на `<div id="catalog"></div>`.
3. В `shop.html` заменить `{% for %}` на `<div id="shop-grid"></div>`.
4. Подключить `api.js`.
5. Проверить: Network → JSON, страницы рисуются на JS.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| Карточки не появляются | `renderCards` вызывается после `fetch` |
| Картинки 404 | Путь `/static/img/` — проверь `item.img` |
| `fetch` не работает | Сервер запущен? `127.0.0.1:5000` |
| `innerHTML` пустой | `container.innerHTML = ""` до `append` |

## Домашка · 45–70 мин

Дополнить:
- Заменить `{% for %}` на `fetch` для каталога.
- Прислать скрин: Network → JSON.

## Мост к A31

Сегодня fetch работает. Завтра — CSS-токены для единого стиля.
