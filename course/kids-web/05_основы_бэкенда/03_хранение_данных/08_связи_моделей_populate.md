# Связи моделей. Populate

URL: https://practicum.yandex.ru/learn/kids-web/courses/fca180a1-4dc7-4494-818a-9536e5cf7aeb/sprints/190125/topics/b0783e3e-bba5-418d-9bdb-d5fa877df8f3/lessons/39cfc03f-47aa-4a60-b987-7bafc00d2a5d/

Course: Основы бэкенда

Topic: Хранение данных

Type: web

---

# Связи моделей. Populate

![](https://pictures.s3.yandex.net:443/resources/Worn-Ass-Semi-Gloss_7_1713540702.jpg)

## Настраиваем связь двух схем

Построение связи начинается со схемы. В Pindie две сущности: категории и игры. Вот схема игры 👇🏻

```javascript
const mongoose = require('mongoose');

const gameSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  developer: {
    type: String,
    required: true
  },
  image: {
    type: String,
    required: true
  },
  link: {
    type: String,
    required: true
  }
});

module.exports = mongoose.model('game', gameSchema);
```

Игры могут относиться к определённым категориям, которые описываются одним полем `name`, то есть их названием 👇🏻

```javascript
const mongoose = require('mongoose');

const categorySchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
});

module.exports = mongoose.model('category', categorySchema);
```

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ Лучшая ссылка из одного документа на другой — идентификатор. Mongo автоматически создаёт поле `_id` — уникальный идентификатор для каждого из них. Именно он позволяет связать один документ с другим.
{/quiz-task}

Чтобы сделать это на уровне схемы, полю следует установить специальный тип — `mongoose.Schema.Types.ObjectId` — и свойство `ref`. В него записывают имя модели, на которую ссылаются. Главное, не забудь импортировать свойство в файл 👇🏻

```javascript
const mongoose = require('mongoose');
// Импорт модели для связывания 
const categoryModel = require('./category');

const gameSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  developer: {
    type: String,
    required: true
  },
  image: {
    type: String,
    required: true
  },
  link: {
    type: String,
    required: true
  },
  // Добавляем свойство категории с массивом объектов, в котором укажем 
  // тип ObjectId и ref на существующую модель категорий
  categories: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: categoryModel,
  }],
});

module.exports = mongoose.model('game', gameSchema);
```

Также в твоём проекте пользователи могут голосовать. Получается, что данные о пользователях, которые отдали голос в пользу игры, нужно тоже хранить в схеме.

Рассмотрим их модель. Она содержит несколько обязательных полей — `username`, `email` и `password` 👇🏻

```javascript
// models/user.js

const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
  },
  password: {
    type: String,
    required: true
  },
});

module.exports = mongoose.model('user', userSchema);
```

Аналогичным образом, как с категориями, создай поле `users` в схеме игры и свяжи элемент массива со схемой пользователя. Для этого нужно использовать идентификатор, который автоматически присвоит Mongo для пользователя `mongoose.Schema.Types.Objectd`, и свойство `ref` со ссылкой на его модель 👇🏻

```javascript
const mongoose = require('mongoose');
// Не забываем импортировать модель, на которую ссылаемся
const userModel = require('./user');
const categoryModel = require('./category');

const gameSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  developer: {
    type: String,
    required: true
  },
  image: {
    type: String,
    required: true
  },
  link: {
    type: String,
    required: true
  },
  // Добавляем поле для списка пользователей
  users: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: userModel,
  }],
  // Добавляем поле для списка категорий
  categories: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: categoryModel,
  }],
});

module.exports = mongoose.model('game', gameSchema);
```

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ Теперь, когда в твоей модели есть связи, можешь попробовать посоздавать через Compass тестовые данные в коллекции игр. В массив помещай `_id` категорий и игр из соответствующих коллекций. А если эти упражнения тебя утомляют, просто импортируй наши данные в Compass, там уже настроены связи — но обязательно посмотри, как это устроено. С данными коллекциями всё заработает.

        [pindie.categories.json](https://code.s3.yandex.net/kids-web/vids/M4/M4T3/pindie.categories.json){target="_blank"}

        [pindie.games.json](https://code.s3.yandex.net/kids-web/vids/M4/M4T3/pindie.games.json){target="_blank"}

        [pindie.users.json](https://code.s3.yandex.net/kids-web/vids/M4/M4T3/pindie.users.json?etag=914870702313b3368f48bc774279b4c6){target="_blank"}

        Твой браузер умеет открывать JSON-файлы, поэтому при клике на них они покажутся в новой вкладке. Скачать их можно через меню (**Файл ➡️ Сохранить**) в твоём браузере или через комбинацию клавиш `Ctrl + S`. После этого файлы можно импортировать в Compass.
{/quiz-task}

## **Получаем всю информацию — метод `populate`**

В прошлом уроке мы уже написали миддлвары для поиска пользователей и категорий проекта, а теперь попробуем получить данные об играх. 

В папке `middlewares` создай файл `games.js`, импортируй в него модель `games` и запиши функцию для поиска всех игр с использованием метода модели `find` 👇🏻

```javascript
// Файл middlewares/games.js

// Импортируем модель
const games = require("../models/game");

const findAllGames = async (req, res, next) => {
  // По GET-запросу на эндпоинт /games найдём все документы категорий
  req.gamesArray = await games.find({});
  // Выведем в терминал результат поиска 
  console.log(req.gamesArray);
  next();
};

// Экспортируем функцию поиска всех игр
module.exports = findAllGames;
```

Супер! Метод `find` найдёт все документы с информацией об играх. 

Давай взглянем на один из результатов — все поля заполнены согласно схеме: `title`, `description` и другие значения ключей в виде строк. Чекай, что ничего не пропущено 👇🏻

```javascript
[
  {
    _id: new ObjectId('65ef2c368c121ad8a56dabc2'),
    title: 'G.U.N.N.E.R.',
    description: 'Продержись как можно дольше, отбиваясь от врагов, которых будет становиться всё больше.',
    developer: 'IDKWIAm',
    image: 'https://code.s3.yandex.net/teens/pindie-games/gunner/cover.png',
    link: 'https://code.s3.yandex.net/teens/pindie-games/gunner/game/index.html',
    categories: [
      new ObjectId('65ef2d1f8c121ad8a56dabc6'),
      new ObjectId('65ef2d848c121ad8a56dabc9')
    ],
    users: [ new ObjectId('65ef1f358c121ad8a56dabb6') ]
  }
]
```

К самой модели игры Mongo автоматически добавила поле с идентификатором `_id`, а в полях `categories` и `users` хранятся также идентификаторы моделей категорий и пользователей соответственно. 

Теперь создай контроллер, который будет возвращать результат поиска в ответе на запрос 👇🏻

```javascript
// Файл controllers/games.js

const sendAllGames = (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  // Вернём найденные игры в формате JSON
  res.end(JSON.stringify(req.gamesArray));
};

module.exports = sendAllGames;
```

Добавь в роут `gamesRouter` обработку `GET`-запроса по эндпоинту `'/games'` с использованием `findAllGames` и `sendAllGames` 👇🏻

```javascript
// Файл routes/games.js

const gamesRouter = require('express').Router();

const findAllGames = require('../middlewares/games');
const sendAllGames = require('../controllers/games');

gamesRouter.get('/games', findAllGames, sendAllGames);

module.exports = gamesRouter;
```

В результате сервер будет обрабатывать запрос на получение данных об играх.

Почти. Давай протестируем в Postman запрос и убедимся, что результат соответствует данным, хранящимся на сервере 👇🏻

![](https://pictures.s3.yandex.net:443/resources/1_3_1713540730.jpg)

![](https://pictures.s3.yandex.net:443/resources/2_3_1713540746.jpg)

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ Идентификатор — это полезный элемент для связывания данных, но одного его недостаточно для отображения актуальных категорий и пользователей. Нужны конкретные поля: для категорий — `name`, а для пользователей — `username`. Чтобы в поля `categories` и `users` загрузились данные из документов по указанным идентификаторам, необходимо дополнительно использовать метод `populate` для связанных моделей.
{/quiz-task}

Метод `populate` позволяет ссылаться на документы в других коллекциях и автоматически заменяет указанные ссылки на другие документы данными из них. 

Для этого нужно вызвать метод и передать в него аргументом название коллекции, которую нужно подгрузить. Последовательно вызови `.populate("categories").populate("users")` 👇🏻

```javascript
const findAllGames = async (req, res, next) => {
  // Используем метод populate для загрузки данных
  // из моделей categories и users по их id
  const result = await games.find({}).populate("categories").populate("users");
  console.log(result);
  next();
};
```

Теперь в полях `categories` и `users` ты увидишь подробную информацию о каждом элементе: метод `populate` по идентификатору и ссылке на другую модель нашёл данные и подставил их в нужные места 👇🏻

![](https://pictures.s3.yandex.net:443/resources/3_3_1713540774.jpg)

Отправив ответ на запрос, клиент получит всё необходимое для отображения информации об игре 👇🏻

```javascript
// Файл middlewares/games.js

// Импортируем модель
const games = require("../models/game");

const findAllGames = async (req, res, next) => {
  req.gamesArray = await games.find({}).populate("categories").populate("users");
  next();
};

// Экспортируем функцию поиска всех игр
module.exports = findAllGames;
```

Смотри, вот так данные об игре будут отображаться на клиенте 👇🏻

![](https://pictures.s3.yandex.net:443/resources/5_3_1713540794.jpg)

Теперь объект с описанием игры имеет всю необходимую информацию, в том числе список категорий и пользователей, проголосовавших за неё 👇🏻

![](https://pictures.s3.yandex.net:443/resources/4_3_1713540839.jpg)