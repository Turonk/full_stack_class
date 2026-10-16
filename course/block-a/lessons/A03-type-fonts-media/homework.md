# Домашка A03 · 45–60 минут

Доведи обложку и добавь радио «свой голос» шрифтами PulseLab.

## Сделай

1. Подключи шрифты PulseLab в `head` своего `index.html` (как на PulseDeck):
   ```html
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
   <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&family=Syne:wght@700&display=swap" rel="stylesheet">
   ```
2. В CSS: заголовкам — `Syne`, остальному тексту — `"IBM Plex Sans", sans-serif`.
3. Убедись, что обложка — настоящая картинка с `object-fit: cover` и осмысленным `alt`.
4. Проверь иерархию: название трека крупнее подписи, подпись приглушена цветом.

## Критерии приёмки

- [ ] Два семейства подключены, заголовки ≠ текст по «голосу»
- [ ] Обложка не «жвачка» (cover + квадрат)
- [ ] alt осмысленный
- [ ] Баннер, карточка и шапка с прошлых уроков живы
- [ ] Работает без интернета не ломаясь (шрифты отвалятся — останется fallback)

## Сдать

Скрин карточки + `index.html` + `styles.css`.

## Если не получилось

- Шрифты не применились → проверь кавычки и `>` в link, потом нажми F5 с очисткой кэша.
- Картинка растянута → проверь `object-fit: cover` — именно на `img`, а не на родителе.
