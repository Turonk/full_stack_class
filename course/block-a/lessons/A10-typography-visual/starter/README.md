# A10 · Стартер: приращение к коду A09

Отдельных файлов нет — ученик продолжает **свой** MusicHub после A07–A09 (тема, плеер, сетка работают).

## Что добавить

Код-блоки стартера и эталона — в [`../teacher/lecture.md`](../teacher/lecture.md) (§8 «Делаешь сам»):

1. Три строки подключения шрифтов в `head` (Syne + IBM Plex Sans).
2. Роли: `h1, h2, h3, .logo` — Syne; `body` — IBM Plex Sans.
3. Шкала: h1 2.4rem · h2 1.6rem · body 1rem · .muted 0.9rem; hero — `clamp(1.8rem, 5vw, 2.4rem)`.
4. `body { line-height: 1.5 }`.
5. Токены: `--radius: 20px` в `:root`; карточки — `border-radius: var(--radius)` + тень.

Критерий «готово» — там же.
