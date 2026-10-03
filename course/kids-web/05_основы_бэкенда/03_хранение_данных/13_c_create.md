# C — create

URL: https://practicum.yandex.ru/learn/kids-web/courses/fca180a1-4dc7-4494-818a-9536e5cf7aeb/sprints/190125/topics/b0783e3e-bba5-418d-9bdb-d5fa877df8f3/lessons/807001ca-e081-4e15-9047-bd28f0f72038/

Course: Основы бэкенда

Topic: Хранение данных

Type: web

---

# C — create

{video:https://code.s3.yandex.net/kids-web/vids/M4/M4T3/2024-04-05_22-12-36.mp4|controls:true|autoplay:0|pip:false|controlsList:nodownload}

{video:https://code.s3.yandex.net/kids-web/vids/M4/M4T3/Create.mp4}

## Создание документов

Метод `create` — это способ добавления новой записи в коллекцию MongoDB. Он принимает объект с данными, которые нужно сохранить в БД. Давай рассмотрим, как он работает на практике, чтобы к концу урока создать функцию добавления игры.

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ В твоём проекте уже есть заготовки для работы с играми по маршруту `/games`: сам роут, миддлвар для выполнения промежуточных действий и обработчик маршрута, то есть контроллер. Обрати внимание на миддлвар — файл `games.js`, который можно найти в директории `middlewares`. Внутри него создана функция `findAllGames`, использующая метод `find` для поиска всех игр в коллекции `games` твоей базы данных.
{/quiz-task}


Метод `create` работает схожим образом, поэтому для него создай асинхронную функцию `createGame` 👇🏻

```javascript
const createGame = async (req, res, next) => {
  console.log("POST /games");
};
```

Она принимает три важных аргумента: объект запроса `req`, объект ответа `res`, а также специальный метод `next()` для запуска следующего по списку миддлвара.

На стороне клиента, когда пользователь заполнит данные об игре в форму и нажмёт на кнопку `Добавить игру`, интерфейс отправит запрос на сервер. В его тело `req.body` будут переданы данные игры, которые ввели через форму.

То есть тебе нужно передать их в метод `create`, чтобы именно они записались в базу данных. Для этого обратись к модели `games` и вызови метод `create`, передав аргументом тело запроса 👇🏻

```javascript
const createGame = async (req, res, next) => {
  console.log("POST /games");
  games.create(req.body)
};
```

Да, но не стоит забывать про обработку ошибок. Метод `create` всегда возвращает **промис,** а значит, вместе с ним нужно использовать конструкцию `try…catch` или обработчики `then` и `catch` 👇🏻

```javascript
const createGame = async (req, res, next) => {
  console.log("POST /games");
  try {
    console.log(req.body);
    req.game = await games.create(req.body);
    next();
  } catch (error) {
  	res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Ошибка создания игры" }));
  }
};
```

Используй ключевое слово `await` перед вызовом метода `create`, а перед добавлением игры в базу данных выведи в консоль тело запроса. Результат запиши в объект `req` поля `game` и используй `next()`. Это позволит передать запрос следующему миддлвару — ему станут доступны данные из `req.game`

В блоке `catch` обратись к объекту ответа `res`, установи `400`-й статус ошибки и передай соответствующее сообщение.

### Самостоятельная работа 📝

1. Создай функцию `createCategory` в миддлваре `categories.js` 👇🏻

    a. Передай в качестве аргументов `req`, `res` и `next` 
    
    b. Используй `try…catch` для обработки ошибок
    
    c. Запиши в `req.category` результат работы метода `create` 
    
    d. В качестве текста ошибки выведи `Error creating category`
    
2. Создай функцию `createUser` в миддлваре `users.js` 👇🏻

    a. Передай в качестве аргументов `req`, `res` и `next` 
    
    b. Используй `try…catch` для обработки ошибок
    
    c. Запиши в `req.user` результат работы метода `create` 
    
    d. В качестве текста ошибки выведи `Error creating category`

```javascript
// middlewares/categories.js
const createCategory = async (req, res, next) => {
  console.log("POST /categories");
  try {
	  console.log(req.body);
    req.category = await categories.create(req.body);
    next();
  } catch (error) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Ошибка создания категории" }));
  }
};
```

```javascript
// middlewares/users.js
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

## Добавление контроллеров

Мы не просто так использовали метод `next()` в миддлварах. Следующий, кто примется за работу с запросом, будет сам контроллер. Сейчас попробуем с тобой описать один из них для запроса на создание игры. 

Для этого перейди в файл `games.js` в папке `controllers`. Теперь добавь стрелочную функцию `sendGameCreated`, которая аргументами будет принимать объект запроса `req` и объект ответа `res` 👇🏻

```javascript
const sendGameCreated = (req, res) => {}
```

Основная задача контроллера — вернуть ответ клиенту. Для этого функция должна установить заголовки с типом контента и закрыть запрос, отправив данные игры, которую до этого миддлвар добавил в базу данных 👇🏻

```javascript
const sendGameCreated = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(req.game));
};
```

Обращаясь к методу `setHeader`, установи уже знакомый заголовок `Content-Type`. В качестве значения укажи `application/json`, сообщая клиенту, что ответ придёт в формате JSON. 

В миддлваре `createGame` результат создания игры мы поместили в объект запроса `req` в поле `game`. Именно данные этого поля нам и нужно передать в ответе, чтобы на клиенте отобразилась созданная игра и пользователь понял: операция прошла успешно. Преобразуй `req.game` в строку формата JSON и отправь её в ответ.

### Самостоятельная работа📝

1. Создай функцию `sendCategoryCreated` в контроллере `categories.js` 👇🏻

    a. Передай в качестве аргументов `req` и `res` 
    
    b. Установи заголовок с типом контента в ответе со значением `application/json` 
    
    c. Заверши запрос, передав в ответе `req.category`, преобразованный в строку JSON
    
2. Создай функцию `sendUserCreated` в контроллере `users.js` 👇🏻

    a. Передай в качестве аргументов `req` и `res` 
    
    b. Установи заголовок с типом контента в ответе со значением `application/json` 
    
    c. Заверши запрос, передав в ответе `req.user`, преобразованный в строку JSON

```javascript
// controllers/categories.js
const sendCategoryCreated = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(req.category));
};
```

```javascript
// controllers/users.js
const sendUserCreated = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(req.user));
};
```

## Работа с роутами

Роуты позволяют принимать запросы на определённые маршруты и задавать последовательность функций, каждая из которых должна обработать запрос перед тем, как сервер вернёт ответ обратно клиенту.

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ Метод `create` отвечает за создание какого-либо документа в БД, а это значит, что он должен принимать данные, чтобы уметь обращаться к базе и просить её создать из них новый документ в нужной коллекции. Чтобы отправлять данные, используется метод `POST`, с которым мы тебя уже знакомили.
{/quiz-task}

Начнём с игровых! Перейди в файл `games.js` папки `routes` и создай новый роут, который будет принимать `POST`-запросы по маршруту `/games` 👇🏻

```javascript
gamesRouter.post("/games");
```

Первым аргументом контроллер принимает маршрут, а остальными можно передать функции, которые будут обрабатывать запрос по нему. Здесь тебе и пригодятся созданные ранее миддлвары и контроллеры. Импортируй функции `createGame` и `sendGameCreated`

В следующих уроках мы доработаем наш игровой миддлвар, чтобы он проверял запрос от клиента и помогал обрабатывать возможные ошибки. Так, если игра уже есть в коллекции, она не будет создаваться заново, дублируя одни и те же документы 👇🏻

```javascript
gamesRouter.post("/games", findAllGames);
```

Теперь передай контроль над запросом функции `createGame`, которая добавит игру в БД. Последним работать с запросом будет контроллер `sendGameCreated`, завершающий его отправкой ответа на сторону клиента 👇🏻

```javascript
gamesRouter.post("/games", findAllGames, createGame, sendGameCreated);
```

### Самостоятельная работа📝

1. Создай новый роут для обработки `POST`-запроса в роуте `categories.js` 👇🏻

    a. Первым аргументом передай маршрут `/categories`
    
    b. Затем передай управление функции `findAllCategories`
    
    c. После её работы в бой должен вступать миддлвар `createCategory`
    
    d. В завершение отправкой ответа займётся контроллер `sendCategoryCreated`
    
2. Создай новый роут для обработки `POST`-запроса в роуте `users.js` 👇🏻

    a. Первым аргументом передай маршрут `/users`
    
    b. Затем передай управление функции `findAllUsers`
    
    c. После её работы в бой должен вступать миддлвар `createUser` 
    
    d. В завершение отправкой ответа займётся контроллер `sendUserCreated`

```javascript
// routes/categories.js
categoriesRouter.post(
	"/categories", 
	findAllCategories, 
	createCategory, 
	sendCategoryCreated
);
```

```javascript
// routes/users.js
usersRouter.post(
  "/users",
  findAllUsers,
  createUser,
  sendUserCreated
);
```