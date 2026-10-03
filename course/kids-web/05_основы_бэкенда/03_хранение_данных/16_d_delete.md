# D — delete

URL: https://practicum.yandex.ru/learn/kids-web/courses/fca180a1-4dc7-4494-818a-9536e5cf7aeb/sprints/190125/topics/b0783e3e-bba5-418d-9bdb-d5fa877df8f3/lessons/512458c8-e11f-41b3-99bb-7c0edef09267/

Course: Основы бэкенда

Topic: Хранение данных

Type: web

---

# D — delete

![](https://pictures.s3.yandex.net:443/resources/Delete_1714046731.jpg)

Работая с MongoDB, ты используешь инструменты, предоставляемые библиотекой Mongoose. Создание записей, поиск в базе данных, обновление и множество других операций доступны разработчикам в виде методов моделей. 

{quiz-task}
    background: |
        #f1f1ef
    content: |
        📚 Так как модели отвечают за создание и получение документов из БД, в функциях мы часто выбираем подходящий метод из API библиотеки. 
        Со всеми доступными методами можно подробнее ознакомиться в [документации](https://mongoosejs.com/docs/api/model.html){target="_blank"}.
{/quiz-task}

Из наших предыдущих уроков тебе уже знакомы:

- `Model.create()`
- `Model.find()`
- `Model.findById()`
- `Model.findByIdAndUpdate()`

А сегодня разберём новый метод — `Model.findByIdAndDelete()`

Запрос на удаление для твоего сервера должен выполняться с определёнными требованиями: содержать метод `delete` и `id` элемента. Лови подробную инструкцию ниже.

## Шаг 1

Для начала создай для маршрута `gamesRouter` ещё один обработчик. Можешь воспользоваться методом `delete`, а идентификатор `id` удаляемого элемента получи из параметра запроса по эндпоинту `"/games/:id"` 👇🏻

```javascript
// Файл routes/games.js

gamesRouter.delete(
  "/games/:id", // Слушаем запросы по эндпоинту
  // Тут будут функция удаления элементов из MongoDB и ответ клиенту
);
```

Именно `id` поможет найти нужный документ в базе данных.

## Шаг 2

Теперь запиши миддлвар-функцию `deleteGame` для поиска и удаления игры. Для этого достаточно воспользоваться методом модели `findByIdAndDelete` и передать в него аргументом `id` удаляемого элемента. Процесс работы с MongoDB асинхронный, и для обработки возможных ошибок необходимо использовать блок `try/catch` 👇🏻

```javascript
// Файл middlewares/games.js

const deleteGame = async (req, res, next) => {
  try {
    // Методом findByIdAndDelete по id находим и удаляем документ из базы данных
    req.game = await games.findByIdAndDelete(req.params.id);
    next();
  } catch (error) {
    res.setHeader("Content-Type", "application/json");
		res.status(400).send(JSON.stringify({ message: "Ошибка удаления игры" }));
  }
};
```

## Шаг 3

После удаления игры из БД остаётся передать клиенту результат выполнения операции. Для этого сформируй подходящий контроллер `sendGameDeleted` 👇🏻

```javascript
// Файл controllers/games.js

const sendGameDeleted = (req, res) => {
	// Объект игры отправляем в формате JSON 
  res.setHeader("Content-Type", "application/json");
  // Отправляем на клиент найденный и удалённый элемент из базы данных
  res.end(JSON.stringify(req.game));
};
```

В результате успешного удаления клиент получит объект с игрой и сможет синхронизировать состояние приложения.

## Шаг 4

Описав все необходимые функции, импортируй их в роут и дополни обработчик `delete` 👇🏻 

```javascript
// Файл routes/games.js

gamesRouter.delete(
  "/games/:id", // Слушаем запросы по эндпоинту
  deleteGame,
  sendGameDeleted // Тут будут функция удаления элементов из MongoDB и ответ клиенту
);
```

### Самостоятельная работа 📝

Опиши роуты для удаления пользователей и категорий игр.

Для пользователей `usersRouter.delete("/users/:id", deleteUser, sendUserDeleted);` 👇🏻

- Добавь миддлвар с использованием метода модели `findByIdAndDelete`, передав аргументом `id` пользователя.
- Верни удалённого пользователя `req.user` в качестве ответа на запрос.

Для категорий `categoriesRouter.delete("/categories/:id", deleteCategory, sendCategoryDeleted);` 👇🏻

- Добавь миддлвар с использованием метода модели `findByIdAndDelete`, передав аргументом `id` категории.
- Верни удалённого пользователя `req.category` в качестве ответа на запрос.