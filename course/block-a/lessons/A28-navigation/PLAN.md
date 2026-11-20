# Урок 28 · Единая навигация: base.html на все страницы

Паспорт. Проект: [MediaGameHub v1](../../projects/06-final/PROJECT.md). После [Склейка](../A27-assemble/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: `base.html` — шаблон-родитель, все страницы наследуют.

## Результат

`base.html` с навигацией: Hub · Shop · Game. Все страницы (hub, shop, cart, checkout, game) используют `{% extends "base.html" %}`. `url_for` для ссылок.

**Связь с A27:** маршруты в одном файле, теперь единая навигация.

## Не входит

JSON API (A29), fetch (A30). Только навигация.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | `{% extends %}`, `{% block content %}`, `url_for` |
| 5–20 | Теория | Навигация в `base.html`, `url_for` для всех маршрутов |
| 20–45 | I do | Стенд: навигация Hub · Shop · Game |
| 45–60 | We do | Класс диктует пункты меню |
| 60–65 | Checkpoint | ≥70% класса видят навигацию на всех страницах |
| 65–70 | Пауза | |
| 70–100 | You do | Ученик добавляет навигацию в `base.html` |
| 100–110 | Проверка | Сосед кликает по пунктам меню |
| 110–120 | Выход | `url_for` — имя функции, не путь. Мост: API |

## Теория

### `base.html` с навигацией

```html
<!DOCTYPE html>
<html>
<head>
    <title>MediaGameHub</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/tokens.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/app.css') }}">
</head>
<body>
    <nav class="main-nav">
        <a href="{{ url_for('home') }}">Hub</a>
        <a href="{{ url_for('shop') }}">Shop</a>
        <a href="{{ url_for('game') }}">Game</a>
        <a href="{{ url_for('cart') }}">Cart</a>
    </nav>
    {% for message in get_flashed_messages() %}
    <p class="flash">{{ message }}</p>
    {% endfor %}
    {% block content %}{% endblock %}
</body>
</html>
```

### Использование в дочерних шаблонах

```html
{% extends "base.html" %}
{% block content %}
<h1>Каталог</h1>
<!-- содержимое -->
{% endblock %}
```

### `url_for` — имя функции, не путь

```html
<!-- Правильно: -->
<a href="{{ url_for('home') }}">Hub</a>

<!-- Неправильно: -->
<a href="/">Hub</a>
```

Если путь изменится — `url_for` обновится автоматически. Жёсткий `/` — нужно искать все ссылки.

## Live-coding на стенде

```html
<!-- base.html -->
<nav class="main-nav">
    <a href="{{ url_for('home') }}">Hub</a>
    <a href="{{ url_for('shop') }}">Shop</a>
    <a href="{{ url_for('game') }}">Game</a>
    <a href="{{ url_for('cart') }}">Cart</a>
</nav>
```

```html
<!-- catalog.html -->
{% extends "base.html" %}
{% block content %}
<h1>Каталог</h1>
<div id="catalog"></div>
{% endblock %}
```

## Практика ученика

1. Добавить навигацию в `base.html`: Hub · Shop · Game · Cart.
2. Использовать `url_for` для всех ссылок.
3. Проверить: навигация видна на всех страницах.
4. Проверить: клик по пунктам переводит на нужную страницу.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| `BuildError` | Имя во `url_for` не совпадает с именем функции |
| Навигация не видна | Забыл `{% extends "base.html" %}` |
| Ссылки ведут не туда | Проверяй имена функций в `@app.route` |

## Домашка · 45–70 мин

Дополнить:
- Добавить навигацию на все страницы.
- Проверить: все пункты работают.
- Прислать скрин: навигация на `/shop`.

## Мост к A29

Сегодня навигация работает. Завтра — JSON API для каталога и корзины.
