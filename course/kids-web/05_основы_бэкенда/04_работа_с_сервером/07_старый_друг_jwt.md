# Старый друг JWT

URL: https://practicum.yandex.ru/learn/kids-web/courses/fca180a1-4dc7-4494-818a-9536e5cf7aeb/sprints/190125/topics/53bf9e76-ef5e-415d-9751-d5a9e2c2d7f1/lessons/33faad9f-c5ee-4ad6-974e-6377a3d578e2/

Course: Основы бэкенда

Topic: Работа с сервером

Type: web

---

# Старый друг JWT

Из объекта запроса функция достаёт почту и пароль юзера. Затем она использует метод модели `users` для поиска пользователя по его данным. Это **кастомный** метод модели, который мы создавали в уроке «Собственные методы моделей Mongoose». Если пользователь с такими реквизитами есть в базе, авторизацию можно считать успешной. Функция отправит на клиент данные юзера и подтвердит авторизацию, установив в ответе статус `200`. В случае если пользователь с такими реквизитами не будет найден, на клиент вернётся статус `401`, означающий ошибку авторизации 👇🏻

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

![](https://pictures.s3.yandex.net/resources/Worn-Ass-Semi-Gloss_26_1714759397.jpg)

## Создание токена

Начнём с создания токена. Для этого потребуется установить специальную библиотеку **JSONWebToken,** используя пакетный менеджер `npm`. Открой терминал внутри проекта и введи команду 👇🏻

```bash
npm install jsonwebtoken
```

После этого в контроллер авторизации нужно импортировать экземпляр библиотеки для работы с её методами. В начале файла `controllers/auth.js` добавь строку 👇🏻

```javascript
// Другие импорты
const jwt = require("jsonwebtoken");

// Код контроллера
```

Теперь следует усовершенствовать саму функцию `login`, чтобы она генерировала токен и отправляла его вместе с данными пользователя на клиент. Для этого добавь ещё один блок `then` перед отправкой ответа 👇🏻

```javascript
// Импорты

const login = (req, res) => {
  const { email, password } = req.body;

  users
    .findUserByCredentials(email, password)
    .then((user) => {
	    // Здесь будет генерация токена
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
```

У экземпляра библиотеки JSONWebToken переменная `jwt` — это множество методов, которые доступны для использования. Чтобы создать токен, обратимся к методу `sign` и передадим нужные аргументы.

Метод `sign` принимает два обязательных и один необязательный аргумент:

- **Данные, которые будут зашифрованы в токене**
Обычно в качестве них передают идентификатор пользователя или его почту. Передавать всё сразу не нужно, чтобы не перегружать токен.
- **Секретный ключ, которым можно будет расшифровать токен**
В качестве секретного ключа указывается обычная строка с каким-то текстом. Благодаря этому ключу можно будет расшифровать данные и проверить токен.
- **Другие опции**
Полный список опций и за что они отвечают, можно посмотреть на [странице библиотеки](https://www.npmjs.com/package/jsonwebtoken){target="_blank"} JSONWebToken. Самая интересная опция — `expiresIn` — обозначает время, в течение которого токен остаётся действительным.

Добавь этот метод в контроллер авторизации 👇🏻

```javascript
// Импорты

const login = (req, res) => {
  const { email, password } = req.body;

  users
    .findUserByCredentials(email, password)
    .then((user) => {
	    const token = jwt.sign({ _id: user._id }, "some-secret-key", {
        expiresIn: 3600
      });
    })
    // Остальной код
};
```

Здесь ты создаёшь переменную `token` для хранения токена и внутри неё обращаешься к экземпляру `jwt`, вызывая метод `sign`

Первым аргументом укажи данные, которые будут зашифрованы в токене. В твоём случае это объект с единственным полем `_id` 👇🏻

```javascript
{ _id: user._id }
```

Вторым аргументом укажи строку с секретным ключом. Долго гадать не будем — укажи простую фразу, но, если хочешь, можешь выбрать любой ключ самостоятельно 👇🏻

```javascript
"some-secret-key"
```

Третьим аргументом передай объект опций, в котором будет параметр, определяющий время жизни токена. Установи ему числовое значение 👇🏻

```javascript
{ expiresIn: 3600 } // Время жизни токена — один час, то есть 3600 секунд
```

Кроме числовых значений можно использовать и строчные с добавлением букв. Буква означает единицу измерения — миллисекунды, минуты, часы или дни 👇🏻

```javascript
expiresIn: '120ms' // 120 миллисекунд
expiresIn: '15m' // Пятнадцать минут
expiresIn: '2h' // Два часа
expiresIn: '7d' // Семь дней
```

После создания токена его нужно передать следующему блоку `then`, который вернёт ответ на клиент. Для этого из первого `then` верни новый объект с двумя полями: `user` — объектом с данными пользователя, и `token` — строкой, содержащей сам токен. Также потребуется изменить второй блок `then`, чтобы он принимал аргументом объект, который возвращает первый блок `then`. Внутри себя он должен возвращать на клиент не просто данные пользователя, но и его токен 👇🏻

```javascript
// Импорты

const login = (req, res) => {
  const { email, password } = req.body;

  users
    .findUserByCredentials(email, password)
    .then((user) => {
	    const token = jwt.sign({ _id: user._id }, "some-secret-key", {
        expiresIn: 3600
      });
      return { user, token };
    })
    .then(({ user, token }) => {
      res
        .status(200)
        .send({
	        _id: user._id, 
	        username: user.username, 
	        email: user.email, 
	        jwt: token });
	      })
    // Остальной код
};
```

Заключительный блок `then` обращается к объекту ответа `res`, указывая ему статус `200` (успешно) и отправляя на клиент данные пользователя: его идентификатор, никнейм, почту и `JWT`-токен.

## Проверка токена

Проверкой достоверности займётся новый миддлвар `checkAuth`. Для этого в папке `middlewares` создай файл `auth.js`. Внутри него также потребуется экземпляр библиотеки JSONWebToken, поэтому сразу импортируй её 👇🏻

```javascript
const jwt = require("jsonwebtoken");
```

Добавь функцию `checkAuth` и передай ей знакомые аргументы: объекты `req`, `res` и метод `next` 👇🏻

```javascript
const checkAuth = (req, res, next) => {};
```

Миддлвар будет срабатывать на всех запросах, которые требуют, чтобы пользователь был авторизован. Значит, первым делом нужно достать из объекта запроса `JWT`-токен пользователя. 

Работая с API на третьем модуле, мы передавали токен в специальном заголовке `Authorization`. Обратись к нему в функции и получи содержимое всего заголовка 👇🏻

```javascript
const checkAuth = (req, res, next) => {
	const { authorization } = req.headers;
};
```

Затем проведи небольшую проверку: если заголовок авторизации отсутствует или не начинается со слова `Bearer`, верни на клиент ошибку `Необходима авторизация` 👇🏻

```javascript
const checkAuth = (req, res, next) => {
	const { authorization } = req.headers;
	
	if (!authorization || !authorization.startsWith("Bearer ")) {
    return res.status(401).send({ message: "Необходима авторизация" });
  }
};
```

Общепринято использовать приставку `Bearer` в заголовке авторизации, но при проверке токена она будет мешать. Обратись к стандартному JS-методу `replace`, чтобы вырезать `Bearer` и пробел после него из заголовка, оставив только токен 👇🏻

```javascript
const checkAuth = (req, res, next) => {
	const { authorization } = req.headers;
	
	if (!authorization || !authorization.startsWith("Bearer ")) {
    return res.status(401).send({ message: "Необходима авторизация" });
  }
  
  const token = authorization.replace("Bearer ", "");
};
```

После извлечения и подготовки токена можно приступить к его верификации — проверке на достоверность. За это отвечает метод `verify` из библиотеки `jsonwebtoken`. Он принимает два аргумента: сам токен и секретный ключ, который поможет его расшифровать 👇🏻

```javascript
const checkAuth = (req, res, next) => {
	const { authorization } = req.headers;
	
	if (!authorization || !authorization.startsWith("Bearer ")) {
    return res.status(401).send({ message: "Необходима авторизация" });
  }
  
  const token = authorization.replace("Bearer ", "");
  req.user = jwt.verify(token, "some-secret-key");
  next();
};
```

Важно указывать секретный ключ, который использовался при генерации токена в функции `login`, иначе расшифровать его не получится. 

Теперь миддлвар проверяет токен и записывает результат в объект запроса. Результат проверки — расшифрованные данные, которые изначально были зашифрованы в токене. В функции `login` при генерации токена мы сказали зашифровать объект с идентификатором пользователя. Он и будет результатом проверки. После чего миддлвар передаст управление над запросом следующему миддлвару, используя метод `next`

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ Процесс верификации может завершиться с ошибкой. Она может возникнуть в случае, если токен устарел или при запросе был отправлен совсем не тот токен, который генерировался для этого пользователя. В этом случае тебе нужно будет прекратить запрос и вернуть ошибку `Необходима авторизация` обратно на клиент.
{/quiz-task}

Для обработки ошибки используй `try/catch` 👇🏻

```javascript
const checkAuth = (req, res, next) => {
  const { authorization } = req.headers;

  if (!authorization || !authorization.startsWith("Bearer ")) {
    return res.status(401).send({ message: "Необходима авторизация" });
  }

  const token = authorization.replace("Bearer ", "");

  try {
    req.user = jwt.verify(token, "some-secret-key");
  } catch (err) {
    return res.status(401).send({ message: "Необходима авторизация" });
  }

  next();
};
```

Давай закрепим главное:

- Миддлвар нужен для запросов, которые требуют, чтобы пользователь был авторизован. Это может быть запрос на получение своих данных или запрос на голосование за игру.
- Миддлвар извлекает заголовок авторизации из запроса пользователя. Затем он подготавливает содержимое заголовка для проверки, удаляя из него приставку `Bearer` и пробел после неё.
- После этого специальный метод `verify` проверяет, действительно ли это токен того пользователя, который отправляет запрос. Также метод проверяет, не просрочился ли токен или его пора бы уже заменить.
- Если с токеном всё гуд, миддлвар записывает расшифрованные данные в объект ответа `req`, чтобы с ним могли работать другие миддлвары или контроллер мог отправить его обратно на клиент.

## Защита маршрутов

Пришло время применить созданный миддлвар в проекте! Но перед его использованием не забудь экспортировать функцию `checkAuth` из файла `auth.js`

Другими словами, использовать `checkAuth` нужно для всех `POST`, `PUT` и `DELETE`-запросов. А как ты помнишь, обработкой маршрутов занимаются роуты.

Внедри миддлвар в игровой роут в файл `routes/games.js` 👇🏻

```javascript
// Другие импорты
const { checkAuth } = require("../middlewares/auth.js");

// Маршрут для создания игры
gamesRouter.post(
  "/games",
  findAllGames,
  checkIsGameExists,
  checkIfCategoriesAvaliable,
  checkEmptyFields,
  checkAuth,
  // Другие миддлвары и контроллеры
);

// Маршрут для обновления игры
gamesRouter.put(
  "/games/:id",
  findGameById,
  checkIsVoteRequest,
  checkIfUsersAreSafe,
  checkIfCategoriesAvaliable,
  checkEmptyFields,
  checkAuth,
  // Другие миддлвары и контроллеры
);

// Маршрут для удаления игры
gamesRouter.delete(
	"/games/:id", 
	checkAuth, 
	// Другие миддлвары и контроллеры
);
```

### Самостоятельная работа 📝

А теперь попробуй самостоятельно добавить миддлвар для `usersRouter` и `categoriesRouter` 

Для этого:

1. В роуте для работы с пользователями 👇🏻
    - Добавь миддлвар для `POST`-роута между миддлварами `checkEmptyNameAndEmailAndPassword` и `hashPassword`
    - Добавь миддлвар для `PUT`-роута между миддлварами `checkEmptyNameAndEmail` и `updateUser`
    - Добавь миддлвар для `DELETE`-роута сразу после указания пути маршрута
2. В роуте для работы с категориями игр 👇🏻
    - Добавь миддлвар для `POST`-роута между миддлварами `checkEmptyName` и `createCategory`
    - Добавь миддлвар для `PUT`-роута между миддлварами `checkEmptyName` и `updateCategory`
    - Добавь миддлвар для `DELETE`-роута сразу после указания пути маршрута

```javascript
// routes/users.js
usersRouter.post(
  "/users",
  findAllUsers,
  checkIsUserExists,
  checkEmptyNameAndEmailAndPassword,
  checkAuth,
  hashPassword,
  createUser,
  sendUserCreated
);
usersRouter.put(
  "/users/:id",
  checkEmptyNameAndEmail,
  checkAuth,
  updateUser,
  sendUserUpdated
);
usersRouter.delete(
	"/users/:id",
	checkAuth,
	deleteUser,
	sendUserDeleted
);
```

```javascript
// routes/categories.js
categoriesRouter.post(
  "/categories",
  findAllCategories,
  checkIsCategoryExists,
  checkEmptyName,
  checkAuth,
  createCategory,
  sendCategoryCreated
);
categoriesRouter.put(
  "/categories/:id",
  checkEmptyName,
  checkAuth,
  updateCategory,
  sendCategoryUpdated
);
categoriesRouter.delete(
  "/categories/:id",
  checkAuth,
  deleteCategory,
  sendCategoryDeleted
);
```

## Личный маршрут пользователя

Этот маршрут будет проверять авторизацию юзера и отправлять его данные обратно на клиент, если она прошла успешно. Миддлвар для проверки авторизации у тебя уже есть, осталось создать контроллер, который вернёт данные в ответе браузеру и настроит сам маршрут.

Начнём с контроллера. В файле `controllers/users.js` создай новую функцию `sendMe`. Она, как и другие функции в этом контроллере, будет устанавливать тип контента, который придёт на клиент в ответе. А также отправит сам ответ, преобразованный в строку JSON 👇🏻

```javascript
const sendMe = (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(req.user));
};
```

В ответе ты отправляешь поле `req.user`, так как именно в него записываются расшифрованные данные в миддлваре `checkAuth`

Теперь настрой маршрут. В файле `routes/users.js` добавь новый роут, который будет обрабатывать `GET`-запросы по маршруту `/me`. После получения запроса миддлвар `checkAuth` проверит авторизацию, а затем контроллер `sendMe` отправит ответ на клиент 👇🏻

```javascript
usersRouter.get("/me", checkAuth, sendMe);
```