# A19 · /api/items + fetch: браузер говорит с Flask

**Точка входа для преподавателя.** Группа ≤10 · 120 мин · планшет + проектор. Спринт 4 · Урок 19.

| Поверхность | Ссылка | Экран |
| --- | --- | --- |
| Runbook (тайминг) | [teacher/runbook.md](./teacher/runbook.md) | планшет |
| Lecture (речь) | [teacher/lecture.md](./teacher/lecture.md) | речь / планшет |
| Slides (проектор) | [teacher/slides.md](./teacher/slides.md) | проектор |
| Demo стенда | [demo/app.py](./demo/app.py) | проектор |
| Checks (контроль) | [teacher/checks.md](./teacher/checks.md) | планшет |
| Starter ученика | [student/starter/](./student/starter/) | ученик |
| Task (задача) | [student/task.md](./student/task.md) | ученик |
| Solution (эталон) | [solution/app.py](./solution/app.py) | только учитель |
| Homework | [homework.md](./homework.md) | ученик |
| Паспорт урока | [PLAN.md](./PLAN.md) | справочно |

**Артефакт дня:** каталог карточек загружается через `fetch("/api/items")` — без `{% for %}`, через JavaScript.  
**Один концепт:** сервер отдаёт JSON, браузер рисует карточки. Данные живут в Python, но отображаются через JS.
