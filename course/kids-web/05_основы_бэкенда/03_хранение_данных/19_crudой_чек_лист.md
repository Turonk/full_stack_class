# CRUDой чек-лист

URL: https://practicum.yandex.ru/learn/kids-web/courses/fca180a1-4dc7-4494-818a-9536e5cf7aeb/sprints/190125/topics/b0783e3e-bba5-418d-9bdb-d5fa877df8f3/lessons/c6e11221-0102-4f70-8c94-0772e337244a/

Course: Основы бэкенда

Topic: Хранение данных

Type: web

---

# CRUDой чек-лист

![](https://pictures.s3.yandex.net:443/resources/IMG_4918_2_1_1714062359.png)

## Чек-лист 📝

### Часть 1. Обновление папки

Для начала проверь, что папка `public` обновлена — в проекте изменился фронтенд приложения. 
Если это ещё не сделано, лови новую и замени ею уже имеющуюся 👇🏻 

[public.zip](https://code.s3.yandex.net/kids-web/vids/M4/M4T3/public.zip){target="_blank"}

### Часть 2. C — Create

Убедись, что настроена функция **Create** — метод для добавления новых данных в базу.

1. Создана асинхронная функция `createGame` в файле `/middlewares/games.js` 👇🏻
Она принимает три аргумента: объект запроса `req`, объект ответа `res`, а также метод `next()` для запуска следующего по списку миддлвара.
В теле запроса `req.body` будут переданы данные игры, которые пользователь заполнял через форму. Нужно обратиться к модели `games` и вызвать метод `create`, передав аргументом `req.body` (перед вызовом `create` должно быть ключевое слово `await`). Результат запроса записывается в `req.game`
Не забудь про обработку ошибок: метод `create` возвращает промис, значит, код следует обернуть в конструкцию `try … catch` или обработчики `then`/`catch`. В случае ошибки устанавливается статус `400` и отправляется сообщение `Ошибка создания игры`

```javascript
const createGame = async (req, res, next) => {
  console.log("POST /games");
  try {
    console.log(req.body);
    req.game = await games.create(req.body);
    next();
  } catch (error) {
    res.status(400).send("Error creating game");
  }
};
```

2\. Создана функция `createCategory` в файле `/middlewares/categories.js`. Алгоритм её настройки аналогичен функции `createGame` 👇🏻

* Передай в функцию аргументы `req`, `res` и `next`
* Используй `try … catch` для обработки ошибок.
* Запиши в `req.category` результат работы метода `create`
- В качестве текста ошибки выведи `Ошибка создания категории`

```javascript
const createCategory = async (req, res, next) => {
  console.log("POST /categories");
  try {
    req.category = await categories.create(req.body);
    next();
  } catch (error) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Ошибка создания категории" }));
  }
};
```

3\. Создана функция `createUser` в файле `/middlewares/users.js`. И снова те же действия 👇🏻

- Передай в функцию аргументы `req`, `res` и `next`
- Используй `try … catch` для обработки ошибок.
- Запиши в `req.user` результат работы метода `create`
- В качестве текста ошибки выведи `Ошибка создания пользователя`

```javascript
const createUser = async (req, res, next) => {
  console.log("POST /users");
  try {
    console.log(req.body);
    req.user = await users.create(req.body);
    next();
  } catch (error) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Ошибка создания пользователя" }));
  }
};
```

4\. Теперь нужно проверить контроллеры для обработки `create`-запросов. Должны быть созданы 👇🏻

- `sendGameCreated` в файле `/controllers/games.js`
- `sendCategoryCreated` в файле `/controllers/categories.js`
- `sendUserCreated` в файле `/controllers/users.js`

Все три функции принимают аргументами объект запроса `req` и объект ответа `res`. В теле функции устанавливаются заголовки с правильным типом контента (в твоём случае `application/json`), а возвращается объект с добавленными в базу данными, приведёнными к строке командой `JSON.stringify`

Функция `sendGameCreated` должна вернуть `req.game`, `sendCategoryCreated` — `req.category`, `sendUserCreated` — `req.user`

```javascript
const sendGameCreated = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(req.game));
};
```

```javascript
const sendCategoryCreated = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(req.category));
};
```

```javascript
const sendUserCreated = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(req.user));
};
```

5\. После того как подготовлен контроллер, убедись в настройке роутера 👇🏻

- В файле `/routes/games.js` добавь обработчик `POST`-запросов по маршруту `/games`. Подключи миддлвары, которые создали ранее: `createGame`, `sendGameCreated`
- В `/routes/categories.js` добавь обработчик `POST`-запросов по маршруту `/categories`. Подключи миддлвары `createCategory` и `sendCategoryCreated`
- В `/routes/users.js` добавь обработчик `POST`-запросов по маршруту `/users`. Подключи миддлвары `createUser` и `sendUserCreated`

```javascript
gamesRouter.post("/games", findAllGames, createGame, sendGameCreated);
```

```javascript
categoriesRouter.post(
  "/categories",
  findAllCategories,
  createCategory,
  sendCategoryCreated
);
```

```javascript
usersRouter.post(
  "/users",
  findAllUsers,
  createUser,
  sendUserCreated
);
```

### Часть 3. R — Read

Убедись, что настроена функция **Read** — методы для чтения из базы данных. 

1. В файле `/middlewares/games.js` создана асинхронная функция `findGameById` — поиск игры по ID 👇🏻
Она принимает три аргумента: объект запроса `req`, объект ответа `res`, а также метод `next()` для запуска следующего миддлвара.
Запрос к базе снова должен быть обёрнут в конструкцию `try … catch`. Для этого в блоке `try` создай новое поле `game` в объекте запроса `req` и присвой ему результат работы функции `findById`
Аргументом `req.params.id` должен быть переданный в параметрах запроса `id` нужной игры. 
После этого вызывай функцию `next()`
Проверь, что при ошибке пользователю отправится сообщение `Игра не найдена` и статус `404`

```javascript
const findGameById = async (req, res, next) => {
	try {
		req.game = await games.findById(req.params.id);
    next();
	} catch (error) {
		res.status(404).send({ message: "Game not found" });
	}
};
```

2. По аналогии созданы функции `findCategoryById` в `/middlewares/categories.js` и `findUserById` в `/middlewares/users.js` 👇🏻
Записывай найденную категорию в `req.category`, а найденного пользователя — в `req.user`

```javascript
// middlewares/users.js
const findUserById = async (req, res, next) => {
  console.log("GET /users/:id");
  try {
    req.user = await users.findById(req.params.id);
    next();
  } catch (error) {
    res.setHeader("Content-Type", "application/json");
		res.status(404).send(JSON.stringify({ message: "Пользователь не найдена" }));
  }
};
```

```javascript
// middlewares/categories.js
const findCategoryById = async (req, res, next) => {
  console.log("GET /categories/:id");
  try {
    req.category = await categories.findById(req.params.id);
    next();
  } catch (error) {
    res.setHeader("Content-Type", "application/json");
		res.status(404).send(JSON.stringify({ message: "Категория не найдена" }));
  }
};
```

3. Обновлены функции `findAllGames` и `findGameById` 👇🏻
Настрой их работу так, чтобы при ответе передавались все данные о категориях, а данные пользователя не содержали пароль. Для этого воспользуйся методом `populate`. Чтобы исключить пароли из ответа, передай объект `{ path: "users", select: "-password" }` при вызове метода `populate` для данных пользователей.

```javascript
const findAllGames = async (req, res, next) => {
  console.log("GET /games");
  req.gamesArray = await games
    .find({})
    .populate("categories")
    .populate({
		  path: "users",
		  select: "-password"
		});
  next();
};
```

4. В файле `/controllers/games.js` создана функция `sendGameById` для отправления данных об игре, найденной по `id` 👇🏻
Установи тип контента `application/json` и отправь приведённым к строке `req.game`

```javascript
const sendGameById = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(req.game));
}; 
```

5. В файле `/routes/games.js` добавлен маршрут, в котором указано, что игру можно получить по её идентификатору 👇🏻
Для этого подключи `findGameById` и `sendGameById`

```javascript
gamesRouter.get("/games/:id", findGameById, sendGameById);
```

6\. Создана функция `sendCategoryById` в контроллере `categories.js` 👇🏻

- Внутри функции установи заголовок с типом контента `application/json`
- Отправь на клиент данные пользователя из поля `req.category`, преобразовав данные в строку формата JSON.

```javascript
const sendCategoryById = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(req.category));
};
```

7\. Создан маршрут на получение данных категории по идентификатору в роуте `categories.js` 👇🏻

- Укажи маршруту тип запроса `GET`
- Передай первым аргументом путь `/categories/:id`
- Передай следующими аргументами миддлвар `findCategoryById` и контроллер `sendCategoryById` в порядке следования.

```javascript
categoriesRouter.get("/categories/:id", findCategoryById, sendCategoryById);
```

8\. Создана функция `sendUserById` в контроллере `users.js` 👇🏻

- Внутри функции установи заголовок с типом контента `application/json`
- Отправь на клиент данные пользователя из поля `req.user`, преобразовав их в строку формата JSON.

```javascript
const sendUserById = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(req.user));
};
```

9\. Создан маршрут на получение данных пользователя по идентификатору в роуте `users.js` 👇🏻

- Укажи маршруту тип запроса `GET`
- Передай первым аргументом путь `/users/:id`
- Передай следующими аргументами миддлвар `findUserById` и контроллер `sendUserById` в порядке следования.

```javascript
usersRouter.get("/users/:id", findUserById, sendUserById);
```

### Часть 4. U — Update

Убедись, что настроена функция **Update** — методы для обновления уже имеющихся в базе данных записей. 

1. Обновлён миддлвар `findGameById` в файле `/middlewares/games.js` 👇🏻
Теперь вместо метода `.find({})` нужно использовать `.findById()`, а аргументом передавать значение `id` из `req.params.id`. Не забудь обернуть это всё в `try/catch`. 
В блоке `try` обратись к БД: у модели `games` методами `findById` найди запись и воспользуйся методами `populate` для загрузки данных о категориях и пользователях, связанных с искомой игрой.

```javascript
// Файл middlewares/games.js

const findGameById = async (req, res, next) => {
  try {
	  // Пробуем найти игру по id
    req.game = await games
      .findById(req.params.id) // Поиск записи по id
      .populate("categories") // Загрузка связанных записей о категориях
      .populate("users"); // Загрузка связанных записей о пользователях
    next(); // Передаём управление в следующую функцию
  } catch (error) {
    // На случай ошибки вернём статус-код 404 с сообщением, что игра не найдена
    res.status(404).send({ message: "Игра не найдена" });
  }
};
```

2. Создан миддлвар `updateGame` в файле `middlewares/games.js` 👇🏻
Это должна быть асинхронная функция, обёрнутая в блок `try/catch`. Для этого воспользуйся методом `findByIdAndUpdate`, который принимает два параметра: `id` (получи его из `req.params.id`) и объект со свойствами, которые нужно обновить.

```javascript
// Файл middlewares/games.js

const updateGame = async (req, res, next) => {
  try {
	  // В метод передаём id из параметров запроса и объект с новыми свойствами
    req.game = await games.findByIdAndUpdate(req.params.id, req.body);
    next();
  } catch (error) {
    res.status(400).send({ message: "Ошибка обновления игры" });
  }
};
```

3. Добавлена функция-контроллер `sendGameUpdated` в `/controllers/games.js`👇🏻 
Её назначением будет отправка сообщения `Игра обновлена`

```javascript
// Файл controllers/games.js

const sendGameUpdated = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end({ message: "Игра обновлена" });
};
```

4. Обновлён роутер игр 👇🏻
Для этого добавь инструкцию, что делать при получении `PUT`-запроса: сначала ищешь игру по ID, обновляешь запись с игрой и возвращаешь ответ клиенту.

```javascript
// Файл routes/games.js

// Пока запишем порядок действий псевдокодом 
gamesRouter.put(
  "/games/:id", // Слушаем запросы по эндпоинту  
	findGameById, // Шаг 1. Находим игру по id из запроса
	// Шаг 2. Проверки, если нужны
	updateGame, // Шаг 3. Обновляем запись с игрой
	sendGameUpdated // Шаг 4. Возвращаем на клиент ответ с результатом обновления
);
```

5\. По аналогии описаны обновления категорий и пользователей 👇🏻

- Для обновления категорий создай миддлвар `updateCategory` в `/middlewares/categories.js`, контроллер `sendCategoryUpdated` в `/controllers/categories.js` с сообщением `Категория обновлена` и опиши, как обрабатывать запрос в роутере `/routes/categories.js`

```javascript
categoriesRouter.put(
  "/categories/:id",
  updateCategory,
  sendCategoryUpdated
);
```

- Для обновления пользователей создай миддлвар `updateUser` в `/middlewares/users.js`, контроллер `sendUserUpdated` в `/controllers/users.js` с сообщением `Пользователь обновлён` и опиши, как обрабатывать запрос в роутере `/routes/users.js`

```javascript
usersRouter.put(
  "/users/:id",
  updateUser,
  sendUserUpdated
);
```

### Часть 5. D — Delete

Убедись, что настроена функция **Delete** — методы для удаления записи из базы данных.

1. Записана миддлвар-функция `deleteGame` в файле `/middlewares/games.js` 👇🏻
Для этого понадобится метод `findByIdAndDelete` с аргументом `id`. Не забывай о `try/catch`

```javascript
// Файл middlewares/games.js

const deleteGame = async (req, res, next) => {
  try {
    // Методом findByIdAndDelete по id находим и удаляем документ из базы данных
    req.game = await games.findByIdAndDelete(req.params.id);
    next();
  } catch (error) {
    res.status(400).send({ message: "Error deleting game" });
  }
};
```

2. Добавлен контроллер в файле `sendGameDeleted` в `/controllers/games.js` 👇🏻
Отправляй в ответе объект с удалённой игры.

```javascript
// Файл controllers/games.js

const sendGameDeleted = (req, res) => {
	// Объект игры отправляем в формате JSON 
  res.setHeader("Content-Type", "application/json");
  // Отправляем на клиент найденный и удалённый элемент из базы данных
  res.end(JSON.stringify(req.game));
};
```

3. Обновлён роутер игр и описано, что делать при получении `DELETE`-запрос 👇🏻

```javascript
// Файл routes/games.js

gamesRouter.delete(
  "/games/:id", // Слушаем запросы по эндпоинту
  deleteGame,
  sendGameDeleted // Тут будут функция удаления элементов из MongoDB и ответ клиенту
);
```

4\. По аналогии описаны удаления игр и пользователей 👇🏻

Для пользователей `usersRouter.delete("/users/:id", deleteUser, sendUserDeleted);` 

- Добавь миддлвар с использованием метода модели `findByIdAndDelete`, передав аргументом `id` пользователя.

```javascript
const deleteUser = async (req, res, next) => {
  console.log("DELETE /users/:id");
  try {
    req.user = await users.findByIdAndDelete(req.params.id);
    next();
  } catch (error) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Ошибка удаления пользователя" }));
  }
};
```

- Верни удалённого пользователя `req.user` в качестве ответа на запрос.

```javascript
const sendUserDeleted = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(req.user));
};
```

Для категорий `categoriesRouter.delete("/categories/:id", deleteCategory, sendCategoryDeleted);` 

- Добавь миддлвар с использованием метода модели `findByIdAndDelete`, передав аргументом `id` категории.

```javascript
const deleteCategory = async (req, res, next) => {
  console.log("DELETE /categories/:id");
  try {
    req.category = await categories.findByIdAndDelete(req.params.id);
    next();
  } catch (error) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Ошибка удаления категории" }));
  }
};
```

- Верни удалённого пользователя `req.category` в качестве ответа на запрос.

```javascript
const sendCategoryDeleted = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(req.category));
};
```

## Напоследок. Проверки и ошибки

Для обработки неправильного ввода пользователя внедри в проект миддлвары. Они будут проверять пустые поля и попытку сломать твой бэкенд.

1. **Проверка пустых полей**
При попытках создать или обновить игру, убедись, что обязательные поля приходят с фронтенда. Это поля `title`, `description`, `image`, `link` и `description`

```javascript
const checkEmptyFields = async (req, res, next) => {
  if (
    !req.body.title ||
    !req.body.description ||
    !req.body.image ||
    !req.body.link ||
    !req.body.developer
  ) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Заполните все поля" }));
  } else {
    next();
  }
};
```

При попытках создать категорию — проверь, что `name` не пустое.

```javascript
const checkEmptyName = async (req, res, next) => {
  if (!req.body.name) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Введите название категории" }));
  } else {
    next();
  }
};
```

При создании пользователя проверяй, что введены его имя, email и пароль.

```javascript
const checkEmptyNameAndEmailAndPassword = async (req, res, next) => {
  if (!req.body.username || !req.body.email || !req.body.password) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Введите имя, email и пароль" }));
  } else {
    next();
  }
};
```

А при обновлении пользователя нужна проверка, что имя пользователя или
          email не пустые.

```javascript
const checkEmptyNameAndEmail = async (req, res, next) => {
  if (!req.body.username || !req.body.email) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Введите имя и email" }));
  } else {
    next();
  }
};
```

2. **Проверка дубликатов**
Перед тем, как создавать новую игру или обновлять существующую, проверь, нет ли игры с таким же названием в базе.

```javascript
const checkIsGameExists = async (req, res, next) => {
  const isInArray = req.gamesArray.find((game) => {
    return req.body.title === game.title;
  });
  if (isInArray) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Игра с таким названием уже существует" }));
  } else {
    next();
  }
};
```

Та же самая проверка нужна для пользователя и категории.

```javascript
const checkIsUserExists = async (req, res, next) => {
  const isInArray = req.usersArray.find((user) => {
    return req.body.email === user.email;
  });
  if (isInArray) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Пользователь с таким email уже существует" }));
  } else {
    next();
  }
};
```

```javascript
const checkIsCategoryExists = async (req, res, next) => {
  const isInArray = req.categoriesArray.find((category) => {
    return req.body.name === category.name;
  });
  if (isInArray) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Категория с таким названием уже существует" }));
  } else {
    next();
  }
};
```

3. **Проверка наличия категории у игры**
Нам нельзя добавлять в базу игры без присвоенных категорий. Проверь это.

```javascript
const checkIfCategoriesAvaliable = async (req, res, next) => {
  if (!req.body.categories || req.body.categories.length === 0) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Выберите хотя бы одну категорию" }));
  } else {
    next();
  }
};
```

4. **Проверка, что прикрепленных к игре пользователей больше ровно на одного**
Это самая сложная проверка. Проверь, что при обновлении игры в случае приходящего массива с пользователями игры количество пользователей в этом массиве увеличивается на единицу. Это нужно для механики голосования за игру.

```javascript
const checkIfUsersAreSafe = async (req, res, next) => {
  if (!req.body.users) {
    next();
    return;
  }
  if (req.body.users.length - 1 === req.game.users.length) {
    next();
    return;
  } else {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Нельзя удалять пользователей или добавлять больше одного пользователя" }));
  }
};
```

5. **Обновление роутов, добавление миддлваров проверок**
Убедись, что проверки на своём месте.

```javascript
gamesRouter.post(
  "/games",
  findAllGames,
  checkIsGameExists,
  checkIfCategoriesAvaliable,
  checkEmptyFields,
  createGame,
  sendGameCreated
);

gamesRouter.put(
  "/games/:id",
  findGameById,
  checkIfUsersAreSafe,
  checkIfCategoriesAvaliable,
  checkEmptyFields,
  updateGame,
  sendGameUpdated
);
```

```javascript
categoriesRouter.post(
  "/categories",
  findAllCategories,
  checkIsCategoryExists,
  checkEmptyName,
  createCategory,
  sendCategoryCreated
);

categoriesRouter.put(
  "/categories/:id",
  checkEmptyName,
  updateCategory,
  sendCategoryUpdated
);
```

```javascript
usersRouter.post(
  "/users",
  findAllUsers,
  checkIsUserExists,
  checkEmptyNameAndEmailAndPassword,
  createUser,
  sendUserCreated
);

usersRouter.put(
  "/users/:id",
  checkEmptyNameAndEmail,
  updateUser,
  sendUserUpdated
);
```