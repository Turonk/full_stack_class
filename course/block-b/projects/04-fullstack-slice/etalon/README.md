# Fullstack-срез MediaGameHub v2

Склеиваем:

1. Витрину из `block-a/projects/05-flask-final/etalon` (HTML-страницы можно постепенно заменить на Vite).
2. API из `block-b/projects/03-pulse-api/etalon`.
3. Игру PulseBeat: после game over `POST /api/scores`.
4. Кабинет: `GET /api/cabinet` только после login pin 1234.

## Запуск двух процессов

Терминал 1: Flask API на 5000  
Терминал 2: `npx vite` на 5173 с proxy `/api`

Минимальный `vite.config.js`:

```js
export default {
  server: { proxy: { "/api": "http://127.0.0.1:5000" } }
};
```
