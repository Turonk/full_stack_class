# Урок 25 · CSS-оформление: токены, адаптив, hover

Паспорт. Проект: [MerchShop](../../projects/05-merchshop/PROJECT.md). После [Polish](../A24-shop-polish/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: CSS-переменные — одна тема на все страницы.

## Результат

`static/css/tokens.css` — переменные для всей темы. `shop.css` — стили магазина. Hover/focus на карточках. Адаптив: колонка на 360px, сетка от 720px.

**Связь с A24:** логика работает, теперь оформление.

## Не входит

Склейка с Hub (A27). Только MerchShop.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | Чек-лист, что проверять |
| 5–20 | Теория | CSS-переменные, grid, media queries |
| 20–45 | I do | Стенд: tokens.css, grid, hover |
| 45–60 | We do | Класс диктует адаптив: 360px → 720px |
| 60–65 | Checkpoint | ≥70% класса видят hover и сетку |
| 65–70 | Пауза | |
| 70–100 | You do | Ученик оформляет MerchShop |
| 100–110 | Проверка | Сосед сузит окно до телефона |
| 110–120 | Выход | Завтра Showcase. Мост: защита |

## Теория

### CSS-переменные

```css
/* static/css/tokens.css */
:root {
    --color-bg: #1a1a2e;
    --color-surface: #16213e;
    --color-accent: #e94560;
    --color-text: #f0f0f0;
    --radius: 8px;
    --font-main: 'Inter', sans-serif;
}
```

### Grid для товаров

```css
.shop-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
}

@media (min-width: 720px) {
    .shop-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

### Hover на карточке

```css
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
```

## Live-coding на стенде

```css
/* shop.css */
@import 'tokens.css';

.shop-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
}

@media (min-width: 720px) {
    .shop-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

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

1. Создать `static/css/tokens.css` с переменными.
2. Создать `static/css/shop.css` — стили магазина.
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

Дополнить CSS:
- Добавить `tokens.css` для всей темы.
- Добавить hover на кнопках.
- Прислать скрин: MerchShop с hover.

## Мост к A26

Сегодня оформление готово. Завтра — Showcase MerchShop.
