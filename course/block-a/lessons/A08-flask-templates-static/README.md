# A08 · Шаблоны и статика: переезд сайта на сервер

**Точка входа для преподавателя.** Группа ≤10 · 120 мин · планшет + проектор. Спринт 2 · Урок 8.

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
| Deep notes | [teacher/deep-notes.md](./teacher/deep-notes.md) | дома |
| Homework | [homework.md](./homework.md) | ученик |
| Паспорт урока | [PLAN.md](./PLAN.md) | справочно |

**Артефакт дня:** сайт ученика из Спринта 1 открывается локально по `http://127.0.0.1:5000/` с подгрузкой `styles.css` и картинок через сервер Flask.  
**Один концепт:** HTML живёт в `templates/` и отдаётся через `render_template()`; ассеты живут в `static/` и связываются через `url_for('static', filename=...)`. Прямой доступ по `file://` закрыт.
