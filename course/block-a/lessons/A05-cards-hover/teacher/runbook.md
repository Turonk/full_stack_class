# A05 Runbook · планшет

Теория вслух: [lecture.md](./lecture.md).  
Живой пример: [demo/](../demo/). Шаги набора кода — в lecture (блоки 1–3), не в deep-notes.

| Мин | Фаза | Экран | Действие | Крючок сцены |
| --- | --- | --- | --- | --- |
| 0–5 | Retrieval | slides | Зачем space-between в шапке вчера? | Вчерашняя шапка |
| 5–15 | Hook + Predict | slides + lecture | Карточка без отклика; предикт: что увидит человек с Tab | «Трек без реакции» |
| 15–35 | I do | demo | lecture блоки 1–2: wrap + gap, потом hover + focus-within | Карточка отвечает |
| 35–50 | We do | demo | lecture блок 3: transition all vs только свойства; прогон Tab | ~0,2 с, не all |
| 50–55 | **Факт IT** | caniuse | lecture «Факт из мира IT»: :focus-visible, WCAG 2.4.7 | caniuse + Tab на стенде |
| 55–60 | **Checkpoint** | checks | Tab по карточкам + ширина 360px | Tab + нет скролла вбок |
| 60–65 | Пауза | — | Вода, разминка | |
| 65–100 | You do | student | [task.md](../student/task.md): три трека с откликом | Витрина к эфиру |
| 100–110 | Gallery | student | 3 витрины на проектор | Hover + Tab + 360px |
| 110–120 | Exit + bridge | slides | термин transition + скрин витрины | Скрин витрины |

## Реплики-якоря

- «Мышь и Tab оба видят отклик: `:hover` + `:focus-within` на карточке, ссылка внутри.»
- «`transition: all` — перечисляй свойства ~0,2 с.»
- «`wrap` — не влезло, перенеси на новую строку.»
- «Скролл страницы вбок хуже, чем перенос карточки.»

## Стоп-кран

Tab не даёт отклика → на demo: внутри карточки ссылка Play (чтобы `:focus-within` сработал), правило `.tile:hover, .tile:focus-within`, повторить check. Не ставить `:focus-visible` на сам `article`.

## Отстаёт / Опережает

- **Отстаёт:** only hover + одна карточка-пример отклика (шаги 1–3 task.md). wrap и 360px — проверить на дом.
- **Опережает:** `flex: 1 1 200px` на карточках; `transform: scale(1.04)` на кнопке с reduced-motion; скрин 360px в чат.
