# A11 · Слайды (проектор)

---

# PulseLab · A11
Motion: одна анимация без ряби
Спринт 2 · **MusicHub**

---

# Retrieval · 60 сек
1. Три ручки иерархии?
2. Что делает clamp()?
3. Роли Syne и IBM Plex Sans?

---

# Сцена
Бейдж «В ЭФИРЕ» стоит, как приклеенный.
У настоящих радио эфир **пульсирует**.
Музыкальный сайт без движения — склад.

---

# Предикт (руки)
Анимировать ВСЁ: фон, карточки, кнопки, бейдж…
1. Вау!
2. Рябит, укачивает, бесит

Правило курса: **одна анимация на экран**

---

# Лифт vs стиральная машина
| transition | @keyframes |
| два состояния | сценарий по шагам |
| по событию (hover) | сам, по команде |
| один раз | infinite — по кругу |

---

# Пульс
```css
@keyframes pulse {
  0%   { box-shadow: 0 0 0 0 rgba(124,92,255,.6); }
  70%  { box-shadow: 0 0 0 12px rgba(124,92,255,0); }
  100% { box-shadow: 0 0 0 0 rgba(124,92,255,0); }
}
.live-badge { animation: pulse 2s infinite; }
```
2–3s = дыхание · 0.3s = стробоскоп

---

# Уважение: reduced-motion
```css
@media (prefers-reduced-motion: reduce) {
  .live-badge, .btn, .card { animation: none; transition: none; }
}
```
Профессиональный стандарт, а не «фича для вежливых»

---

# Checkpoint
1. transition vs @keyframes?
2. Что делает prefers-reduced-motion?

---

# You do · критерий «готово»
- [ ] бейдж «В ЭФИРЕ» пульсирует (2–3s)
- [ ] одна зацикленная анимация
- [ ] reduced-motion глушит всё движение
- [ ] hover + focus-visible живы (A05)
- [ ] дешёвые свойства: transform/opacity/filter/shadow

---

# Exit + A12
1. Термин: transition / keyframes / reduced-motion
2. Скрин или видео пульса в чат
3. **Завтра showcase:** демо 360 → 1200 → `:root` → один приём. Репетируй с таймером: 6 минут
