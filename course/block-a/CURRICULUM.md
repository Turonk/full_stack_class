# Блок A · детальный учебный план

34 урока × 120 мин. Продукт года: MediaGameHub v1. Во втором спринте каждый ученик переводит свой сайт из спринта 1 на Flask.

Тайминг: [`../teacher/RHYTHM.md`](../teacher/RHYTHM.md). Пакет урока: `README.md` → runbook / slides / demo / student / checks.

Старые папки `A07`–`A12` (CSS) и `A25`–`A30` (ранний Flask) на диске не удалены. Порядок преподавания — таблицы ниже. Уроки 8–13 пока в виде паспортов: полный пакет со слайдами собирается отдельно.

## Спринт 1 · A01–A06 · витрина Pulse FM

- **PulseDeck** — стенд лектора. Папка `projects/00-pulsedeck/`.
- **Pulse FM** — проект ученика к A06. Не копировать тексты стенда.

| Код | Хук для зала | Ядро | Must-have к концу | Hub |
| --- | --- | --- | --- | --- |
| A01 | F12 в Discord / Steam | Каркас + CSS-файл с первой минуты | Тёмный баннер, слоган, кнопка | [README](lessons/A01-first-screen-style/README.md) |
| A02 | Коробка vs товар внутри | Box model, border-box | Карточка с padding и radius | [README](lessons/A02-box-model/README.md) |
| A03 | Почему обложки Spotify квадратные | Fonts, object-fit, alt | Обложка не сплющена | [README](lessons/A03-type-fonts-media/README.md) |
| A04 | Шапка Discord: лого слева | Flex, gap, space-between | Шапка в один ряд | [README](lessons/A04-flex-header/README.md) |
| A05 | Карточка «подпрыгивает» | wrap, hover, focus, transition | 3 карточки + отклик | [README](lessons/A05-cards-hover/README.md) |
| A06 | Родители в зале | Showcase ≤6 мин × ученик | Чек-лист Pulse FM | [README](lessons/A06-showcase-pulse-fm/README.md) |

## Спринт 2 · A07–A13 · Flask, свой сайт как серверное приложение

Замыкающий проект: [Pulse FM / авторский хаб 2.0](projects/01b-flask-hub/PROJECT.md).

Один концепт на урок. Урок 7 уже собран пакетом. Уроки 8–13 — паспорта к сборке пакетов.

| Урок | Код | Ядро | Must-have к концу | План |
| --- | --- | --- | --- | --- |
| 7 | A06b | Клиент, сервер, URL, `GET`, маршрут, обработчик, тело ответа | `/`, `/radio`, свой `/about` из Python | [пакет](lessons/A06b-flask-client-server/README.md) |
| 8 | A08 | `templates/`, `render_template`, `static/`, `url_for` | Свой сайт спринта 1 открывается с `127.0.0.1:5000` со своими CSS и картинками | [паспорт](lessons/A08-flask-templates-static/PLAN.md) |
| 9 | A09 | Список словарей в Python, `{{ }}`, `{% for %}` | Каталог карточек рисуется одним циклом, данные не скопированы в HTML | [паспорт](lessons/A09-jinja-data-loops/PLAN.md) |
| 10 | A10 | `base.html`, `{% extends %}`, `/item/<item_id>` | Общая шапка и переход с каталога на карточку | [паспорт](lessons/A10-jinja-inheritance-routes/PLAN.md) |
| 11 | A11 | `POST`, `request.form`, redirect, `flash` | Форма `/suggest` добавляет карточку в каталог | [паспорт](lessons/A11-flask-forms-post/PLAN.md) |
| 12 | A12 | `@app.errorhandler(404)`, пустые поля, чек-лист защиты | Свой `404.html`, пустая форма не портит список | [паспорт](lessons/A12-flask-error404-polish/PLAN.md) |
| 13 | A13 | Showcase ≤6 мин × ученик | Питч: страницы, `ITEMS`, живой POST, 404 | [паспорт](lessons/A13-showcase-flask-hub/PLAN.md) |

Пакеты CSS `A07`–`A12` в этом спринте не ведём. Старые Flask-уроки `A25`–`A30` этим спринтом закрыты: клиент-серверная лекция уже прочитана на уроке 7.

## Спринт 3 · A14–A19 · интерфейс поверх работающего Flask

Темы бывшего CSS-спринта. Верстаем уже серверные страницы, не отдельный статический MusicHub. Исходные пакеты остаются в старых папках.

| Код | Ядро | Откуда материал |
| --- | --- | --- |
| A14 | Каскад и CSS-переменные: одна тема на все шаблоны | [A07](lessons/A07-css-cascade-vars/README.md) |
| A15 | Липкая панель плеера | [A08](lessons/A08-flex-header-player/README.md) |
| A16 | Grid и mobile-first каталога | [A09](lessons/A09-grid-mobile-first/README.md) |
| A17 | Типографика карточки | [A10](lessons/A10-typography-visual/README.md) |
| A18 | Анимация и `prefers-reduced-motion` | [A11](lessons/A11-css-animations/README.md) |
| A19 | Showcase интерфейса на 360 и 1200 | [A12](lessons/A12-showcase-musichub/README.md) |

## Спринт 4 · A20–A25 · JavaScript в браузере

Мост с Python короткий: таблица соответствий, не два дня синтаксиса. Продукт — интерактив на уже серверной странице: плеер или короткий раунд.

| Код | Ядро |
| --- | --- |
| A20 | Консоль браузера, `===`, функция |
| A21 | Массив и объект как список карточек |
| A22 | DOM: найти карточку и изменить текст |
| A23 | Событие клика как обработчик |
| A24 | Короткий сценарий: play/pause или раунд на время |
| A25 | Showcase интерактива |

## Спринт 5 · A26–A31 · браузер говорит с Flask без перезагрузки

`session` и любой «логин» — учебные. Вслух: «это не банк». HTML по-прежнему для человека, JSON — для скрипта.

| Код | Ядро |
| --- | --- |
| A26 | `JSON.stringify` / `JSON.parse`, один `localStorage` |
| A27 | Состояние списка в браузере и один `render()` |
| A28 | `jsonify`: `/api/items` отдаёт тот же список, что и шаблон |
| A29 | `fetch` читает `/api/items` |
| A30 | Форма в браузере отправляет JSON, страница не собирается заново целиком |
| A31 | Showcase клиент-серверной связки |

## Спринт 6 · A32–A34 · защита года

A32 склейка маршрутов, API и интерфейса · A33 репетиция · A34 защита перед залом.

Годовой эталон по-прежнему [projects/05-flask-final](projects/05-flask-final/etalon/README.md). Спринт 2 до него не дотягивает JSON API и игру: это спринт 5.
