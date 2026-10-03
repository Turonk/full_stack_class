# Setup Checklists

## Live Server (каждый урок A01–A24)

- [ ] Расширение Live Server / аналог установлен
- [ ] Открываем `index.html` стартера или demo, не «Open in Browser» с кривыми путями CSS
- [ ] Offline: нет зависимости от обязательного CDN (шрифты → system stack)

## Git · перед B01 и на B01

- [ ] `git --version` у каждого
- [ ] Аккаунт GitHub создан **до** урока (домашнее задание A34/B-prep)
- [ ] `git config user.name` / `user.email` заданы
- [ ] Первый commit на учебном репо курса, не в `node_modules`
- [ ] `.gitignore`: `node_modules/`, `.env`, `__pycache__/`

## Vite · B02

- [ ] Node LTS установлен до урока (`node -v`)
- [ ] `npm create vite@latest` отрабатывает в учебной папке
- [ ] `npm run dev` → localhost:5173
- [ ] Объяснение одной фразой: «сборщик, не новый язык»
- [ ] Offline fallback: заранее скачанный zip шаблона курса без сети

## Flask · A25+ / B13+

- [ ] `python -m venv .venv` и активация
- [ ] `pip install flask` в venv
- [ ] `flask run` или `python app.py` на :5000
- [ ] Реплика вслух: **session учебная, это не банк / не production-auth**

## Два порта (B17)

- [ ] Vite :5173 рисует
- [ ] Flask :5000 отвечает
- [ ] CORS понят как «два происхождения», не «магия»
