# API-контракт PulseAPI (учебный)

База: `http://127.0.0.1:5000`

| Метод | Путь | Ок | Ошибки |
| --- | --- | --- | --- |
| GET | /api/health | `{ok:true, version}` | |
| GET | /api/tracks | массив треков | |
| GET | /api/tracks/:id | объект | 404 `{error}` |
| GET | /api/top | 3 трека | |
| GET | /api/scores | топ-10 | |
| POST | /api/scores | 201 `{ok:true}` | 400 `{error, field}` |
| POST | /api/login | `{user}` | 400 |
| GET | /api/me | `{user}` | |
| GET | /api/cabinet | кабинет | 401 |
| POST | /api/logout | `{ok:true}` | |

GET без побочных эффектов. POST без JSON → 400.
