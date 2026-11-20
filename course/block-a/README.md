# Блок A · MediaGameHub v1

Детальный план: [CURRICULUM.md](CURRICULUM.md).

## Спринты

| Спринт | Уроки | Продукт | Эталон | Showcase |
| --- | --- | --- | --- | --- |
| 1 | A01–A06 | Pulse FM, статический сайт | `projects/01-pulse-fm/` | A06 |
| 2 | A06b–A08 | Серверная база: Flask, шаблоны, статика | `projects/01b-flask-hub/` | — |
| 3 | A09–A14 | **Flask Hub v1** — данные в Python, POST, 404 | `projects/01b-flask-hub/` | **A14** |
| 4 | A15–A20 | **Interactive Hub** — JS, DOM, localStorage, fetch | `projects/04-interactive-hub/` | **A20** |
| 5 | A21–A26 | **MerchShop** — каталог, корзина, session, заказ | `projects/05-merchshop/` | **A26** |
| 6 | A27–A32 | **MediaGameHub v1** — склейка, API, токены | `projects/06-final/` | **A32** |
| Защита | A33–A34 | Репетиция + защита перед залом | `projects/06-final/` | A34 |

## Связь с 8 уроком

Урок 8 — точка входа в серверную разработку. Ученик перенёс свой статический сайт на Flask: `templates/index.html`, `static/css/style.css`, `static/img/`, `render_template()`, `url_for('static', ...)`.

Отсюда начинается непрерывная цепочка:

```
A08: сайт работает на 127.0.0.1:5000
 ↓
A09: карточки уходят в Python-список ITEMS
 ↓
A10: base.html, /item/<id>, многостраничность
 ↓
A11: POST, форма, redirect, flash
 ↓
A12: 404, polish, чек-лист
 ↓
A13: чистка, репетиция
 ↓
A14: Showcase Hub — защита Спринта 3
 ↓
A15: JS-база — к серверу добавляется game.js
 ↓
A16: DOM — счёт на странице
 ↓
A17: события — мини-игра
 ↓
A18: localStorage — результат сохраняется
 ↓
A19: /api/items + fetch — каталог без перезагрузки
 ↓
A20: Showcase Interactive Hub — защита Спринта 4
 ↓
A21: клонируем app.py — новый проект MerchShop
 ↓
A22: session — корзина на сервере
 ↓
A23: POST, валидация — форма заказа
 ↓
A24: polish — чистка, чек-лист
 ↓
A25: CSS-оформление — токены, адаптив
 ↓
A26: Showcase MerchShop — защита Спринта 5
 ↓
A27: склейка Hub + Shop в один app.py
 ↓
A28: единая навигация, base.html
 ↓
A29: JSON API — /api/items, /api/shop, /api/cart
 ↓
A30: fetch на всех страницах
 ↓
A31: CSS-токены — единый стиль
 ↓
A32: Showcase MediaGameHub v1 — защита Спринта 6
 ↓
A33: репетиция
 ↓
A34: защита блока
```

**Каждые 6 уроков — отчётный проект, готовый к показу на открытом уроке.**

## Архитектура проекта

```
projects/
  00-pulsedeck/        — стенд лектора
  01-pulse-fm/         — Спринт 1: статический сайт
  01b-flask-hub/       — Спринт 2–3: Flask Hub
  04-interactive-hub/  — Спринт 4: Hub + JS
  05-merchshop/        — Спринт 5: магазин
  06-final/            — Спринт 6: MediaGameHub v1
```

## Пакет урока

Каждый урок имеет пакет:
- `README.md` — точка входа для преподавателя
- `PLAN.md` — паспорт урока (результат, тайминг, теория, практика)
- `teacher/runbook.md` — тайминг
- `teacher/lecture.md` — речь
- `teacher/slides.md` — слайды
- `teacher/checks.md` — контроль
- `demo/app.py` — стенд
- `student/starter/` — стартер
- `student/task.md` — задача
- `solution/app.py` — эталон (только учитель)
- `homework.md` — домашка
