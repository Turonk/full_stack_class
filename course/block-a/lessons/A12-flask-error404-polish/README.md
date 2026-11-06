# A12 · Кастомная страница 404 и предзащитная сборка

**Точка входа для преподавателя.** Группа ≤10 · 120 мин · планшет + проектор. Спринт 2 · Урок 12.

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

**Артефакт дня:** стилизованная страница `404.html` в дизайне проекта, настроенный `@app.errorhandler(404)`, вызовы `abort(404)` для неизвестных карточек, оформленный `README.md` с командами запуска и прохождение проекта по чек-листу защиты.  
**Один концепт:** ошибка 404 — это штатный ответ сервера («ресурс не найден»), а не поломка программы. Качественное приложение встречает пользователя фирменной страницей ошибки и кнопкой возврата.
