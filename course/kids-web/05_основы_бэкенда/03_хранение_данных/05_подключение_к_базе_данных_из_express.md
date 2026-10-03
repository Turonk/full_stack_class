# Подключение к базе данных из Express

URL: https://practicum.yandex.ru/learn/kids-web/courses/fca180a1-4dc7-4494-818a-9536e5cf7aeb/sprints/190125/topics/b0783e3e-bba5-418d-9bdb-d5fa877df8f3/lessons/132b0620-499d-4902-81e1-bcf97549e622/

Course: Основы бэкенда

Topic: Хранение данных

Type: web

---

# Подключение к базе данных из Express

![](https://pictures.s3.yandex.net:443/resources/Worn-Ass-Semi-Gloss_3_1713460645.jpg)

Чтобы подружить JS с документами, существуют специальные инструменты — **ODM,** или **Object Document Mapper** (с англ. «сопоставитель объектов и документов»). У каждой БД свой собственный сопоставитель. Например, у MongoDB он называется **Mongoose** и представляет собой мост между двумя мирами — миром документов в базе данных и миром объектов JavaScript.

В этом уроке ты только установишь и запустишь его, а работу начнёшь уже в следующем.

### Старт

Тебе предстоит подключить базу данных к приложению на Express. Это новый проект, ты начинаешь работу над Pindie. Поэтому потребуется новое приложение с базовыми настройками.

1. Создай новый проект, это тебе уже знакомо из урока **«Билет на Express»**. Хорошим названием для проекта будет `pindie-backend`
2. Следом создай в Github новый репозиторий под проект и сделай первый пуш туда. Как это сделать, рассказывали в уроке **«Git через терминал»**.
3. Задай базовые настройки: запусти сервер на порту `3000`, добавь `CORS` и `bodyParser`, научи проект отдавать HTML на сервер (уроки **«Раздаём HTML»**, **«CORS»** и **«Миддлвары»**).
4. Тебе также нужен новый фронтенд в папке `/public`. Прикладываем его ниже (скачай архив и положи в проект) 👇🏻
    
    [public.zip](https://code.s3.yandex.net/kids-web/vids/M4/M4T3/files/public.zip){target="_blank"}

Теперь, когда предварительная настройка закончена, можно подключать базу данных.

### Устанавливаем Mongoose

Открой в терминале папку с проектом и запусти команду `npm` 👇🏻

```bash
npm i mongoose
```

Теперь сопоставитель можно импортировать как модуль и пользоваться.

В корне проекта создай папку `database`, а в ней — файл `connect.js`, в который добавь функцию `connectToDatabase` 👇🏻

```javascript
const mongoose = require('mongoose');

const DB_URL = 'mongodb://localhost:27017/pindie';

async function connectToDatabase() {
  try {
    await mongoose.connect(DB_URL);
    console.log('Успешно подключились к MongoDB')
  }
  catch (err) {
    console.log('При подключении MongoDB возникла ошибка')
    console.error(err);
  }
}

module.exports = connectToDatabase;
```

Непосредственное подключение к базе данных осуществляется строкой 👇🏻

```javascript
await mongoose.connect(DB_URL);
```

Здесь `DB_URL` — адрес базы данных, который состоит из двух частей:

- `mongodb://localhost:27017` — адрес сервера MongoDB,
- `pindie` — имя БД на сервере MongoDB, которую мы будем использовать для записи и чтения данных.

Далее просто вызови функцию `connectToDatabase` в файле `app.js`, таким образом подключишься к базе данных при старте приложения. 

Вот полный код 👇🏻

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const usersRouter = require('./routes/users');
const gamesRouter = require('./routes/games');
const categoriesRouter = require('./routes/categories');

const connectToDatabase = require('./database/connect');
const cors = require('./middlewares/cors');

const app = express();
const PORT = 3000;

connectToDatabase();

app.use(
  cors, 
  bodyParser.json(),
  express.static(path.join(__dirname, 'public')),
  usersRouter, 
  gamesRouter, 
  categoriesRouter
);

app.listen(PORT);
```

### Запускаем сервер MongoDB

Перед тем как запускать Node.js-приложение, которое будет записывать и читать из базы данных `pindie`, нужно сначала запустить сервер MongoDB.

Сделать это можно следующей командой под тогглом 👀

```bash
mongod --config /usr/local/etc/mongod.conf --fork
```

```bash
mongod --config /opt/homebrew/etc/mongod.conf --fork
```

```bash
mongod
```

Если первая команда для Windows не сработала, воспользуйся альтернативной 👇🏻

```bash
mongod --port 27017 --dbpath "C:\data\db"
```