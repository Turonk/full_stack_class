# Раздаём HTML

URL: https://practicum.yandex.ru/learn/kids-web/courses/fca180a1-4dc7-4494-818a-9536e5cf7aeb/sprints/190125/topics/d034b6b4-f9ec-479f-ab65-1b8b1b769e5d/lessons/a3c0a61a-2fc2-476e-a16a-9f330ff3dc59/

Course: Основы бэкенда

Topic: Основы Node.js и Express

Type: web

---

# Раздаём HTML

![](https://pictures.s3.yandex.net:443/resources/11.04.2024_1712855934.jpg)

Мы разобрались с передачей данных в ответе на запрос. Но пользователю нужно отдавать и статичные файлы: разметку, стили, скрипты, изображения. Тебе уже знаком стандартный Node.js-модуль для работы с файлами — `fs`. Файлы, которые нужно отдавать клиентам, складывают в отдельную папку — её принято называть `public`. Ты можешь прочитать содержимое папки `public` и отдавать на запрос HTML-страницу.

В файле с роутером `main.js` для базового запроса к серверу обеспечь доступ к `index.html` 👇🏻

```javascript
// routes/main.js
const mainRoute = require("express").Router();

mainRoute.get("/", (req, res) => {
  res.status(200).send('<h1>Скоро тут будет интерфейс</h1>');
});

module.exports = mainRoute;
```

Добавь импорт модуля `fs` и методом `readFile` прочти HTML-файл из `public` с указанием верной кодировки `utf-8`. Этот процесс асинхронный, поэтому воспользуйся `.then()` и отправь ответ с указанием заголовков после чтения файла 👇🏻

```javascript
// routes/main.js
const mainRoute = require("express").Router();
const fs = require("fs").promises;

mainRoute.get("/", (req, res) => {
  fs.readFile("./public/index.html", "utf-8").then((data) => {
    res.header("Content-Type", "text/html").send(data);
  });
});
module.exports = mainRoute;
```

Теперь клиент сможет получить заготовленную HTML-страницу по `GET`-запросу с роутом `"/"`

Писать обработчики для всей этой информации неудобно и не нужно, вместо этого научимся пользоваться методом `static` из Express.

По умолчанию у пользователей нет доступа к файлам на твоём сервере. Это можно изменить, так как метод `static` принимает адрес папки на вход и делает её доступной снаружи 👇🏻

```javascript
// Сделали всё, что есть на сервере, доступным пользователю
app.use(express.static(__dirname));
```

Оптимальным вариантом будет дать доступ только к папке `public`

1) Скачай для своего проекта этот архив и добавь его в корень проекта 👇🏻

[public.zip](https://code.s3.yandex.net/kids-web/vids/M4/public.zip){target="_blank"}

2) Теперь папка `public` лежит в корне проекта на одном уровне с исполняемым файлом — `app.js`. Переменная `__dirname` указывает абсолютный путь к корню сервера, содержащему текущий исполняемый файл, поэтому остаётся только воспользоваться методом `join` (информация о методе, как всегда, в [документации](https://nodejs.org/api/path.html#pathjoinpaths){target="_blank"}), чтобы склеить абсолютный путь до файла и название папки с файлами, к которым хотим дать доступ 👇🏻

```javascript
// app.js 
const express = require('express');
const path = require('path');
const mainRoute = require('./routes/main');
const gamesRouter = require('./routes/games'); 

const PORT = 3000;
const app = express();

// Теперь клиент имеет доступ только к публичным файлам
app.use(express.static(path.join(__dirname, 'public'))); 

app.use(mainRoute, gamesRouter); 

app.listen(PORT, () => {
  console.log(`Server is running at PORT http://localhost:${PORT}`);
})
```

Метод `static` задаёт определённую логику отправки файлов. Если обратиться к корню сервера, ты автоматически попадёшь в `public` и получишь файл `index.html`. Получается, что не нужно добавлять в запрос имя файла, достаточно просто обратиться в корень — по адресу `"/"`

Публичная папка — отправная точка в проекте, которую мы уже указали с помощью `express.static`