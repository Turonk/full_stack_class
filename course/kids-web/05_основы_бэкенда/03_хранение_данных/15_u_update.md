# U — update

URL: https://practicum.yandex.ru/learn/kids-web/courses/fca180a1-4dc7-4494-818a-9536e5cf7aeb/sprints/190125/topics/b0783e3e-bba5-418d-9bdb-d5fa877df8f3/lessons/5f5c0493-8b00-4f2d-99ec-72adc5aa9b6d/

Course: Основы бэкенда

Topic: Хранение данных

Type: web

---

# U — update

![](https://pictures.s3.yandex.net:443/resources/Worn-Ass-Semi-Gloss_14_1714122940.jpg)

Для начала загляни в папку с роутом `/games`

Чтобы обновить данные, тебе понадобится слушать `PUT`-запросы по эндпоинту `"/games/:id"` 👇🏻

```javascript
// Файл routes/games.js

// Пока запишем порядок действий псевдокодом 
gamesRouter.put(
  "/games/:id", // Слушаем запросы по эндпоинту
	// Шаг 1. Находим игру по id из запроса
	// Шаг 2. Выполняем проверки для корректного обновления (опционально)
	// Шаг 3. Обновляем запись с игрой
	// Шаг 4. Возвращаем на клиент ответ с результатом обновления
);
```

### Шаг 1. Поиск игры по `id`

Для обновления конкретной записи её изначально нужно найти. 

Создай миддлвар-функцию для поиска игры — `findGameById`. Ранее она была описана в уроке **«R — read»,** сейчас вместе будем её дорабатывать.

Используй переданный в запросе `id` (идентификатор игры), который, как обычно, получишь из параметров запроса `req.params.id`. Не забывай и про блок `try/catch`, чтобы обработать возможные ошибки, ведь искомой игры может и не существовать.

В блоке `try` обратись к базе данных: у модели `games` методами `findById` найди запись и воспользуйся методами `populate` для загрузки данных о категориях и пользователях, связанных с искомой игрой 👇🏻

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
    res.setHeader("Content-Type", "application/json");
    res.status(404).send(JSON.stringify({ message: "Игра не найдена" }));
  }
};
```

### Шаг 2. Проверки

На этом шаге ты обычно проверяешь тело запроса с данными. Прежде чем вносить изменения в базу данных, нужно убедиться, что информация безопасна и корректна.

### Шаг 3. Обновляем запись с игрой

Если данные в теле запроса соответствуют требованиям MongoDB, можно обновить запись об игре. Для этого опиши очередную миддлвар-функцию — `updateGame`. Так как процесс обновления записи не мгновенный, функция будет асинхронная с блоком `try/catch`

Для обновления конкретной записи в библиотеке Mongoose существует [подходящий метод](https://mongoosejs.com/docs/api/model.html#Model.findByIdAndUpdate()) у модели — `findByIdAndUpdate`. Вызови его на `games` и передай на вход идентификатор в строковом виде. Вторым параметром — объект со свойствами, которые нужно обновить 👇🏻

```javascript
// Файл middlewares/games.js

const updateGame = async (req, res, next) => {
  try {
	  // В метод передаём id из параметров запроса и объект с новыми свойствами
    req.game = await games.findByIdAndUpdate(req.params.id, req.body);
    next();
  } catch (error) {
    res.setHeader("Content-Type", "application/json");
    res.status(400).send(JSON.stringify({ message: "Ошибка обновления игры" }));
  }
};
```

### Шаг 4. Возвращаем на клиент ответ с результатом обновления

В папке `controllers` в файле `games.js` запиши `sendGameUpdated` — простую функцию, которая будет возвращать сообщение `"Игра обновлена"` 👇🏻

```javascript
// Файл controllers/games.js

const sendGameUpdated = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.status(200).send(JSON.stringify({ message: "Игра обновлена" }));
};
```

### Подведём итоги

Все разобранные тобой сегодня функции нужно импортировать в папку `routes` и файл `games.js`. Теперь вместо псевдокода смело вставляй то, что должно выполняться в роуте в случае `PUT`-запроса с обновлёнными данными 👇🏻

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

### Самостоятельная работа 📝

Опиши по аналогии роуты для обновления категорий и пользователей.

1. Обновление категорий 👇🏻

```javascript
// Файл routes/categories.js

categoriesRouter.put(
  "/categories/:id", // Слушаем запросы по эндпоинту
  updateCategory, // Обновляем запись в MongoDB
  sendCategoryUpdated // Возвращаем ответ на клиент
);
```

- В миддлвар-функции `updateCategory` используй метод модели `findByIdAndUpdate` для обновления записи в MongoDB по аналогии с разобранной выше функцией `updateGame`
- В контроллере `sendCategoryUpdated` верни сообщение `res.status(200).send(JSON.stringify({ message: "Категория обновлена" }));`

2\. Обновление пользователей👇🏻

```javascript
// Файл routes/users.js

usersRouter.put(
  "/users/:id", // Слушаем запросы по эндпоинту
  updateUser, // Обновляем запись в MongoDB
  sendUserUpdated // Возвращаем ответ на клиент
);
```

- В миддлвар-функции `updateUser` используй метод модели `findByIdAndUpdate` для обновления записи в MongoDB по аналогии с разобранной выше функцией `updateGame`
- В контроллере `sendUserUpdated` верни сообщение `res.status(200).send(JSON.stringify({ message: "Пользователь обновлён" }));`