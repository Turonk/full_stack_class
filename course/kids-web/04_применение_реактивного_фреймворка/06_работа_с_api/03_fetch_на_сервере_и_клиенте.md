# Fetch на сервере и клиенте

URL: https://practicum.yandex.ru/learn/kids-web/courses/232ea8d5-ae43-4072-aa39-ade914d25935/sprints/190124/topics/bc79c275-9228-450f-a1d7-3eab285e7058/lessons/0baa08b9-9663-40e1-bac2-ab7a6e75d6df/

Course: Применение реактивного фреймворка

Topic: Работа с API

Type: web

---

# Fetch на сервере и клиенте

![](https://pictures.s3.yandex.net:443/resources/Worn-Ass-Semi-Gloss_54_1708938069.jpg)

### `fetch` в серверных компонентах: `"u**se server**"`

В серверных компонентах легко описать и вызвать асинхронную функцию. 

Проиллюстрируем файлом `page.js` из Pindie. 

Сейчас компонент `Home` обрабатывается на сервере (по умолчанию все компоненты серверные) и загрузку данных можно осуществить в нём 👇🏻

```javascript
import { getGamesByCategory } from "./data/data-utils";
import { Banner } from "./components/Banner/Banner";
import { CardsList } from "./components/CardsList/CardsList";
import { Promo } from "./components/Promo/Promo";

export default function Home() {
  const popularGames = getGamesByCategory("popular");
  const newGames = getGamesByCategory("new");
  return (
    <main className="main">
      <Banner />
      <CardsList id="popular" title="Популярные" data={popularGames} />
      <CardsList id="new" title="Новинки" data={newGames} />
      <Promo />
    </main>
  );
}
```

Запишем асинхронную функцию `getData` для получения данных по `url` 👇🏻

```javascript
import { getGamesByCategory } from "./data/data-utils";
import { Banner } from "./components/Banner/Banner";
import { CardsList } from "./components/CardsList/CardsList";
import { Promo } from "./components/Promo/Promo";

export const getData = async (url) => {
  try {
    const response = await fetch(url)
    if (response.status !== 200) {
      throw new Error('Ошибка получения данных')
    }
    const data = await response.json()
    return data
  } catch (error) {
    return error
  }
}

export default function Home() {
  const popularGames = getGamesByCategory("popular");
  const newGames = getGamesByCategory("new");
  return (
    <main className="main">
      <Banner />
      <CardsList id="popular" title="Популярные" data={popularGames} />
      <CardsList id="new" title="Новинки" data={newGames} />
      <Promo />
    </main>
  );
}
```

В компоненте `Home` создадим переменную `dataFromUrl` для хранения данных, полученных с помощью функции `getData`

Присвоим в переменную результат вызова функции `getData`. Так как функция асинхронная и нужно дождаться её выполнения, укажем ключевое слово `await` 👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1540_1_1708938100.png)

Сверху VSC подчеркивает `await` как ошибку, потому что использовать его можно только в асинхронных функциях с ключевым словом `async`. Поэтому важно указать `async` для функции `Home` (как снизу).

Теперь при запросе к нашему сайту на сервере предварительно произойдёт запрос и полученные данные сохранятся в переменную `dataFromUrl`. В этом можно убедиться с помощью `console.log(dataFromUrl)`. Данные будут выведены в терминал редактора кода 👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1541_1708938113.png)

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ **Важно** **запомнить:** используя асинхронную функцию в серверном компоненте, необходимо прописывать ей ключевое слово `async`
{/quiz-task}

Предварительная загрузка данных полезна:

- Для ускорения загрузки сайта 
Предзагруженные данные на сервере избавляют пользователя от ожидания дополнительной загрузки данных перед просмотром страницы.
- Для улучшения поисковой выдачи 
Поисковые системы Яндекса, Google и других сервисов могут точнее определять контент сайта, а значит, более точно отображать его в поисковой выдаче.
- Для улучшения производительности сайта 
Снижая нагрузку с клиента (уменьшение количества запросов, дополнительных загрузок и обновлений данных и страниц сайта), мы улучшаем взаимодействие с пользователем.
- Для улучшения безопасности 
Поскольку данные загружаются исключительно на сервере, они остаются недоступными для клиентского браузера.

### `fetch` в клиентских компонентах: `"use client"`

Получение данных на стороне клиента используют для динамических данных: бесконечная лента постов социальной сети, обновление списка комментариев, кнопки лайка или покупки товаров. Такая обработка данных в основном связана со взаимодействием пользователя, обработкой событий и жизненного цикла компонента.

Для использования асинхронных функций в клиентских компонентах тебе понадобится хук `useEffect`. Он позволит загружать необходимые данные в момент монтирования клиентского компонента. 

В качестве примера укажем в компоненте `Home` ключевую фразу `"use client"` и перенесём объявление асинхронной функции и её вызов в хук `useEffect` 👇🏻

```javascript
"use client";
import { getGamesByCategory } from "./data/data-utils";
import { Banner } from "./components/Banner/Banner";
import { CardsList } from "./components/CardsList/CardsList";
import { Promo } from "./components/Promo/Promo";
import { useEffect } from "react";

export default function Home() {
  useEffect(() => {
    const getData = async (url) => {
      try {
        const response = await fetch(url);
        if (response.status !== 200) {
          throw new Error("Ошибка получения данных");
        }
        const data = await response.json();
        console.log(data);
        return data;
      } catch (error) {
        return error;
      }
    };
    getData("https://api-code-2.practicum-team.ru/games");
  }, []);

  const popularGames = getGamesByCategory("popular");
  const newGames = getGamesByCategory("new");

  return (
    <main className="main">
      <Banner />
      <CardsList id="popular" title="Популярные" data={popularGames} />
      <CardsList id="new" title="Новинки" data={newGames} />
      <Promo />
    </main>
  );
}
```

Теперь нет нужды делать компонент асинхронным (указывать `async` перед объявлением функции `Home`), как при работе с асинхронными функциями внутри серверных компонентов. 

Асинхронная функция `getData` будет вызвана в момент монтирования компонента `Home` в браузере пользователя благодаря хуку `useEffect` с пустым массивом зависимостей. 

Для наглядности выведем данные в консоль 👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1543_1708938176.png)

Компонент сначала отрисовывается, и только потом происходит запрос и отображение полученных данных. 

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ **Важно помнить:** работа с большим количеством данных может негативно повлиять на производительность страницы в браузере. Ожидание запросов, обработка данных и отсутствие кэширования результатов делают интерфейс менее отзывчивым.
{/quiz-task}