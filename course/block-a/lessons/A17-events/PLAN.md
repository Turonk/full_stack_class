# Урок 17 · События: click и клавиатура

Паспорт. Проект: [Interactive Hub](../../projects/04-interactive-hub/PROJECT.md). После [DOM](../A16-dom/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: `addEventListener` — «ухо» браузера. Слушает клики и нажатия клавиш.

## Результат

Площадки реагируют на клик: `addEventListener("click", ...)` вызывает `addScore(1)`. Клавиши A/S/D/F тоже работают: `addEventListener("keydown", ...)` проверяет `event.key`. Мини-quiz работает.

**Связь с A16:** площадки созданы, теперь они реагируют на действия.

## Не входит

`localStorage` (A18), `fetch` (A19). Только события и счёт.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | `querySelector`, `textContent`, `createElement` |
| 5–20 | Теория | `addEventListener`, `event.target`, `event.key` |
| 20–45 | I do | Стенд: клик → счёт, клавиша → счёт |
| 45–60 | We do | Класс диктует подсветку при клике: `classList.add("is-hit")` |
| 60–65 | Checkpoint | ≥70% класса видят счёт при клике |
| 65–70 | Пауза | |
| 70–100 | You do | Ученик добавляет обработчики на площадки |
| 100–110 | Проверка | Сосед кликает и проверяет счёт |
| 110–120 | Выход | `event.key` — какая клавиша нажата. Мост: завтра — сохранение |

## Теория

### `addEventListener` — слушать события

```javascript
const btn = document.querySelector("#pad-a");

btn.addEventListener("click", function() {
    addScore(1);
});
```

### `event.target` — какой элемент нажали

```javascript
btn.addEventListener("click", function(event) {
    console.log("Нажали:", event.target.textContent);
    addScore(1);
});
```

### `keydown` — нажатие клавиши

```javascript
document.addEventListener("keydown", function(event) {
    console.log("Клавиша:", event.key);
    if (event.key === "a" || event.key === "A") {
        addScore(1);
    }
});
```

### Подсветка при клике

```javascript
btn.addEventListener("click", function() {
    btn.classList.add("is-hit");
    setTimeout(() => btn.classList.remove("is-hit"), 300);
    addScore(1);
});
```

### CSS для подсветки

```css
.pad.is-hit {
    background-color: var(--color-accent);
    transform: scale(1.1);
}
```

## Live-coding на стенде

```javascript
// static/js/game.js
const pads = document.querySelectorAll(".pad");

pads.forEach(function(pad) {
    pad.addEventListener("click", function() {
        pad.classList.add("is-hit");
        setTimeout(() => pad.classList.remove("is-hit"), 300);
        addScore(1);
    });
});

document.addEventListener("keydown", function(event) {
    const key = event.key.toLowerCase();
    const padMap = { a: "pad-a", s: "pad-s", d: "pad-d", f: "pad-f" };
    const pad = document.querySelector("#" + padMap[key]);
    if (pad) {
        pad.classList.add("is-hit");
        setTimeout(() => pad.classList.remove("is-hit"), 300);
        addScore(1);
    }
});
```

## Практика ученика

1. Найти все площадки: `document.querySelectorAll(".pad")`.
2. Для каждой добавить `addEventListener("click", ...)`.
3. При клике: подсветка + `addScore(1)`.
4. Добавить `addEventListener("keydown", ...)` для A/S/D/F.
5. Проверить: клик мышью и нажатие клавиш увеличивают счёт.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| Слушатель внутри другого слушателя | Двойной счёт — вынести `addEventListener` наружу |
| `keyCode` не работает | Устарел, используй `event.key` |
| Клавиша не срабатывает | `event.key` возвращает `'a'` или `'A'` — проверяй регистр |
| Подсветка не исчезает | Забыл `setTimeout` или неверное время |
| `forEach` не работает на `NodeList` | Используй `document.querySelectorAll` — он возвращает NodeList |

## Домашка · 45–70 мин

Дополнить `game.js`:
- Добавить функцию `resetScore()` — обнуляет счёт и убирает подсветку.
- Добавить кнопку «Рестарт» на страницу.
- Прислать скрин: клик → счёт обновился.

## Мост к A18

Сегодня счёт живёт на странице, но пропадает при обновлении. Завтра — `localStorage`: результат сохранится.
