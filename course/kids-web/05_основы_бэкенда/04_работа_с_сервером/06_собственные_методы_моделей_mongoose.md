# Собственные методы моделей Mongoose

URL: https://practicum.yandex.ru/learn/kids-web/courses/fca180a1-4dc7-4494-818a-9536e5cf7aeb/sprints/190125/topics/53bf9e76-ef5e-415d-9751-d5a9e2c2d7f1/lessons/dba0fae8-22da-4227-8625-7b3cfd1315ef/

Course: Основы бэкенда

Topic: Работа с сервером

Type: web

---

# Собственные методы моделей Mongoose

![](https://pictures.s3.yandex.net/resources/Mongoose_1714758989.jpg)

Сейчас цепочка промисов работает так:

- Проверяет, есть ли в базе пользователь с указанной почтой.
- Если пользователь найден, сверяет хеш его пароля с теми хешами, что были созданы при регистрации пользователя.

```javascript
// controllers/auth.js

const login = (req, res) => {
  const { email, password } = req.body;

  users
    .findOne({ email })
    .then(user => {
      if (!user) {
        return Promise.reject(new Error("Неправильные почта или пароль"));
      }

      return bcrypt.compare(password, user.password).then(matched => {
        if (!matched) {
          // Хеши не совпали — отклоняем промис
          return Promise.reject(new Error("Неправильные почта или пароль"));
        }
        // Аутентификация успешна
        return user; // Теперь user доступен
      })
    })
    .then((user) => {
      res
        .status(200)
        .send({ _id: user._id, username: user.username, email: user.email });
    })
    .catch(error => {
      res.status(401).send({ message: error.message });
    });
};

// Не забываем экспортировать функцию 
module.exports = { login };
```

Пользоваться снова будем Mongoose. Чтобы добавить собственный метод, запиши его в свойство `statics` нужной схемы 👇🏻

```javascript
// models/user.js

const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");

const userSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true
  },
  email: {
    type: String,
    required: true,
    unique: true
  },
  password: {
    type: String,
    required: true,
    minlength: 8
  }
});

// Добавим метод findUserByCredentials схеме пользователя,
// у него будет два параметра: почта и пароль
userSchema.statics.findUserByCredentials = function (email, password) {

};

module.exports = mongoose.model('user', userSchema);
```

Осталось написать сам код метода. Работать он должен примерно так 👇🏻

```javascript
// controllers/auth.js

const login = (req, res) => {
  const { email, password } = req.body;

  users.findUserByCredentials('emailExample@yandex.ru', 'passwordExample')
    .then(user => {
      // Получаем объект пользователя, если почта и пароль подошли
    })
    .catch(err => {
      // Получаем ошибку, если нет
    });
};

module.exports = { login };
```

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ Статические методы в моделях Mongoose предоставляют удобный способ выполнения операций над коллекцией документов, не создавая экземпляр модели. Написание собственных методов позволяет расширить возможности модели, адаптировать код под проект.
{/quiz-task}

За счёт выноса логики поиска пользователя по `email` и `password` в отдельный собственный метод мы разгрузили файл контроллера и создали удобный и простой способ взаимодействия с моделью, который можем переиспользовать во всём проекте.

### Описываем метод `findUserByCredentials`

Чтобы найти пользователя по почте, нам потребуется метод `findOne`, которому следует передать на вход `email`. Метод `findOne` принадлежит модели `users`, поэтому обратись к нему через ключевое слово `this` 👇🏻

```javascript
// models/user.js

userSchema.statics.findUserByCredentials = function(email, password) {
  // Попытаемся найти пользователя по почте
  return this.findOne({ email }) // this — это модель users
    .then(user => {
      if (!user) {
        // Не нашёлся — отклоняем промис
        return Promise.reject(new Error("Неправильные почта или пароль"));
      }
      
      // Нашёлся — сравниваем хеши
      return bcrypt.compare(password, user.password).then(matched => {
      if (!matched) {
        return Promise.reject(new Error("Неправильные почта или пароль"));
      }

      return user; // Теперь user доступен
    });
  });
};

module.exports = mongoose.model("user", userSchema);
```

Заметь, что функция `findUserByCredentials` не должна быть **стрелочной.** Это сделано, чтобы мы могли использовать `this`

Одно из ключевых отличий **стрелочных** функций от **традиционных** функций, которые начинаются с ключевого слова `function`, — это взаимодействие с контекстом выполнения функции и ключевым словом `this`

{quiz-task}
    background: |
        #f1f1ef
    content: |
        📚 Ознакомиться со сложной и объёмной темой про `this` более детально можно в этой [статье](https://doka.guide/js/function-context/){target="_blank"}.
{/quiz-task}

Осталось добавить обработку ошибки, когда хеши не совпадают. Опиши этот код в ещё одном обработчике — `then`

Сначала разберём, как делать не стоит 👇🏻

```javascript
// models/user.js

userSchema.statics.findUserByCredentials = function(email, password) {
  // Попытаемся найти пользователя по почте
  return this.findOne({ email }) // this — это модель users
    .then(user => {
      if (!user) {
        // Не нашёлся — отклоняем промис
        return Promise.reject(new Error("Неправильные почта или пароль"));
      }
      
      // Нашёлся — сравниваем хеши
      return bcrypt.compare(password, user.password)
    })
    .then(matched => {
      if (!matched) {
        // Отклоняем промис
        return Promise.reject(new Error("Неправильные почта или пароль"));
      }

      return user; // Но переменной user нет в этой области видимости
    });
  });
};

module.exports = mongoose.model("user", userSchema);
```

Здесь во втором `then` мы обращаемся к объекту `user`, которого нет в блоке кода, так как он остался в предыдущем `then`

Чтобы решить эту проблему, следует организовать цепочку промисов иначе: добавить обработчик `then` вызову метода `bcrypt.compare` 👇🏻

```javascript
// models/user.js

userSchema.statics.findUserByCredentials = function(email, password) {
  // Попытаемся найти пользователя по почте
  return this.findOne({ email }) // this — это модель users
    .then(user => {
      if (!user) {
        // Не нашёлся — отклоняем промис
        return Promise.reject(new Error("Неправильные почта или пароль"));
      }
      
      // Нашёлся — сравниваем хеши
      return bcrypt.compare(password, user.password)
        .then(matched => {
          if (!matched) {
            return Promise.reject(new Error("Неправильные почта или пароль"));
          }

          return user; // Теперь user доступен
      });
  });
};

module.exports = mongoose.model("user", userSchema);
```

Код метода готов! Теперь можешь применить его в обработчике аутентификации 👇🏻

```javascript
// controllers/auth.js

const login = (req, res) => {
  const { email, password } = req.body;

  users
    .findUserByCredentials(email, password)
    .then((user) => {
      res
        .status(200)
        .send({ _id: user._id, username: user.username, email: user.email });
    })
    .catch(error => {
      res.status(401).send({ message: error.message });
    });
};
```

### Описываем метод `findGameByCategory`

Да, по аналогии статические методы Mongoose помогают расширить и упростить взаимодействие с данными в MongoDB. 

Для декомпозиции кода вынеси поиск игры по категории в отдельный метод `findGameByCategory` модели `game`. Актуальное состояние файла `game.js` 👇🏻

```javascript
// models/game.js

const mongoose = require("mongoose");
const userModel = require("./user");
const categoryModel = require("./category");

const gameSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
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
  users: [
    {
      type: mongoose.Schema.Types.ObjectId,
      ref: userModel // Содержит ссылки на связанные с игрой модели пользователей
    }
  ],
  categories: [
    {
      type: mongoose.Schema.Types.ObjectId,
      ref: categoryModel // Содержит ссылки на связанные с игрой модели категорий
    }
  ]
});

// Добавим метод для поиска игр по категории 
gameSchema.statics.findGameByCategory = function(category) {
  //...
}

module.exports = mongoose.model("game", gameSchema);
```

Чтобы найти игры по категории, тебе потребуется методом `find` сперва обнаружить все записи об играх; потом, используя дополнительный метод `populate`, подгрузить связанные с играми записи о пользователях и категориях. А чтобы выборка игр совпадала с переданной категорией, укажи методу `populate` для категорий опцию `match: { name: category }` 👇🏻

```javascript
// models/game.js

gameSchema.statics.findGameByCategory = function(category) {
  return this.find({}) // Выполним поиск всех игр
    .populate({
      path: "categories",
      match: { name: category } // Опция поможет сопоставить подходящие игры по выбранной категории 
    })
    .populate({
      path: "users",
      select: "-password" // Позволяет получить записи о пользователях за исключением их паролей (они же хранятся в зашифрованном виде)
    })
    // ...
};
```

Опция сопоставления `match` не отфильтровывает документы. Если нет файлов, соответствующих совпадению, ты можешь получить документы с пустым массивом категорий. Чтобы наверняка отфильтровать подходящие по категориям игры, в методе `then` отфильтруй массив игр по длине свойства `categories` 👇🏻

```javascript
// models/game.js

gameSchema.statics.findGameByCategory = function(category) {
  return this.find({}) // Выполним поиск всех игр
    .populate({
      path: "categories",
      match: { name: category } 
    })
    .populate({
      path: "users",
      select: "-password"
    })
    .then(games => {
	    // Отфильтруем по наличию искомой категории 
      return games.filter(game => game.categories.length > 0);
    });
};
```

Функция `findAllGames` в базовом случае должна находить все игры проекта, подгружать к ним записи о категориях и пользователях. Теперь важно учесть пару моментов:

- **Исключи данные о паролях пользователей**
Это приватная информация только для регистрации и аутентификации пользователя на сайте. Сделать это можно, используя опцию `select` в методе `populate`
- **Передай категорию игры**
Поиск всех игр должен работать с переданным параметром, например категорией. Передав категорию игры в качестве параметра в `url` запроса, мы позволяем серверу прочитать значение параметра (жанра) в объекте запроса по ключу `req.query["categories.name"]`

Если жанр игры передан параметром `req.query["categories.name"]`, воспользуйся статическим методом для поиска игр по категории 👇🏻

```javascript
// middlewares/games.js

const findAllGames = async (req, res, next) => {
  // Поиск всех игр в проекте по заданной категории
  if(req.query["categories.name"]) { 
    req.gamesArray = await games.findGameByCategory(req.query["categories.name"]);
    next();
    return;
  }
  // Поиск всех игр в проекте
  req.gamesArray = await games
    .find({})
    .populate("categories")
    .populate({
      path: "users",
      select: "-password" // Исключим данные о паролях пользователей
    })
  next();
};

```