# Урок 15 · JS-база: переменные, функции, мост с Python

Паспорт. Проект: [Interactive Hub](../../projects/04-interactive-hub/PROJECT.md). После [Showcase Hub](../A14-showcase-hub/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: JS — не новый язык, а тот же Python в другой обёртке. `let` = `var`, `function` = `def`, `console.log` = `print`.

## Результат

Ученик открывает DevTools Console и видит: `let score = 0`, `function addScore(n) { score += n; console.log(score); }`, вызов `addScore(5)` → `5`. На странице — пустой `<span id="score">0</span>`, который JS может обновить.

**Связь с A14:** ученик открывает **свой же** `app.py` из Спринта 3. Не новый проект — добавляет `static/js/game.js`, подключает `<script defer src="{{ url_for('static', filename='js/game.js') }}">`.

## Не входит

DOM-манипуляции (A16), события (A17), `localStorage` (A18). Только консоль и функции.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | Что делает `render_template`, где лежит `static/` |
| 5–15 | Hook + Теория | Таблица Python → JS. `let` vs `const`, функции, `console.log` |
| 15–35 | I do | Стенд: `game.js`, `let score = 0`, `function addScore(n)`, вызов |
| 35–55 | We do | Класс диктует `let lives = 3`, `function loseLife()` |
| 55–60 | Checkpoint | ≥70% класса видят `5` в консоли |
| 60–65 | Пауза | |
| 65–100 | You do | Ученик пишет `game.js` для своего Hub: счёт, жизни, функции |
| 100–110 | Peer | Сосед открывает Console и проверяет |
| 110–120 | Exit ticket | `const` нельзя переназначить. Мост: завтра — DOM |

## Теория

### Таблица Python → JS

| Python | JavaScript | Примечание |
| --- | --- | --- |
| `var x = 5` | `let x = 5` | `let` — можно менять |
| `x = 5` (глоб.) | `const x = 5` | `const` — нельзя переназначить |
| `def add(a, b):` | `function add(a, b) {` | Фигурные скобки, не отступы |
| `print(x)` | `console.log(x)` | DevTools → Console |
| `if x > 0:` | `if (x > 0) {` | Скобки обязательны |
| `x += 1` | `x += 1` | Одинаково |
| `x == y` | `x === y` | Строгое сравнение в JS |

### `let` и `const`

```javascript
let score = 0;       // можно: score = 10;
const MAX_LIVES = 3; // нельзя: MAX_LIVES = 5; → ошибка
```

### Функция

```javascript
function addScore(n) {
    score += n;
    console.log(score);
}

addScore(5);  // → 5
addScore(3);  // → 8
```

### Подключение скрипта

В `base.html` или `game.html`:

```html
<script defer src="{{ url_for('static', filename='js/game.js') }}"></script>
```

`defer` — скрипт выполняется после загрузки DOM. Без `defer` — скрипт может не найти элементы.

## Live-coding на стенде

```javascript
// static/js/game.js
let score = 0;
let lives = 3;

function addScore(n) {
    score += n;
    console.log("Счёт:", score);
}

function loseLife() {
    lives -= 1;
    console.log("Жизни:", lives);
}

addScore(5);
loseLife();
addScore(3);
```

Открыть DevTools → Console. Видим:
```
Счёт: 5
Жизни: 2
Счёт: 8
```

## Практика ученика

1. В своём Hub-проекте создать `static/js/game.js`.
2. Подключить `<script defer>` в `game.html` (или `base.html`).
3. Написать: `let score = 0`, `let lives = 3`.
4. Написать функцию `addScore(n)` — прибавляет счёт.
5. Написать функцию `loseLife()` — отнимает жизнь.
6. Вызвать `addScore(5)`, `loseLife()`, `addScore(3)` — проверить в Console.
7. В `game.html` добавить `<span id="score-display">0</span>` — пока статический.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| В консоли `ReferenceError: score is not defined` | `let score` объявлен внутри функции, а не глобально |
| Скрипт не работает, `null` | Нет `defer`, скрипт выполняется до загрузки DOM |
| `Uncaught SyntaxError` | Забыл фигурную скобку `}` или точку с запятой (не критично, но лучше ставить) |
| `const` не меняется | Использовал `const` для переменной, которую нужно менять |
| `console.log` не видит | Не открыл DevTools → Console |

## Домашка · 45–70 мин

Дополнить `game.js`:
- Добавить функцию `resetGame()` — обнуляет `score` и `lives`.
- Добавить функцию `checkGameOver()` — если `lives === 0`, выводит `'Game over'`.
- Вызвать все функции и проверить в Console.
- Прислать скрин Console с результатами.

## Мост к A16

Сегодня счёт живёт только в Console. Завтра ученик выведет его на страницу: `document.querySelector("#score-display").textContent = score`.
