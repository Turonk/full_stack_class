# A10 · Каркас и страница карточки

**Точка входа для преподавателя.** Группа ≤10 · 120 мин · планшет + проектор. Спринт 2 · Урок 10.

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

**Артефакт дня:** многостраничный сайт с общей шапкой через `base.html` и динамической детальной страницей карточки по адресу `/item/<item_id>`.  
**Один концепт:** каркас страницы описывается один раз в `base.html` и наследуется через `extends`; динамический параметр в `@app.route("/item/<item_id>")` позволяет одной функцией отображать любую карточку.
