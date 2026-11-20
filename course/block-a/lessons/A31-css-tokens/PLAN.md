# Урок 31 · CSS-токены: единый стиль для всего MediaGameHub

Паспорт. Проект: [MediaGameHub v1](../../projects/06-final/PROJECT.md). После [Fetch](../A30-fetch-pages/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: CSS-переменные — одна тема на все страницы.

## Результат

`static/css/tokens.css` — переменные для всей темы. `app.css` — общие стили. Hover/focus на карточках. Адаптив: 1 колонка на телефоне, 3 на десктопе.

**Связь с A30:** fetch работает, теперь единый стиль.

## Не входит

Showcase (A32). Только CSS.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | `fetch`, `jsonify`, `renderCards` |
| 5–20 | Теория | CSS-переменные, grid, media queries, hover |
| 20–45 | I do | Стенд: tokens.css, grid, hover |
| 45–60 | We do | Класс диктует адаптив: 360px → 720px |
| 60–65 | Checkpoint | ≥70% класса видят hover и сетку |
| 65–70 | Пауза | |
| 70–100 | You do | Ученик оформляет MediaGameHub |
| 100–110 | Проверка | Сосед сузит окно до телефона |
| 110–120 | Выход | Завтра Showcase. Мост: защита |

## Теория

### tokens.css

```css
/* static/css/tokens.css */
:root {
    --color-bg: #1a1a2e;
    --color-surface: #16213e;
    --color-accent: #e94560;
    --color-text: #f0f0f0;
    --color-success: #4caf50;
    --color-error: #f44336;
    --radius: 8px;
    --font-main: 'Inter', sans-serif;
    --shadow: 0 2px 8px rgba(0,0,0,0.2);
}
```

### app.css

```css
/* static/css/app.css */
@import 'tokens.css';

body {
    background: var(--color-bg);
    color: var(--color-text);
    font-family: var(--font-main);
    margin: 0;
}

.card {
    background: var(--color-surface);
    border-radius: var(--radius);
    padding: 16px;
    box-shadow: var(--shadow);
    transition: transform 0.2s;
}

.card:hover {
    transform: translateY(-4px);
}

.main-nav {
    display: flex;
    gap: 16px;
    padding: 16px;
    background: var(--color-surface);
}

.main-nav a {
    color: var(--color-text);
    text-decoration: none;
}

.main-nav a:hover {
    color: var(--color-accent);
}
```

### Grid

```css
.grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
}

@media (min-width: 720px) {
    .grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

## Live-coding на стенде

```css
/* tokens.css */
:root {
    --color-bg: #1a1a2e;
    --color-surface: #16213e;
    --color-accent: #e94560;
    --color-text: #f0f0f0;
    --radius: 8px;
}

/* app.css */
@import 'tokens.css';

.card {
    background: var(--color-surface);
    border-radius: var(--radius);
    padding: 16px;
    transition: transform 0.2s;
}

.card:hover {
    transform: translateY(-4px);
}
```

## Практика ученика

1. Создать `tokens.css` с переменными.
2. Создать `app.css` — общие стили.
3. Grid: 1 колонка на телефоне, 3 на десктопе.
4. Hover на карточке: `transform`, `box-shadow`.
5. Проверить: сузить окно → 1 колонка.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| Переменные не работают | Забыл `var(--name)` |
| Grid не адаптивный | Нет `@media` |
| Hover не работает | Нет `transition` |

## Домашка · 45–70 мин

Дополнить:
- Добавить `tokens.css` и `app.css`.
- Добавить hover на карточках.
- Прислать скрин: MediaGameHub с hover.

## Мост к A32

Сегодня оформление готово. Завтра — Showcase MediaGameHub v1.
