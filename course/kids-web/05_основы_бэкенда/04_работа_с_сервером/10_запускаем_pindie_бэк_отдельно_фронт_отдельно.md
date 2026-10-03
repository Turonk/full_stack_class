# Запускаем Pindie: бэк отдельно, фронт отдельно

URL: https://practicum.yandex.ru/learn/kids-web/courses/fca180a1-4dc7-4494-818a-9536e5cf7aeb/sprints/190125/topics/53bf9e76-ef5e-415d-9751-d5a9e2c2d7f1/lessons/11aced92-0b53-4cfa-abf6-0d70ea0cf0ef/

Course: Основы бэкенда

Topic: Работа с сервером

Type: web

---

# Запускаем Pindie: бэк отдельно, фронт отдельно

![](https://pictures.s3.yandex.net/resources/Pindie_0_1715007105.jpg)

Запусти фронтенд Pindie из третьего модуля и убедись, что он запустился на порте `3000` (по адресу [localhost:3000](http://localhost:3000){target="_blank"} в браузере).

Супер! Дальше в этом уроке мы будем подсказывать тебе, как доработать код в твоём фронтенде, чтобы он научился взаимодействовать с бэкендом. 

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ Не исключено, что при выполнении практики в этом уроке что-то не будет работать так, как надо. На этот случай мы прикладываем свой архив с тем, что у тебя должно было получиться в конце прошлого модуля. Можешь сверить свой код с кодом в архиве и доработать его при необходимости.

        [pindie-theme-8-main.zip](https://code.s3.yandex.net/kids-web/vids/M4/M4T4/pindie-theme-8-main.zip){target="_blank"}

        Заодно скачай нашу коллекцию данных и импортируй её в Compass. 

        [pindie-collections.zip](https://code.s3.yandex.net/kids-web/vids/M4/M4T4/pindie-collections.zip){target="_blank"}
{/quiz-task}

Запусти бэкенд на порте `3001`. Указать порт нужно в `app.js` 👇🏻

```javascript
/* app.js */

const PORT = 3001;
/* Код Express-приложения */
app.listen(PORT);
```

Теперь можно перейти к обновлению фронтенда и бэкенда.

## Наводим порядки в Next.js-приложении

Сначала обнови файл `/app/api/config.js` на фронте. Сейчас в константе `BASE_URL` адресом для отправления запросов указан `https://api-code-2.practicum-team.ru` — замени его на `http://localhost:3001/api`

Ещё поменяй несколько эндпоинтов. Теперь авторизация идёт по новым адресам:

- `/auth/login`
- `/me`

С нашего бэкенда приходят JSON-файлы с несколько другой структурой (есть поле `_id` вместо `id` и `users` вместо поля `users_permissions_users`). 

У нас уже создана функция `normalizeDataObject`, которая приводит полученные с бэкенда данные к нужному нам виду. Её надо обновить. Можешь скопировать новую функцию из блока ниже 👇🏻

```javascript
const normalizeDataObject = (obj) => {
  let str = JSON.stringify(obj)
  
  str = str.replaceAll('_id', 'id');
  const newObj = JSON.parse(str)
  const result = { ...newObj, category: newObj.categories }
  return result;
}
```

Теперь обнови авторизацию. Раньше при авторизации приходил объект такого вида 👇🏻

```javascript
{
	identifier: "",
	password: "",
	id: ""
}
```

Сейчас этот объект выглядит так 👇🏻

```javascript
{
	email: "",
	password: "",
	_id: ""
}
```

Поэтому нужно заменить `identifier` на `email` в файле `/app/components/AuthForm/AuthForm.jsx` (при создании стейта `authData` и в атрибуте `name` поля ввода электронной почты). Новый вариант идентификатора `_id` нужно передавать при вызове `authContext.login()` (первым параметром — объект `{ …userData, id: userData._id }`).

```javascript
const [authData, setAuthData] = useState({ email: "", password: "" });
```

```javascript
authContext.login({...userData, id: userData._id}, userData.jwt);
```

```javascript
<input
  onInput={handleInput}
  className={Styles["form__field-input"]}
  name="email"
  type="email"
  placeholder="hello@world.com"
/>
```

Ещё нужно, чтобы голосование заработало с новым ключом. У нас теперь нет ключа `users_permissions_users`, поэтому функцию `vote` внутри `app/api/api-utils.js` нужно переписать. Новый `body` в запросе к серверу 👇🏻

```javascript
body: JSON.stringify({ users: usersArray })
```

Небольшие доработки также потребуются в `store`. В файле `app/store/app-store.js` есть такая строчка 👇🏻

```javascript
set({ isAuth: true, user, token: jwt });
```

Она должна стать такой, чтобы в сторе хранился верный `id` 👇🏻

```javascript
set({ isAuth: true, user: { ...user, id: user._id }, token: jwt });
```

## Наводим порядки в Express-приложении

Теперь обнови бэкенд приложения. 

Чтобы запросы к бэкенду не блокировались CORS, нужно записать порты `3000` и `3001` в список разрешённых портов в файле `/middlewares/cors.js` (о CORS мы говорили подробно в одноимённом уроке).

Нужно сделать так, чтобы при голосовании пользователя за игру не проверялись категории и пустые поля. Для этого надо отличать `PUT`-запросы из админки, которые изменяют данные об игре, и запросы голосования за игру из Pindie. Этого можно добиться, добавив миддлвар `checkIsVoteRequest` в файл `/middlewares/games.js`, который будет записывать в объект `req`, что полученный запрос — голос за игру 👇🏻

```javascript
const checkIsVoteRequest = async (req, res, next) => {
	// Если в запросе присылают только поле users
  if (Object.keys(req.body).length === 1 && req.body.users) {
    req.isVoteRequest = true;
  }
  next();
};
```

Теперь, если запрос будет голосом за игру, можно не проверять её на категории и пустые поля, а передавать следующим миддлварам через условие в начале функций `checkEmptyFields` и `checkIfCategoriesAvailable` 👇🏻

```javascript
if(req.isVoteRequest) {
    next();
    return;
  }
```

Осталось обновить роутер `gamesRouter.put` в `/routes/games.js`. Проверка `checkIsVoteRequest` должна идти сразу после миддлвара `findGameById`

Последний штрих, чтобы всё точно запустилось — донастрой CORS. В миддлваре `middlewares/cors.js` разреши все ключевые запросы между доменами. Перед вызовом `next()` добавь строчки 👇🏻

```javascript
res.header("Access-Control-Allow-Methods", "GET,HEAD,PUT,PATCH,POST,DELETE");
res.header("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers, Authorization");
```

Теперь Pindie завершён целиком — фронт запущен отдельно от бэка и получает данные из него.

## Задача со звёздочкой

Задача в том, что на фронте нужно сделать так, чтобы получение пустой коллекции из базы данных не ломало проект.

**В чём проблема сейчас**

При получении игр по категории, если массив окажется пустым, приложение выдаст ошибку.

**Как решить**

Предлагаем три варианта решения, используй любой из них на свой вкус:

- Измени функцию `getNormalizedGamesDataByCategory` так, чтобы при проверке длины массива не выбрасывалась ошибка.
- Измени хук `useGetDataByCategory`, добавив дополнительную проверку `isResponseOk` перед тем, как возвращать данные.
- Измени проверку массива `gamesArray` на каждой странице категорий: пусть проверяется не только массив, но и его длина.

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ Когда сделаешь всё, описанное в этом уроке, и фронтенд начнёт работать с бэкендом, помести их в два отдельных репозитория на гитхабе. Скорее всего, бэкенд у тебя уже лежит там, нужно просто сделать коммит и пуш. А вот для кода фронтенда Pindie создай отдельный репозиторий. Эти репозитории ты будешь использовать в следующей теме, поэтому подготовься заранее.
{/quiz-task}