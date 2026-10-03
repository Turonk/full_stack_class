# Блок A · детальный учебный план

34 урока × 120 мин. Продукт года: MediaGameHub v1 на Flask-шаблонах.

## Спринт 1 · два контура

- **PulseDeck** — стенд лектора: теория, схемы, пример вместе. Папка `projects/00-pulsedeck/`.
- **Pulse FM** — проект ученика к родителям на A06. Не копировать тексты лаунчера.

Тайминг (teacher-first): см. [`../teacher/RHYTHM.md`](../teacher/RHYTHM.md). Пакет урока: hub `README.md` → runbook / slides / demo / student / checks. Sprint 1 пакеты готовы.

| Код | Хук для зала | Ядро | Must-have к концу | Hub |
| --- | --- | --- | --- | --- |
| A01 | F12 в Discord / Steam | Каркас + CSS-файл с первой минуты | Тёмный баннер, слоган, кнопка | [README](lessons/A01-first-screen-style/README.md) |
| A02 | Коробка vs товар внутри | Box model, border-box | Карточка с padding и radius | [README](lessons/A02-box-model/README.md) |
| A03 | Почему обложки Spotify квадратные | Fonts, object-fit, alt | Обложка не сплющена | [README](lessons/A03-type-fonts-media/README.md) |
| A04 | Шапка Discord: лого слева | Flex, gap, space-between | Шапка в один ряд | [README](lessons/A04-flex-header/README.md) |
| A05 | Карточка «подпрыгивает» | wrap, hover, focus, transition | 3 карточки + отклик | [README](lessons/A05-cards-hover/README.md) |
| A06 | Родители в зале | Showcase ≤6 мин × ученик | Чек-лист Pulse FM | [README](lessons/A06-showcase-pulse-fm/README.md) |

Аналогии спринта: HTML = скелет, CSS = скин, браузер = движок.

## Спринт 2 · MusicHub · cascade → player → grid+mobile

Критерии: [`../teacher/CURRICULUM-GATES.md`](../teacher/CURRICULUM-GATES.md).

| Код | Ядро | Зачем подростку |
| --- | --- | --- |
| A07 | Cascade + CSS variables | Один источник цвета темы |
| A08 | Flex-плеер | Панель как у настоящего плеера |
| A09 | Grid **и** mobile-first; position только sticky/absolute точечно | Витрина без четырёх моделей position за раз |
| A10 | Типографика каталога | Читаемость > «красивый шрифт» |
| A11 | keyframes + reduced-motion | Вау без укачивания |
| A12 | Showcase MusicHub | Демо 360 и 1200 |

## Спринт 3 · Мост Python → JS

Правило: таблица Python→JS, не два дня синтаксиса. Быстрее DOM (A15) и события (A16).

| Код | Мост | Продукт |
| --- | --- | --- |
| A13 | REPL → Console, `===` vs `==` | Счёт в консоли |
| A14 | list/dict/def кратко | Данные пэдов |
| A15 | «сцена игры» = DOM | Счёт на экране |
| A16 | обработчик как callback | Вспышка пэда |
| A17 | игровой цикл упрощённо | Раунд ~30с |
| A18 | Showcase PulseBeat | Живая игра |

## Спринт 4 · Данные и магазин

Порядок: формы → state+render+storage → корзина → fetch (после Live Server) → glue → showcase.

| Код | Ядро |
| --- | --- |
| A19 | Валидация форм на клиенте |
| A20 | JSON + localStorage + один `render()` |
| A21 | Состояние корзины |
| A22 | fetch = «сходи на склад» |
| A23 | Склейка навигации магазина |
| A24 | Showcase покупки |

## Спринт 5 · Flask

Session и любой «логин» — **учебные**. Вслух: «это не банк».

| Код | Ядро |
| --- | --- |
| A25 | Браузер — клиент, Flask — официант с меню-роутами |
| A26 | Несколько страниц = несколько функций |
| A27 | Jinja = f-string на стероидах + наследование |
| A28 | static — шкаф с css/js, url_for — не забыть путь |
| A29 | POST не светит пароль в URL |
| A30 | HTML для людей, JSON для скриптов |

## Спринт 6 · Защита

A31 склейка · A32 404 и README · A33 репетиция · A34 защита перед залом.
