# Аудит сетки PulseLab · 2 × 34

Дата: 2026-10-02. Объект: вся программа блоков A и B. Цель — teacher-first доставка для групп до 10.

## Сильные стороны (сохраняем)

- Спираль продуктов: Pulse FM → MusicHub → PulseBeat → MerchShop → Flask → MediaGameHub.
- Ранний CSS (A01) и Zero Ugly Screens — визуальный результат с первого дня.
- Showcase каждые шесть уроков даёт ритм публичности.
- Dual-track Sprint 1: PulseDeck (стенд) + Pulse FM (личный проект) — правильная модель PRIMM.
- PROGRAM.md уже фиксирует retrieval, checkpoint mid, exit ticket.

## Главный разрыв

Материалы написаны как **сценарий для автора**, не как **пульт для преподавателя на планшете**:

| Симптом | Где | Риск на уроке |
| --- | --- | --- |
| Монолитный `teacher.md` 200+ строк | A01–A06 | Прокрутка, потеря тайминга |
| Нет единой точки входа урока | все уроки | >15 сек на поиск ресурса |
| Нет `slides.md` для проектора | Sprint 1 | На экран попадает документация |
| Checkpoint без «что делать, если неверно» | частично | Класс уходит в You do неготовым |
| A07–A34 / B01–B34 без пакетов | блоки A/B | Только curriculum-таблицы |

## Карта зависимостей (сжато)

```text
A01 HTML+link CSS ──► A02 box ──► A03 type/media ──► A04 flex ──► A05 states ──► A06 show
         │                │              │               │            │
         └─ Pulse FM banner / card / cover / header / shelf ──────────┘
A07 vars ──► A08 player flex ──► A09 grid+mobile ──► A10 type ──► A11 motion ──► A12 MusicHub
A13 JS map ──► A14 loops ──► A15 DOM ──► A16 events ──► A17 loop ──► A18 PulseBeat
A19 forms ──► A20 storage ──► A21 cart ──► A22 fetch ──► A23 glue ──► A24 MerchShop
A25–A34 Flask assemble → polish → defense
B01–B06 studio → B07–B12 client truth → B13–B18 API → B19–B24 glue → B25–B31 python → B32–B34 diploma
```

### Когнитивная нагрузка по спринтам

| Спринт | Оценка | Проблема | Решение аудита |
| --- | --- | --- | --- |
| A S1 | высокая по доставке, норма по контенту | толстый teacher.md | пакеты runbook/slides/checks |
| A S2 | средняя | A09: grid + mobile + position сразу | mobile-first с grid; position только sticky/absolute на плеере |
| A S3 | риск «скучно» | A13–A14 синтаксис JS после Python | Python→JS таблица, быстрее DOM |
| A S4 | высокая | cart + storage + fetch рядом | сначала state+render, fetch после Live Server |
| A S5–6 | средняя | Flask кажется «продакшеном» | маркировать session учебной |
| B S1 | setup-риск | Vite/Git без чек-листа | setup-checklist в teacher shell |
| B S3 | misconception | session = банк | явная реплика «это не банк» |
| B S6 | ок | — | оставить рубрику диплома |

## Артефакты и showcase

| Урок | Артефакт «покажи экран» | Showcase? |
| --- | --- | --- |
| A01 | баннер Pulse FM | нет |
| A02 | карточка трека | нет |
| A03 | обложка + иерархия | нет |
| A04 | header радио | нет |
| A05 | витрина 3 трека | нет |
| A06 | Pulse FM v1 | **да** · ≤10 × 6 мин |
| A12 | MusicHub | да |
| A18 | PulseBeat | да |
| A24 | MerchShop | да |
| A34 | защита A | да |
| B06 / B12 / B18 / B24 | UI-kit / catalog / API / fullstack | да |
| B33 | диплом | да |

## Пробелы assessment loop

- Есть идея peer-feedback на A06, нет единого шаблона для всех showcase.
- Нет единой карточки диагностики на 5 мин (retrieval) с ответами учителя.
- Нет маршрута «отстающий / быстрый» в каждом спринте (есть только в STYLE/PROGRAM намёками).

## Политика чистки (исполнение)

1. Сначала пакет + ссылки из README.
2. Проверка quality gate.
3. Удаление только: старый корневой `teacher.md` после переноса в `teacher/runbook.md` + `deep-notes.md`; дубли starter/etalon после переноса в `student/` и `solution/`; сиротские копии без ссылок.
4. Без `legacy/`, `old/`, параллельных деревьев.

## Вердикт

Контент курса готов к преподаванию после **teacher shell + пакеты A01–A06 + ресеквенс критериев A07–B34 + assessment + quality gates**. Дальнейшие пакеты A07+ создаются по тому же контракту `LESSON-PACKET-STANDARD.md`.
