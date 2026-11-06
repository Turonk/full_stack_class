# A11 · Формы и метод POST: добавление данных на сервер

**Точка входа для преподавателя.** Группа ≤10 · 120 мин · планшет + проектор. Спринт 2 · Урок 11.

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

**Артефакт дня:** страница `/suggest` с HTML-формой добавления карточки; сервер обрабатывает `POST`, проверяет поле `title`, добавляет словарь в `ITEMS`, выводит `flash`-сообщение и перенаправляет в каталог без риска повторной отправки при F5.  
**Один концепт:** `GET` запрашивает страницу, `POST` передает данные на сервер. Паттерн Post/Redirect/Get защищает от случайного дублирования данных.
