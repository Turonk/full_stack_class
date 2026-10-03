# A02 Runbook · планшет

Теория вслух: [lecture.md](./lecture.md) ( Hook / Observe — читай оттуда, не из deep-notes).

| Мин | Фаза | Экран | Действие | Крючок сцены |
| --- | --- | --- | --- | --- |
| 0–5 | Retrieval | slides | Padding внутри или снаружи рамки? | Ковёр или улица |
| 5–15 | Hook | slides | Коробка: товар / плёнка / картон / щель | «Я написал 300, а шире» |
| 15–35 | I do | demo | Карточка квеста + DevTools Computed | Пончик в Computed |
| 35–55 | We do | demo | Меняем padding, считаем ширину вслух | Хор: 300+40+4=344 |
| 55–60 | **Checkpoint** | checks | 300 content-box → ? ; border-box → 300 | 344 vs 300 |
| 60–65 | Пауза | — | | |
| 65–100 | You do | student | Карточка трека Pulse FM | Текст не липнет к краю |
| 100–110 | Gallery | student | «Воздух есть / нет» | Воздух в карточке |
| 110–120 | Exit | slides | термин box model + скрин карточки | Скрин + термин |

## Якоря
- content-box: width = только content → итого 300+pad+border.
- border-box: width включает padding+border.
- На курсе по умолчанию: `* { box-sizing: border-box; }`

## Стоп-кран
Не считают 344 → доска: 300 + 20+20 padding + 2+2 border = 344. Потом снова check.

