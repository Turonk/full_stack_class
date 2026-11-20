# Урок 16 · DOM: найти, изменить, создать элемент

Паспорт. Проект: [Interactive Hub](../../projects/04-interactive-hub/PROJECT.md). После [JS-база](../A15-js-basics/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: DOM — это дерево HTML-элементов. JS находит узлы через `querySelector` и меняет их.

## Результат

На странице `/game` — `<span id="score">0</span>`. JS обновляет его: `document.querySelector("#score").textContent = score`. Ученик создаёт 4 кнопки-площадки из массива `['A','S','D','F']` через `createElement` и `append`.

**Связь с A15:** сегодня счёт переезжает из Console на страницу. Завтра площадки будут реагировать на клик.

## Не входит

События (A17), `localStorage` (A18). Только найти и изменить.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | Что делает `let`, `function`, `console.log` |
| 5–20 | Теория | DOM-дерево, `querySelector`, `textContent`, `createElement`, `append` |
| 20–45 | I do | Стенд: `querySelector("#score")`, меняем текст, создаём кнопку |
| 45–60 | We do | Класс диктует массив площадок, цикл создаёт кнопки |
| 60–65 | Checkpoint | ≥70% класса видят счёт на странице |
| 65–70 | Пауза | |
| 70–100 | You do | Ученик выводит счёт на страницу, создаёт кнопки-площадки |
| 100–110 | Проверка | Сосед обновляет `score` и смотрит, изменился ли текст |
| 110–120 | Выход | `querySelector` ищет по ID, классу, тегу. Мост: завтра — клик |

## Теория

### `querySelector` — найти элемент

```javascript
// По ID
const scoreEl = document.querySelector("#score");

// По классу
const button = document.querySelector(".pad");

// По тегу
const firstCard = document.querySelector("article");
```

### `textContent` — изменить текст

```javascript
let score = 8;
document.querySelector("#score").textContent = score;
// На странице: <span id="score">8</span>
```

### `createElement` + `append` — создать элемент

```javascript
const button = document.createElement("button");
button.textContent = "A";
button.className = "pad";
document.querySelector("#pads").append(button);
```

### Цикл создаёт кнопки из массива

```javascript
const pads = ["A", "S", "D", "F"];

for (let i = 0; i < pads.length; i++) {
    const btn = document.createElement("button");
    btn.textContent = pads[i];
    btn.className = "pad";
    document.querySelector("#pads").append(btn);
}
```

## Live-coding на стенде

```javascript
// static/js/game.js
let score = 8;

// 1. Найти элемент
const scoreEl = document.querySelector("#score");

// 2. Изменить текст
scoreEl.textContent = score;

// 3. Создать кнопки
const pads = ["A", "S", "D", "F"];
const container = document.querySelector("#pads");

for (let i = 0; i < pads.length; i++) {
    const btn = document.createElement("button");
    btn.textContent = pads[i];
    btn.className = "pad";
    container.append(btn);
}
```

HTML:
```html
<span id="score">0</span>
<div id="pads"></div>
```

Результат на странице:
- Счёт: `8`
- 4 кнопки: A, S, D, F

## Практика ученика

1. В `game.html` добавить `<span id="score">0</span>` и `<div id="pads"></div>`.
2. В `game.js` найти `#score`: `document.querySelector("#score")`.
3. Изменить текст: `.textContent = score`.
4. Создать 4 кнопки из массива `['A','S','D','F']`.
5. Добавить кнопки в `#pads`.
6. Проверить: при изменении `score` на странице текст обновляется.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| `null` в консоли, дальше не идёт | `querySelector` не нашёл элемент — проверь ID в HTML |
| Скрипт выполняется до загрузки DOM | Нет `defer` в `<script defer>` |
| Кнопки не появляются | Забыл `.append(btn)` или указал неверный контейнер |
| `textContent` не работает | Переменная не объявлена через `let`, а через `const` и меняется |
| innerHTML vs textContent | Не вставляй сырой HTML от пользователя — используй `textContent` |

## Домашка · 45–70 мин

Дополнить `game.js`:
- Добавить функцию `updateScore(newScore)` — обновляет `#score`.
- Добавить функцию `createPads(padsArray)` — создаёт кнопки из массива.
- Вызвать обе функции.
- Прислать скрин страницы с кнопками и счётом.

## Мост к A17

Сегодня площадки созданы, но на них нельзя нажать. Завтра — `addEventListener("click", ...)` и `keydown`.
