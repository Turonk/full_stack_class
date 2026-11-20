# A23 · Форма заказа: POST, валидация, flash

**Точка входа для преподавателя.** Группа ≤10 · 120 мин · планшет + проектор. Спринт 5 · Урок 23.

| Поверхность | Ссылка | Экран |
| --- | --- | --- |
| Runbook | [teacher/runbook.md](./teacher/runbook.md) | планшет |
| Lecture | [teacher/lecture.md](./teacher/lecture.md) | речь |
| Slides | [teacher/slides.md](./teacher/slides.md) | проектор |
| Demo | [demo/app.py](./demo/app.py) | проектор |
| Checks | [teacher/checks.md](./teacher/checks.md) | планшет |
| Starter | [student/starter/](./student/starter/) | ученик |
| Task | [student/task.md](./student/task.md) | ученик |
| Solution | [solution/app.py](./solution/app.py) | учитель |
| Homework | [homework.md](./homework.md) | ученик |
| Паспорт | [PLAN.md](./PLAN.md) | справочно |

**Артефакт дня:** форма заказа с полями `name`, `email`, `address`. Валидация: имя не пустое, email содержит `@`. `flash` с подтверждением.  
**Один концепт:** `POST` → валидация → `flash` → `redirect`. Пустая форма не отправляет заказ.
