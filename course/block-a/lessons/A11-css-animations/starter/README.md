# A11 · Стартер: приращение к коду A10

Отдельных файлов нет — ученик продолжает **свой** MusicHub после A07–A10 (тема, плеер, сетка, типографика работают).

## Что добавить

Код-блоки стартера и эталона — в [`../teacher/lecture.md`](../teacher/lecture.md) (§8 «Делаешь сам»):

1. `span.live-badge` «В ЭФИРЕ» на обложке хита недели (absolute в углу — `.cover` уже relative из A09).
2. `@keyframes pulse` — круг света расходится и растворяется (0% → 70% → 100%).
3. `animation: pulse 2s infinite` на бейдже.
4. `@media (prefers-reduced-motion: reduce)` — `animation: none` на бейдже, `transition: none` на карточках и кнопках.
5. Ревизия A05: hover карточки, кольцо `:focus-visible`, transition точечный (не `all`).

Критерий «готово» — там же. Правило дня: **одна анимация на экран**.
