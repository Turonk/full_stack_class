# Внешние стейт-машины. Zustand

URL: https://practicum.yandex.ru/learn/kids-web/courses/232ea8d5-ae43-4072-aa39-ade914d25935/sprints/190124/topics/7fa40fdd-1d01-45f2-8cd5-271295dfecfc/lessons/d8edeb84-8b53-46c4-b537-11b6162471bc/

Course: Применение реактивного фреймворка

Topic: Внешние менеджеры состояний

Type: web

---

# Внешние стейт-машины. Zustand

Да! Поэтому разработчики придумали библиотеки для хранения глобальных состояний и управления ими.

Эти библиотеки называют **менеджерами состояния** (или **стейт-менеджерами**, или **стейт-машинами**). Они позволяют описывать состояние в отдельном файле и обходиться без лишних контекстов-обёрток.

Первой библиотекой для управления состояниями был **[Redux](https://redux.js.org/){target="_blank"}**. У этой библиотеки сравнительно сложный синтаксис, и для её применения нужно будет хорошенько попотеть и исписать не один десяток строчек кода. Но не будем скрывать: она всё ещё часто используется во многих крупных проектах. В документации Redux даже есть [раздел](https://redux.js.org/introduction/getting-started#should-you-use-redux){target="_blank"}, в котором предлагается взвесить все за и против перед юзанием этого стейт-менеджера. 

Со временем стали появляться и другие библиотеки для хранения состояний, с помощью которых пытались упростить работу с глобальным стейтом.

![](https://pictures.s3.yandex.net:443/resources/IMG_4721_2_1709559261.jpg)

### Подготовка к работе с Zustand

В этом уроке мы будем использовать для Pindie сравнительно простую библиотеку [**Zustand**](https://docs.pmnd.rs/zustand/getting-started/introduction){target="_blank"} (с немецкого — «состояние»). Это внешняя библиотека, поэтому её надо установить в проект с помощью `npm` (про `npm` мы подробнее рассказывали в уроке «Фреймворки и магазин разработчиков NPM»). Для этого введи команду `npm install zustand` в консоли, в той папке, где хранится код Pindie. 

Например, если Pindie лежит в папке `pindie`, тебе нужно ввести следующие две команды: 👇🏻

```bash
cd pindie #Выбираем папку, где лежит код проекта
npm install zustand #Устанавливаем Zustand
```

Ты можешь проверить, установилась ли библиотека, открыв файл `package.json`. Если в `dependencies` появилась запись `"zustand": "^4.5.0"`, всё в порядке и Zustand готов к использованию.

![](https://pictures.s3.yandex.net:443/resources/Frame_1565_1709559300.png)

### Хранилище состояний

В Zustand хранилище состояний (это хранилище иногда называют **стор**, с английского store — «хранилище») работает как реакт-хук (о хуках в React мы рассказывали в уроке «Хуки и особенные события»).

Сегодня мы научимся переносить в хранилище данные, которые на прошлом уроке записывали в контекст приложения в файле `App.jsx`

**Шаг 1. Создание хранилища**

В случае с Pindie создай папку `/app/store` и в ней отдельный файл `app-store.js`. Для создания хука-хранилища (назовём его `useStore`) используй функцию `create` библиотеки Zustand. Её нужно импортировать из библиотеки Zustand и записать в константу `useStore`, которую экспортируешь из файла. Используй для этого ключевые слова `import` и `export` (мы говорили о них подробно в уроке «Модули и ключевые слова `export` и `import`»).

```javascript
import { create } from 'zustand';

export const useStore = create();
```

Функция `create` принимает как аргумент функцию такого вида: `(set) => ({})`. Она возвращает объект, в котором хранятся данные о состояниях и функции для обновления этих состояний. Параметр `set` — функция, которая используется для обновления стейта.

**Шаг 2. Наполнение хранилища**

Перед тем как наполнить твоё хранилище для Pindie, давай разберём, как это работает, на простом примере. Хранилище, в котором есть значение счётчика `counter`, изначально равное нулю, выглядит так 👇🏻

```javascript
export const useStore = create((set) => ({
  /* Изначальное значение */
  counter: 0
})); 
```

Теперь, чтобы показывать значение счётчика, достаточно вызвать хук `useStore` в нужном компоненте 👇🏻

```javascript
import { useStore } from "@/app/store/app-store";

function Counter = () => {
  const store = useStore();

  return (
    <div>
      <p>{store.counter}</p>
    <div>
  )
}
```

Но как изменять это значение? Если пытаться перезаписать значение из хранилища в том же компоненте, где мы используем счётчик, ничего не получится 👇🏻

```javascript
import { useStore } from "@/app/store/app-store";

function WrongCounter = () => {
  const store = useStore();

  return (
    <div>
      <p>{store.counter}</p>
      {/* Нажатие на эту кнопку не будет менять значение store.counter */}
      <button onClick={() => {store.counter = store.counter + 1}}>
        +1
      </button>
    <div>
  )
}
```

Для записи нового состояния хранилища как раз и нужна функция `set`. Добавь в хранилище функцию `increment`, которая будет увеличивать значение на один 👇🏻

```javascript
export const useStore = create((set) => ({
    /* Изначальное значение */
    counter: 0,
    /* Параметр state в функции set — нынешнее состояние хранилища */
    increment: () => set((state) => ({ counter: state.counter + 1 })),
})); 
```

А вот как использовать функцию `increment` в компоненте `Counter` 👇🏻

```javascript
import { useStore } from "@/app/store/app-store";

function Counter = () => {
  const store = useStore();

  return (
    <div>
      <p>{store.counter}</p>
      {/* Нажатие на эту кнопку будет менять значение store.counter */}
      <button onClick={store.increment}>
        +1
      </button>
    <div>
  )
}
```

### Наполнение Pindie

Вернёмся к Pindie и хранилищу, которое создали ранее в файле `app/store/app-store.js`

Добавь в хранилище три изначальных состояния: 

- `isAuth` (авторизовался ли пользователь): `false`
- `user` (данные пользователя): `null`
- `token` (`JWT`-токен пользователя): `null`

```javascript
import { create } from 'zustand';

export const useStore = create((set) => ({
  isAuth: false,
  user: null,
  token: null,
}));
```

Теперь в хранилище нужно добавить функцию `login`, которая будет обновлять состояние приложения после авторизации пользователя. Эта функция принимает параметры `user` и `token`. Состояние `isAuth` должно меняться на `true`. Значение `user` будет записываться в состояние `user`, а значение `token` — в `token`

А ещё нужно записать переданный токен в `localStorage` — для этого воспользуйся функцией `setJWT` из файла `'../api/api-utils'` (о работе с `JWT`-токенами мы говорили в уроке «Запросы с JWT-токеном и его хранение»).

```javascript
import { create } from 'zustand';
import { setJWT } from '../api/api-utils';

export const useStore = create((set) => ({
  isAuth: false,
  user: null,
  token: null,
  login: (user, token) => {
    /* С помощью функции set устанавливаем новое состояние хранилища */
    set({ isAuth: true, user, token });
    /* Записываем полученный токен */
    setJWT(token);
  },
}));
```

Да, в результате вызова функции `logout` все состояния должны сбрасываться к изначальному, а `JWT`-токен — удаляться.

```javascript
import { create } from 'zustand';
import { setJWT, removeJWT } from '../api/api-utils';

export const useStore = create((set) => ({
  isAuth: false,
  user: null,
  token: null,
  login: (user, token) => {
    /* С помощью функции set устанавливаем новое состояние хранилища */
    set({ isAuth: true, user, token });
    /* Записываем полученный токен */
    setJWT(token);
  },
  logout: () => {
    /* Возвращаем изначальные состояния */
    set({ isAuth: false, user: null, token: null });
    /* Удаляем токен */
    removeJWT();
  },
}));
```

Отлично! Стор почти готов — осталось только добавить функцию `checkAuth`, которая будет проверять, что пользователь авторизован. В прошлом уроке мы уже писали подобную функцию в файле `App.jsx` — теперь она будет обновлять состояния в хранилище после проверки `JWT`-токена у пользователя или удалять их, если токен не найден 👇🏻

```javascript
import { create } from 'zustand';
import { getJWT, setJWT, removeJWT, getMe } from '../api/api-utils';
import { endpoints } from '../api/config';

export const useStore = create((set) => ({
  isAuth: false,
  user: null,
  token: null,
  login: (user, token) => {
    /* С помощью функции set устанавливаем новое состояние хранилища */
    set({ isAuth: true, user, token });
    /* Записываем полученный токен */
    setJWT(token);
  },
  logout: () => {
    /* Возвращаем изначальные состояния */
    set({ isAuth: false, user: null, token: null });
    /* Удаляем токен */
    removeJWT();
  },
  checkAuth: async () => {
    const jwt = getJWT();
    if (jwt) {
      const user = await getMe(endpoints.me, jwt);
      if (user) {
        /* Сохраняем полученные данные и токен */
        set({ isAuth: true, user, token: jwt });
        setJWT(jwt);
      } else {
        /* Возвращаем изначальные состояния и удаляем токен */
        set({ isAuth: false, user: null, token: null });
        removeJWT();
      }
    } else {
      set({ isAuth: false, user: null, token: null });
    }
  },
}));
```

Да, Аски, из файла `App.jsx` теперь можно удалять все переменные состояния и обёртку-контекст. Оставить в нём следует только эффект для проверки: авторизован пользователь или нет. Для этого воспользуйся записанной в хранилище функцией `checkAuth`

```javascript
'use client';

import { Header } from './components/Header/Header';
import { Footer } from './components/Footer/Footer';

import { useEffect } from 'react';

import { useStore } from './store/app-store';

export const App = (props) => {
  /* Используем хук-хранилище */
  const store = useStore();

  useEffect(() => {
  /* 
    Проверяем, авторизован ли пользователь, 
    функцией checkAuth из хранилища 
  */
    store.checkAuth();
  }, []);

  return (
    <>
      <Header />
      {props.children}
      <Footer />
    </>
  ) 
};
```

Во всех файлах, где в `authContext` записывался контекст, запись `const authContext = useContext(AuthContext)` нужно заменить на `const authContext = useStore()`. Тогда вместо объекта с данными из контекста в переменной `authContext` будут доступны значения из хранилища и функции для их изменения. Так что, если сохранить те же названия состояний и функций, всё должно заработать автоматически при использовании хранилища состояний.

Лови! Раньше в шапке сайта мы писали функцию для логаута `handleLogout`, получая `authContext` из контекста 👇🏻

```javascript
import { useContext } from "react";
import { AuthContext } from "@/app/context/app-context";

export const Header = () => {
  // Сохраняем в authContext контекст
  const authContext = useContext(AuthContext);

  const handleLogout = () => {
    authContext.logout(); // Используем метод logout из контекста
  };

  return (
    <header className={Styles["header"]}>
      {/* JSX-код компонента */}
    </header>
  );
}
```

Теперь, если функция `logout` сохранила своё название, она продолжает быть доступна и при использовании хранилища 👇🏻

```javascript
import { useStore } from "@/app/store/app-store";

export const Header = () => {
  // Сохраняем в authContext хук-хранилище
  const authContext = useStore();

  const handleLogout = () => {
    authContext.logout(); // Используем метод logout из хранилища
  };

  return (
    <header className={Styles["header"]}>
    {/* JSX-код компонента */}
    </header>
  );
};
```