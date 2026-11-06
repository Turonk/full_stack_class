# Урок 7 · Клиент и сервер: как браузер получает страницу

**Точка входа для преподавателя.** Группа ≤10 · 120 мин · планшет + проектор. Урок 7 спринта 2. Папка исторически называется A06b и не переименовывалась.

| Поверхность | Ссылка | Экран |
| --- | --- | --- |
| Runbook | [teacher/runbook.md](./teacher/runbook.md) | планшет |
| Lecture | [teacher/lecture.md](./teacher/lecture.md) | речь / планшет |
| Slides | [teacher/slides.md](./teacher/slides.md) | проектор |
| Презентация | [teacher/A06b-кто-отвечает-браузеру.pptx](./teacher/A06b-кто-отвечает-браузеру.pptx) | проектор |
| Demo | [demo/app.py](./demo/app.py) | проектор |
| Checks | [teacher/checks.md](./teacher/checks.md) | планшет |
| Starter | [student/starter/](./student/starter/) | ученик |
| Task | [student/task.md](./student/task.md) | ученик |
| Homework | [homework.md](./homework.md) | ученик |
| Solution | [solution/](./solution/) | только учитель |
| Deep notes | [teacher/deep-notes.md](./teacher/deep-notes.md) | дома |

**Артефакт дня:** локальный сервер Flask с тремя маршрутами. `/` и `/radio` работают на стенде, обработчик `/about` ученик реализует самостоятельно.  
**Один концепт:** браузер отправляет HTTP-запрос; Flask по маршруту выбирает функцию-обработчик; её `return` становится телом ответа; браузер рендерит полученный HTML.

Pulse FM в `templates/` сегодня не переносим. Frontend — клиентская часть в браузере, backend — серверная часть на Python/Flask; граница между ними проходит по HTTP.

## Дальше

- Следующее занятие — урок 8, шаблоны и статика: [план](../A08-flask-templates-static/PLAN.md). Свой Pulse FM переезжает на `127.0.0.1:5000`.
- Замыкающий проект спринта: [хаб 2.0](../../projects/01b-flask-hub/PROJECT.md). Каскад CSS уходит в спринт 3 и на этом шаге не открывается.
