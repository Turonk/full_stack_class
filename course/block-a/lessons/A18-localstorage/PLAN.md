# Урок 18 · localStorage: сохранить состояние

Паспорт. Проект: [Interactive Hub](../../projects/04-interactive-hub/PROJECT.md). После [События](../A17-events/PLAN.md).

- Группа ≤10 · 120 минут
- Один концепт: `localStorage` — «жёсткий диск» браузера. Данные живут между перезагрузками.

## Результат

После игры: `localStorage.setItem("hub-score", score)`. При загрузке страницы: `let saved = localStorage.getItem("hub-score")` — показать последний результат. Кнопка «Очистить рекорд» удаляет данные.

**Связь с A17:** счёт обновляется при клике, теперь он сохраняется.

## Не входит

`fetch`, `/api/items` (A19). Только localStorage.

## Тайминг

| Мин | Фаза | Действие |
| --- | --- | --- |
| 0–5 | Retrieval | `addEventListener`, `event.key`, `classList` |
| 5–15 | Теория | `setItem`, `getItem`, `removeItem`, `JSON.stringify` |
| 15–40 | I do | Стенд: сохранить счёт, обновить страницу, восстановить |
| 40–55 | We do | Класс диктует кнопку «Очистить рекорд» |
| 55–60 | Checkpoint | ≥70% класса видят счёт после обновления |
| 60–65 | Пауза | |
| 65–100 | You do | Ученик добавляет сохранение/восстановление |
| 100–110 | Проверка | Сосед обновляет страницу и проверяет |
| 110–120 | Выход | `localStorage` хранит только строки. Мост: завтра — сервер |

## Теория

### Основные методы

```javascript
// Сохранить
localStorage.setItem("hub-score", score);

// Прочитать
let saved = localStorage.getItem("hub-score");

// Удалить
localStorage.removeItem("hub-score");
```

### `localStorage` хранит только строки

```javascript
let score = 42;
localStorage.setItem("hub-score", score);  // автоматически в строку

// При чтении — тоже строка:
let saved = localStorage.getItem("hub-score"); // "42", не 42
// Если нужен число:
saved = parseInt(saved, 10);
```

### Для объектов — `JSON.stringify` / `JSON.parse`

```javascript
let cart = [{id: 1, name: "Футболка", price: 1200}];
localStorage.setItem("cart", JSON.stringify(cart));

let loaded = JSON.parse(localStorage.getItem("cart"));
```

### При загрузке страницы

```javascript
let score = 0;
let saved = localStorage.getItem("hub-score");
if (saved) {
    score = parseInt(saved, 10);
}
document.querySelector("#score").textContent = score;
```

## Live-coding на стенде

```javascript
// static/js/game.js
// 1. Сохранить после клика
function addScore(n) {
    score += n;
    localStorage.setItem("hub-score", score);
    document.querySelector("#score").textContent = score;
}

// 2. Восстановить при загрузке
let score = 0;
let saved = localStorage.getItem("hub-score");
if (saved) {
    score = parseInt(saved, 10);
}
document.querySelector("#score").textContent = score;

// 3. Очистить
document.querySelector("#clear").addEventListener("click", function() {
    localStorage.removeItem("hub-score");
    score = 0;
    document.querySelector("#score").textContent = 0;
});
```

## Практика ученика

1. В `addScore` добавить `localStorage.setItem("hub-score", score)`.
2. При загрузке `game.js` проверить `localStorage.getItem("hub-score")`.
3. Если есть сохранённый счёт — показать его на странице.
4. Добавить кнопку «Очистить рекорд» → `removeItem`.
5. Проверить: обновить страницу → счёт на месте.

## Ошибки

| Симптом | Куда смотреть |
| --- | --- |
| `null` при чтении | Ещё не было `setItem` — проверь `if (saved)` |
| Счёт не сохраняется | `setItem` вызывается после изменения, не до |
| `JSON.parse` ломает | Сохранял не объект, а число — используй `parseInt` при чтении |
| Данные не очищаются | Забыл `removeItem` или очистил не тот ключ |
| `localStorage` не работает в `file://` | Открой через `127.0.0.1:5000` |

## Домашка · 45–70 мин

Дополнить `game.js`:
- Добавить функцию `saveScore()` — сохраняет счёт.
- Добавить функцию `loadScore()` — восстанавливает.
- Добавить функцию `clearScore()` — очищает.
- Прислать скрин: счёт после обновления страницы.

## Мост к A19

Сегодня счёт хранится в браузере. Завтра каталог карточек начнёт загружаться с сервера через `fetch("/api/items")`.
