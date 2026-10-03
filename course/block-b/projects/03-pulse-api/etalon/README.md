# PulseAPI · эталон блока B

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
flask --app app run --debug
pytest
```

Фронт Vite: в `vite.config.js` поставь `server.proxy: { '/api': 'http://127.0.0.1:5000' }`.

Учебный пин логина: `1234`. Это не безопасность, это урок сессии.
