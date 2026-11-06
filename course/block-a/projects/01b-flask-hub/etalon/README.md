# Pulse FM 2.0 · Server Edition (Эталон Спринта 2)

Серверное веб-приложение на Flask: шаблоны Jinja, статика, динамические маршруты, добавление карточек через форму POST и страница 404.

## Быстрый запуск

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m flask --app app run --debug
```

Открыть в браузере: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Маршруты приложения

- `GET /` — Главная страница: герой-баннер и топ-3 трека из Python.
- `GET /catalog` — Полный каталог всех карточек (цикл `{% for %}`).
- `GET /item/<item_id>` — Детальная страница карточки по её `id`.
- `GET /about` — Страница об авторе и станции.
- `GET /suggest` — Форма добавления новой карточки.
- `POST /suggest` — Валидация, сохранение в `ITEMS`, `flash` и `redirect` на `/catalog`.
- Любой неизвестный адрес — фирменная страница `404.html`.
