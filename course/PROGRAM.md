# PulseLab · программа 2 × 34

Занятия раз в неделю по 120 минут. Каждые 6 уроков — showcase. Финал блока A — защита портала. Финал блока B — диплом.

Правило курса: **Zero Ugly Screens**. К концу каждого обычного урока на экране уже есть узнаваемый PulseLab-интерфейс, а не белый лист с сырым HTML.

Правило лектора: **Deep Engagement**. Методичка — это сценарий, а не конспект. Реплики, факты индустрии, аналогии с Python и играми, вопросы-ловушки.

Доставка: **teacher-first**. Старт педагога — [`teacher/HOME.md`](teacher/HOME.md). Урок = пакет (`README` → runbook / slides / demo / starter / checks). Ритм, assessment и quality gates — в `course/teacher/`.

## Блок A · MediaGameHub v1

Финал года: Flask + Jinja + свой CSS/JS. Ребята уже знают Python — Flask даём как «знакомый язык в роли сервера», не как второй язык программирования.

### Спринт 1 · A01–A06 · Modern Web и Box Model

Папка: `block-a/lessons/A01-first-screen-style` … `A06-showcase-pulse-fm`.

Два контура: стенд **PulseDeck** (`projects/00-pulsedeck/`) — теория и пример вместе; **Pulse FM** (`projects/01-pulse-fm/`) — радио ученика к родителям.

| Урок | Тип | Вместе на стенде PulseDeck | Своё радио Pulse FM |
| --- | --- | --- | --- |
| A01 | урок | HUD + кнопка Play | Баннер и «Слушать» |
| A02 | урок | Карточка квеста, коробка | Карточка трека |
| A03 | урок | Иконка cover + шрифты | Обложки эфира |
| A04 | урок | Шапка лаунчера flex | Шапка радио |
| A05 | урок | Полка из трёх игр | Три трека, hover |
| A06 | showcase | 5 мин карта приёмов | Защита перед родителями |

Педагогика спринта: CSS с первой минуты. HTML учим как смысл блоков, не как конспект тегов на шесть недель.

### Спринт 2 · A07–A12 · MusicHub · cascade → grid → motion

Вход/выход и риски: [`teacher/CURRICULUM-GATES.md`](teacher/CURRICULUM-GATES.md).

| Урок | Тема | Экран |
| --- | --- | --- |
| A07 | Cascade, specificity, CSS-переменные `:root` | Тема PulseLab без хаоса цветов |
| A08 | Flex-плеер (добор к шапке A04) | Нижняя панель управления |
| A09 | **Grid + mobile-first вместе** (1 кол. → 2+); `position` только sticky/absolute на плеере/бейдже | Витрина + липкий плеер |
| A10 | Типографика каталога, визуальная иерархия | Читаемый MusicHub |
| A11 | `@keyframes` + `prefers-reduced-motion` | Одна анимация без ряби |
| A12 | Showcase MusicHub | Телефон + десктоп |

### Спринт 3 · A13–A18 · JS для тех, кто знает Python · PulseBeat

Не два дня синтаксиса. Таблица **Python → JS** на слайдах; быстрее DOM и события.

| Урок | Тема | Экран |
| --- | --- | --- |
| A13 | Мост Python→JS: `let`/`const`, `===`, консоль как REPL | Счёт в консоли, заготовка |
| A14 | Массивы/объекты на данных треков (коротко) | Список пэдов в данных |
| A15 | DOM: querySelector, textContent, classList | Счёт на странице |
| A16 | click, keydown, event.target | Пэды вспыхивают |
| A17 | Упрощённый game loop | Раунд ~30 секунд |
| A18 | Showcase PulseBeat | Живой раунд на проекторе |

### Спринт 4 · A19–A24 · MerchShop и данные

Порядок: формы → **состояние + `render()` + storage** → корзина → **fetch после** локальных данных и Live Server → склейка → showcase.

| Урок | Тема | Экран |
| --- | --- | --- |
| A19 | Формы и валидация на клиенте | Тёмный checkout-lite |
| A20 | JSON + localStorage + единый `render()` | F5 не убивает состояние |
| A21 | Корзина: qty, сумма, удаление | Живой чек |
| A22 | fetch, async/await, mock JSON | Каталог с «склада» |
| A23 | Навигация и склейка магазина | Сценарий покупки |
| A24 | Showcase MerchShop | Демо + форма |

### Спринт 5 · A25–A30 · Flask с нуля для знающих Python

| Урок | Тема | Экран |
| --- | --- | --- |
| A25 | HTTP, venv, `@app.route` | «PulseLab жив» с localhost:5000 |
| A26 | Несколько роутов | /music /game /shop |
| A27 | Jinja: extends, block, for | Одна шапка на всех страницах |
| A28 | static CSS/JS через url_for | Стили PulseLab на сервере |
| A29 | POST, request.form, flash | Форма «написать нам» |
| A30 | jsonify + fetch | Хиты с `/api/hits` |

### Спринт 6 · A31–A34 · Сборка и защита года

| Урок | Тема |
| --- | --- |
| A31 | Склейка портала: шаблоны + игра + магазин |
| A32 | 404, адаптив, README на 3 команды |
| A33 | Репетиция 5-минутной защиты |
| A34 | Защита финала A |

## Блок B · MediaGameHub v2 · fullstack

Берём финал A и растим инженерию: модули, API-контракт, сессия, тесты, диплом.

### Спринт 1 · B01–B06 · Studio / UI-кит

| Урок | Тема | Экран |
| --- | --- | --- |
| B01 | Git, ветки, GitHub Pages | Публичная ссылка на статику |
| B02 | Vite, `import`/`export` | localhost:5173, кнопка из модуля |
| B03 | Компонент = функция + данные | Card, Nav, Badge без React |
| B04 | CSS motion + Element.animate | Ripple, появление карточки |
| B05 | a11y: focus-visible, aria, контраст | Весь кит на Tab |
| B06 | Showcase UI-кита | Галерея компонентов + Pages |

### Спринт 2 · B07–B12 · Клиент API

| Урок | Тема |
| --- | --- |
| B07 | async/await, try/catch, retry, DevTools offline |
| B08 | REST-контракт, api.md, статусы 200/400/404 |
| B09 | Список и деталь из JSON |
| B10 | Состояния loading / empty / error |
| B11 | Поиск и фильтр на клиенте |
| B12 | Showcase каталога |

### Спринт 3 · B13–B18 · PulseAPI

| Урок | Тема |
| --- | --- |
| B13 | Flask как API, `/api/health` |
| B14 | GET списка и `/api/tracks/<id>` |
| B15 | POST скора, 201 и 400 |
| B16 | session-лайт, `/api/me` (учебный pin, не прод-безопасность) |
| B17 | CORS vs Vite proxy, два процесса |
| B18 | Showcase: фронт бьёт свой API |

### Спринт 4 · B19–B24 · Fullstack-срез

| Урок | Тема |
| --- | --- |
| B19 | Лидерборд: сортировка в Python, таблица на фронте |
| B20 | Логин-лайт, нав гостя vs пользователя |
| B21 | Защищённый `/api/cabinet`, 401 |
| B22 | Валидация только на сервере недопустима — и только на клиенте тоже. Оба слоя |
| B23 | Pages для фронта, README бэка, `.env.example` |
| B24 | Showcase fullstack-среза |

### Спринт 5 · B25–B31 · Python-bridge и полировка

| Урок | Тема |
| --- | --- |
| B25 | Логика в `functions.py` без Flask-импортов |
| B26 | JSON-файлы, pathlib, utf-8 |
| B27 | Алгоритм top-3, ничьи |
| B28 | pytest + test_client: health, 404, bad POST |
| B29 | UX-полировка диплома, 360px |
| B30 | README + видео 60 сек |
| B31 | Черновая защита |

### Спринт 6 · B32–B34 · Диплом

| Урок | Тема |
| --- | --- |
| B32 | Чек-лист и холодный старт машины |
| B33 | Защита 5–7 мин |
| B34 | Рефлексия и портфолио |

## Как читать методичку

Пакет урока: `README.md` → на планшете `teacher/runbook.md`, подробности в `teacher/deep-notes.md`.  
`deep-notes` обязан содержать блоки Deep Engagement из `templates/lesson.md`: хук, инсайт, аналогия, ловушка, live-coding вслух, ошибки возраста, челлендж.  
На проектор — только `slides.md` или `demo/`.
