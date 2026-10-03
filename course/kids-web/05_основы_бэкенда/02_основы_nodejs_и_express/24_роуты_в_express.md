# Роуты в Express

URL: https://practicum.yandex.ru/learn/kids-web/courses/fca180a1-4dc7-4494-818a-9536e5cf7aeb/sprints/190125/topics/d034b6b4-f9ec-479f-ab65-1b8b1b769e5d/lessons/d040a779-3235-4282-8628-0d68bc8aee16/

Course: Основы бэкенда

Topic: Основы Node.js и Express

Type: web_server

---

# Роуты в Express

{video:https://code.s3.yandex.net/kids-web/vids/aski_rout.mp4}

Начнём с обработки знакомого тебе `GET`-запроса — другие типы рассмотрим чуть позже.

### Роутинг `GET`-запроса

Для обработки `GET`-запроса в экспрессе существует метод `get`, который принимает на вход два аргумента:

- строку с запросом
- колбэк-функцию, предписывающую, что нужно делать, если такой запрос пришёл на сервер

Лови пример реализации 👇🏻

```javascript
app.get('/', (req, res) => {
	// Логика обработки запроса
});
```

Параметры колбэк-функции — объекты запроса и ответа.

### Объект ответа

У объекта ответа есть метод `send`. Параметром ему передают информацию, которую нужно отправить пользователю, например веб-страницу 👇🏻

```javascript
app.get('/', (req, res) => {
  res.send(
		`<html>
		<body>
		    <p>Ответ на сигнал из далёкого космоса</p>
		</body>
		</html>`
	);
});
```

Метод `send` может принимать разные данные в качестве аргумента 👇🏻

```javascript
res.send('Немного текста');
res.send('<p>Немного html</p>');
res.send({ some: 'json' });
```

Кроме отправки ответа, метод автоматически выставит заголовок `Content-Type` в соответствии с аргументом, который ему передали 👇🏻

```javascript
res.send('Немного текста'); // Content-Type: text/plain
res.send('<p>Немного html</p>'); // Content-Type: text/plain
res.send({ some: 'json' }); // Content-Type: application/json
```

По умолчанию `send` отправляет ответ со статусом `200`. Его можно изменить методом `status` 👇🏻

```javascript
app.get('/', (req, res) => {
  res.status(404);
  res.send('<h1>Страница не найдена</h1>');
});
```

Обрати внимание, что `status` устроен так, что его и `send` можно использовать по цепочке. Обычно разработчики так и делают 👇🏻

```javascript
app.get('/', (req, res) => {
  res.status(404).send('<h1>Страница не найдена</h1>');
});
```

{quiz-task}
    background: |
        #f1f1ef
    content: |
        📚 Со статус-кодами ты можешь познакомиться в [документации](https://developer.mozilla.org/ru/docs/Web/HTTP/Status){target="_blank"}. Важно присваивать разным ошибкам соответствующие статус-коды. Это нужно для правильной работы любого приложения.

        Для других методов работы объекта ответа рекомендуем заглянуть вот в [эту документацию](http://expressjs.com/ru/api.html#res){target="_blank"}.
{/quiz-task}

### Объект запроса

Запрос содержит информацию о том, что нужно пользователю. Она может быть организована по-разному: например, в `GET`-запросе данные пользователя упакованы в строку, которая хранится в свойстве `query` объекта запроса. Это те самые параметры, которые прикрепляются в `url` запроса. Они часто встречаются на популярных сайтах 👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1693_1712855894.png)

Тебе уже приходилось работать с ними, когда в Pindie запрашивали набор карточек по категории. Вспоминай 👇🏻

```javascript
  // Склеиваем строку запроса из url и query параметра 
  const data = await getData(`${url}?categories.name=${category}`)
```

Эти параметры как раз хранятся в `req.query` 👇🏻

```javascript
app.get('/', (req, res) => {
  res.send(req.query);
});
```

### Обработка методов в express

HTTP-метод запроса определяет, что делать с ресурсом. В REST применяются пять основных методов:

- `GET` — получает ресурсы
- `POST` — создаёт ресурс
- `PUT` — целиком заменяет существующий ресурс
- `PATCH` — частично изменяет существующий ресурс
- `DELETE` — удаляет ресурс

Реже применяют ещё 2 метода:

- `HEAD` — позволяет получить только заголовки ответа; похож на `GET`, но у его ответа нет тела
- `OPTIONS` — позволяет узнать, какие HTTP-методы поддерживает сервер

В экспрессе есть методы для обработки любого запроса. 

Они называются так же, как соответствующие HTTP-методы, и могут быть вызваны в приложении, где им в качестве параметров будут переданы эндпоинты и функции-обработчики 👇🏻

```javascript
app.get('/games', getAllGames);
app.post('/games', updateGamesArray);
app.put('/games', replaceGame);
app.patch('/games', updateGameInfo);
app.delete('/games', deleteGame);
```

## Что такое динамические роуты

Раньше в Pindie мы писали статические роуты, они обрабатывали запросы на конкретные адреса: `/`, `/games`, `/users/me`

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ **Динамический роут** — это обработчики шаблона адреса. 
        То есть сразу всех адресов, подходящих под определённое правило.
{/quiz-task}

Чтобы создать динамический роут, в `url` укажи двоеточие и имя свойства, которое может меняться, — похожую механику мы делали с тобой в прошлом модуле в Pindie для страницы с детальным описанием игры 👇🏻

```javascript
app.get('/games/:id', (req, res) => { 
	// Этот код обработает все запросы, чей путь начинается с /games/1
});
```

Обрати внимание: значение переменной в адресе не может быть пустым. Вот такой запрос не будет обработан 👇🏻

```bash
http://localhost:3000/games
```

## Параметры роута

Обработать запрос мало — необходимо получить его параметры, чтобы отдавать пользователю нужные данные. В экспрессе это просто: все параметры запроса становятся свойствами JSON-объекта `req.params`

Лови код 👇🏻

```javascript
app.get('/games/:id', (req, res) => {
  res.send(req.params);

	/* Если отправить запрос на адрес http://localhost:3000/games/123,
	 внутри объекта req.params окажется JSON-объект:
	 { "id": "123" } */
});
```

Формат JSON оказывается тут как никогда кстати. Особенно при обработке адресов со множественной вложенностью. Если бы в описании игры были дополнительные разделы с контентом, то их обрабатывали бы примерно так 👇🏻

```javascript
app.get('/games/:id/albums/:album/:photo', (req, res) => {
  const { id, album, photo } = req.params;

	/* При обращении к адресу http://localhost:3000/games/123/albums/333/2
	 параметры запроса будут записаны в таком виде:
	 {"id":"123","album":"333","photo":"2"}

	 Мы записали их в переменные id, album и photo */

  res.send(`Мы на странице игры с id ${id}, смотрим альбом №${album} и фотографию №${photo}`);
});
```

## Как организовать роутинг

Мы уже не раз говорили о преимуществах модульного кода, предлагаем логику роутинга тоже разнести по разным файлам. Пусть один отвечает за основную часть сайта, второй — за админку, третий — за мобильное приложение.

Держи пример того, как разбить код на модули 👇🏻

```javascript
// Здесь функциональность точки входа
const express = require('express');

const PORT = 3000;
const app = express();

// Здесь данные
const games = [
  { 
    id: 1,
	  title: "Crystal Keeper",
	  description: "Управляй боевым дроном, чтобы любой ценой защитить кристалл от враждебных космо-слизней."
  },
  { 
    id: 2,
    title: "Dangeons'n'Caves. Prologue", 
    description: "Безымянный герой исследует пещеры и подземелья, чтобы найти больше информации о себе."
  },
];

// Здесь роутинг
app.get('/games/:id', (req, res) => {
  if (!games[req.params.id]) {
    res.send(`Такой игры не существует`);

    // Не забудем выйти из функции
    return;
  }

  const { title, description } = users[req.params.id];
  
  res.send(`Новое издание игры - ${name}, откроет для вас новый мир: ${description}`);
});

app.listen(PORT, () => {
  console.log(`Server is running at PORT http://localhost:${PORT}`);
});
```

Первым делом перенеси данные об играх в отдельный файл — `games.json`. В твоём проекте их будет больше, чем в примере выше, а храниться они будут в формате JSON 👇🏻

```javascript
// games.json
[
  {
    "id": 1,
    "title": "Crystal Keeper",
    "description": "Управляй боевым дроном, чтобы любой ценой защитить кристалл от враждебных космо-слизней.",
    "image": "https://code.s3.yandex.net/teens/pindie-games/cristal-keeper/cover.png",
    "link": "https://code.s3.yandex.net/teens/pindie-games/cristal-keeper/game/index.html"
  },
  {
    "id": 2,
    "title": "Dangeons'n'Caves. Prologue",
    "description": "Безымянный герой исследует пещеры и подземелья, чтобы найти больше информации о себе.",
    "image": "https://code.s3.yandex.net/teens/pindie-games/dangeons-n-caves-prologue/cover.png",
    "link": "https://code.s3.yandex.net/teens/pindie-games/dangeons-n-caves-prologue/game/index.html"
  }
]

```

Воспользуйся вспомогательными функциями для чтения и записи данных в JSON-файл 👇🏻

```javascript
const fs = require("fs").promises;

const readData = async url => {
  try {
    const data = await fs.readFile(url, "utf-8");
    const json = JSON.parse(data);
    return json;
  } catch (error) {
    console.log(error);
  }
};

const writeData = async (url, data) => {
  const json = JSON.stringify(data);
  await fs.writeFile(url, json);
};
```

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ В твоём проекте они должны располагаться отдельно в папках `utils/data` 👇🏻

        [utils.zip](https://code.s3.yandex.net/kids-web/vids/M4/utils.zip){target="_blank"}
{/quiz-task}

Итак, лови инструкцию, как за два шага из приложения сделать сервер, который будет обрабатывать запросы👇🏻

## **Шаг 1. Настрой роутеры**

Как Аски уже успел сказать, код роутинга лучше хранить в отдельном файле, но для этого сначала допишем его. 

Логика ответа на запросы описана в обработчиках `get`. Мы вызывали `get` как метод самого приложения, то есть метод переменной `app`, но в отдельном модуле с роутингом этой переменной нет. И создать её не получится, так как может быть только одно приложение. Поэтому в экспрессе есть спецметод `Router`, который создаёт объект, идеально подходящий для того, чтобы повесить на него обработчики. 

Создай папку `routes`, а в ней файл `games.js`, в котором и опишешь логику для входящих запросов 👇🏻

```javascript
// routes/games.js
const gamesRouter = require("express").Router(); // Создали роутер
const { readData, writeData } = require("../utils/data"); // Чтение и запись данных в JSON-файл

// Получим игры из JSON-файла и отправим в ответ на запрос
const getAllGames = async (req, res) => {
  const games = await readData("./data/games.json");
  if (!games) {
    res.status(400);
    res.send({
      status: "error",
      message: "Нет игр в базе данных. Добавьте игру."
    });
    return;
  }
  req.games = games;
  res.send(req.games);
};

const deleteGame = async (req, res) => {
	// Получим данные из файла
  const games = await readData("./data/games.json");
  if (!games) {
    res.status(400);
    res.send({
      status: "error",
      message: "Нет игр в базе данных. Добавьте игру.",
    });
    return;
  }
  req.games = games;
  
  // Прочитаем запрашиваемый id игры из запроса
	const id = Number(req.params.id);
	
	// Найдём игру, которую хотят удалить, в общем массиве с играми по id
	req.game = req.games.find((item) => item.id === id);
	
	// Найдём индекс удаляемой игры в общем массиве игр
	const index = req.games.findIndex((item) => item.id === req.game.id);
	
	// Удалим из массива игр игру
	req.games.splice(index, 1);
	
	// Запишем обновлённый массив игр в JSON-файл
	await writeData("./data/games.json", req.games);
	
	// Вернём ответ о проделанной операции с данными об играх
	res.send({
    games: req.games,
    updated: req.game
  });
}

gamesRouter.get("/games", getAllGames)
gamesRouter.delete("/games/:id", deleteGame);

module.exports = gamesRouter;
```

А пока создай ещё один небольшой роут для запроса по маршруту `"/"`. В той же папке `routes` добавь `main.js` 👇🏻

```javascript
// routes/main.js
const mainRoute = require("express").Router();

mainRoute.get("/", (req, res) => {
  res.status(200).send('<h1>Скоро тут будет интерфейс</h1>');
});

module.exports = mainRoute;
```

## **Шаг 2. Настрой точку входа**

Для этого импортируй роутеры в `app.js` и запусти их методом `use`. Так как до этого мы описали, какие методы и `url`-запросы необходимо обрабатывать, достаточно просто передать `mainRoute` и `gamesRouter` аргументами в метод `use` 👇🏻

```javascript
// app.js 
const express = require('express');

// Импортируем роутеры
const mainRoute = require('./routes/main');
const gamesRouter = require('./routes/games'); 

const PORT = 3000;
const app = express();

// Запускаем
app.use(mainRoute, gamesRouter); 

app.listen(PORT, () => {
  console.log(`Server is running at PORT http://localhost:${PORT}`);
})
```