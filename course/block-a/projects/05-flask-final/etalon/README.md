# MediaGameHub v1 · эталон финала блока A

Учебный портал: Jinja-шаблоны + CSS/JS + простой Flask.

## Запуск

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --debug
```

Открой http://127.0.0.1:5000

## Что смотреть на защите

- `/` тянет хиты ещё и через `/api/hits`
- `/music` — цикл Jinja
- `/game` — PulseBeat JS
- `/shop` — список из Python
- `/contact` — POST + flash
- любой кривой URL — брендовый 404
