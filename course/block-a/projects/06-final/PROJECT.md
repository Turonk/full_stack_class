# MediaGameHub v1 — Финальная сборка

- Спринт: A27–A32
- Защита: A32
- Стек: Flask, Jinja, CSS, JS, fetch, JSON API
- База: [Interactive Hub](projects/04-interactive-hub/PROJECT.md) + [MerchShop](projects/05-merchshop/PROJECT.md) (Спринты 4 и 5)

## История

Ученик имеет два мини-проекта на одном сервере: Hub (каталог карточек, мини-игра, форма, 404) и MerchShop (магазин, корзина, заказ). Теперь он склеивает их в единое приложение: одна навигация, единая шапка в `base.html`, единый CSS через `tokens.css`, JSON API для каталога и корзины, `fetch` без перезагрузки.

**Важно:** это не переписывание с нуля. Ученик берёт оба проекта и объединяет: копирует маршруты в один `app.py`, выносит общую шапку, делает единый `static/css/tokens.css`.

## Must-have

### Единое приложение

- Один `app.py` с маршрутами Hub + Shop + Game
- Единая навигация в `base.html`: Hub · Shop · Game
- `static/css/tokens.css` — CSS-переменные для всей темы
- `static/css/app.css` — общие стили, не дублируют `game.css` и `shop.css`

### JSON API

- `/api/items` — JSON карточек Hub
- `/api/shop` — JSON товаров
- `/api/cart` — JSON корзины
- Все API-маршруты отдают `jsonify`

### Fetch на страницах

- `/catalog` — каталог карточек через `fetch("/api/items")`
- `/shop` — каталог товаров через `fetch("/api/shop")`
- `/cart` — корзина через `fetch("/api/cart")`
- Функция `renderCards(items, container)` — универсальный рендер

### CSS-токены

```css
:root {
    --color-bg: #1a1a2e;
    --color-surface: #16213e;
    --color-accent: #e94560;
    --color-text: #f0f0f0;
    --radius: 8px;
    --font-main: 'Inter', sans-serif;
}
```

- Все страницы используют токены
- Нет жёстких цветов в компонентах
- Hover/focus на карточках

## Дерево файлов

```
app.py                          # все маршруты: Hub + Shop + Game + API
requirements.txt
README.md
templates/
  base.html                     # единая шапка: Hub · Shop · Game
  index.html                    # главная: Hub-герой + 3 карточки
  catalog.html                  # каталог карточек (fetch)
  item.html                     # карточка
  about.html                    # об авторе
  suggest.html                  # форма добавления
  404.html                      # своя страница ошибки
  game.html                     # мини-игра
  shop.html                     # каталог товаров (fetch)
  cart.html                     # корзина
static/
  css/
    tokens.css                  # CSS-переменные
    app.css                     # общие стили
    game.css                    # стили игры
    shop.css                    # стили магазина
  img/
    hub/                        # обложки карточек
    shop/                       # картинки товаров
  js/
    game.js                     # логика игры
    api.js                      # fetch + render
    cart.js                     # логика корзины
```

## Маршруты

| Путь | Метод | Страница |
| --- | --- | --- |
| `GET /` | GET | Главная: герой + 3 карточки |
| `GET /catalog` | GET | Каталог карточек (fetch) |
| `GET /item/<id>` | GET | Детальная карточка |
| `GET /about` | GET | Об авторе |
| `GET /suggest` | GET | Форма добавления |
| `POST /suggest` | POST | Добавление карточки |
| `GET /game` | GET | Мини-игра |
| `GET /shop` | GET | Каталог товаров (fetch) |
| `POST /api/cart/add` | POST | Добавить в корзину |
| `POST /api/cart/remove` | POST | Удалить из корзины |
| `GET /cart` | GET | Корзина |
| `POST /checkout` | POST | Оформление заказа |
| `GET /api/items` | GET | JSON карточек |
| `GET /api/shop` | GET | JSON товаров |
| `GET /api/cart` | GET | JSON корзины |
| любой другой | — | `404.html` |

## Критерий «проект готов»

- [ ] Сервер запускается: `flask --app app run --debug`
- [ ] Единая навигация: Hub · Shop · Game — работает на всех страницах
- [ ] `/catalog` — карточки через `fetch("/api/items")`, не `{% for %}`
- [ ] `/shop` — товары через `fetch("/api/shop")`, не `{% for %}`
- [ ] `/cart` — корзина через `fetch("/api/cart")`
- [ ] `/game` — игра работает, счёт в localStorage
- [ ] `/suggest` — форма добавляет карточку
- [ ] CSS-токены: нет жёстких цветов, hover/focus на карточках
- [ ] `/fake-path` — свой 404
- [ ] README: команды запуска, структура

## Защита на A32

До 6 минут на ученика.

1. Открыть `/` — единая навигация, герой.
2. Показать `/catalog` — fetch, JSON в Network.
3. Показать `/shop` — fetch, JSON в Network.
4. Перейти на `/game` — сыграть раунд.
5. Добавить товар в корзину, перейти на `/cart`.
6. Открыть `/api/items` — JSON в браузере.
7. Открыть `/fake` — свой 404.

Оценка по рубрике:

| | Не зачёт | Зачёт | Сильно |
| --- | --- | --- | --- |
| Единое приложение | Два отдельных проекта | Один `app.py`, одна навигация | Единый `base.html`, общий `static/` |
| API | Нет `/api/` | JSON возвращается, страницы на `fetch` | Может добавить новый endpoint |
| CSS | Жёсткие цвета, нет токенов | `tokens.css`, hover/focus | Адаптив, `prefers-reduced-motion` |
| Авторство | Тексты стенда | Свои карточки, товары, вопросы | Рассказывает архитектуру |

## Итоговый сценарий защиты

```
/ → /catalog (fetch) → /shop (fetch) → /game → /cart → /api/items → /fake (404)
```

Каждый шаг — 30–45 секунд. Итого ≤6 минут.

## Связь с A08

От первого шага на сервере до единого приложения с тремя страницами, API и fetch:

```
A08: render_template("index.html")
A09: ITEMS в Python, {% for %} в шаблоне
A10: base.html, /item/<id>
A11: POST, форма, redirect
A12: 404, polish
A13: Showcase Hub
A15: let/const, функции
A16: DOM, querySelector
A17: click, keydown
A18: localStorage
A19: /api/items, fetch
A20: Showcase Interactive Hub
A21: новый проект — Shop
A22: session, корзина
A23: POST, валидация
A24: polish
A25: CSS-оформление
A26: Showcase MerchShop
A27: склейка в один app.py
A28: единая навигация
A29: JSON API
A30: fetch на всех страницах
A31: CSS-токены
A32: Showcase MediaGameHub v1
A33: репетиция
A34: защита блока
```
