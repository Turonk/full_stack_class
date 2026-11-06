# A09 · Данные в Python и циклы Jinja

**Точка входа для преподавателя.** Группа ≤10 · 120 мин · планшет + проектор. Спринт 2 · Урок 9.

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

**Артефакт дня:** в `app.py` оформлен список словарей `ITEMS` (минимум 6 авторских карточек); в шаблоне каталога удалена копипаста `<article>` и заменена на **один** цикл `{% for item in items %}`.  
**Один концепт:** данные отделены от верстки. Данные живут в структурах Python, а шаблон Jinja описывает только правила их отрисовки.
