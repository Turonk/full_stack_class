# Встроенное решение — React Context

URL: https://practicum.yandex.ru/learn/kids-web/courses/232ea8d5-ae43-4072-aa39-ade914d25935/sprints/190124/topics/7fa40fdd-1d01-45f2-8cd5-271295dfecfc/lessons/ec77c33f-aa3e-455f-b707-a6c296c8d0bb/

Course: Применение реактивного фреймворка

Topic: Внешние менеджеры состояний

Type: web

---

# Встроенное решение — React Context

На прошлом уроке мы создали компонент `App`. Это клиентский компонент, который хранит в состоянии данные о пользователе — о том, зарегистрирован ли он, его токен и функции для авторизации на сайте. `App` — компонент-обёртка, как раньше был `RootLayout`, только теперь он хранит общие данные для компонентов сайта и при каждом обновлении проверяет их актуальность 👇🏻

{video:https://code.s3.yandex.net/kids-web/vids/Запись_экрана_2024-02-07_в_18.19.19.mp4|controls:true|autoplay:0|pip:false|controlsList:nodownload}

Чекай, как выглядит `App` в коде👇🏻

{video:https://code.s3.yandex.net/kids-web/vids/Запись_экрана_2024-02-07_в_18.28.09.mp4|controls:true|autoplay:0|pip:false|controlsList:nodownload}

Общие данные мы собрали в одном компоненте, а теперь передадим их дочерним компонентам. 

Мы уже использовали `props` для передачи данных вниз по дереву элементов, но, если данных много или их нужно передать очень глубоко в дереве элементов, это приведёт к проблемам.

![](https://pictures.s3.yandex.net:443/resources/IMG_4717_1709557966.jpg)

### `Props` и как их не пробрасывать

На прошлом уроке мы говорили про концепцию **глобального состояния** — удобный способ независимо хранить данные.

Верно! Есть разные способы реализовать подобное хранилище и взаимодействие с ним. 

В библиотеке React тоже предусмотрен такой механизм, и называется он **React Context**.

Context позволяет родительскому компоненту сделать некоторую информацию доступной для любого компонента в дереве под ним — независимо от глубины, без явной передачи её через `props`. С помощью одной простой функции создаётся хранилище 👇🏻

```javascript
const context = createContext("мой контекст");
```

Аргументом в функцию `createContext` передаётся значение, которое нужно сохранить. В данном примере — строка `"мой контекст"`. Если посмотришь в консоли, как выглядит это хранилище — переменная `context`, то увидишь объект с небольшим количеством полей 👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1563_1709558021.png)

В нём можно найти сохранённое значение `"мой контекст"`, а ещё свойство `Provider` (с англ. «поставщик») — этот механизм обеспечит доступ вложенным компонентам приложения к хранилищу.

Добавим в Pindie контекст для хранения информации об авторизации пользователя.

**Шаг 1. Создание контекста**

В папке `app` создай папку `context`, а в ней — файл `app-context.js`

![](https://pictures.s3.yandex.net:443/resources/Frame_1564_1709558057.png)

В файле достаточно импортировать функцию `createContext` из библиотеки React и с помощью вызова создать переменную `AuthContext` для хранения данных. Единственным аргументом для `createContext` является значение по умолчанию. Укажи `null` — пустое значение, а затем переопредели его данными об авторизации пользователя в корневом компоненте `App` 👇🏻

```javascript
import {createContext} from 'react';

export const AuthContext = createContext(null);
```

**Шаг 2. Предоставление контекста**

Импортируй `AuthContext` в корневой компонент `App`, где хранятся данные об авторизации пользователя 👇🏻

```javascript
import {AuthContext} from './context/app-context';

export const App = (props) => {
  const [isAuth, setIsAuth] = useState(false);
  const [user, setUser] = useState(null);
  const [token, setToken] = useState('');

  const login = (user, token) => {
    setIsAuth(true);
    setUser(user);
    setToken(token);
    setJWT(token);
  };

  const logout = () => {
    setIsAuth(false);
    setUser(null);
    setToken('');
    removeJWT();
  };

return (
	<>
   <Header />
	  {props.children}
	  <Footer />
	</>
	)
};
```

Компоненты, которым необходимо получать доступ к контексту, нужно обернуть в `AuthContext.Provider`, а в параметр `value` указать объект с переменными и ссылками на функции. Так компоненты `Header` и `Footer`, а также все остальные вложенные элементы через `{props.children}` смогут использовать значение `value` 👇🏻

```javascript
<AuthContext.Provider value={{isAuth, user, token, login, logout}}>
  <Header />
  {props.children}
  <Footer />
</AuthContext.Provider>
```

**Шаг 3. Использование контекста**

Вложенные в провайдер `AuthContext.Provider` компоненты могут получить доступ к контексту `value` с помощью хука `useContext`. Как и `useState` и `useReducer`, хук можно вызывать только непосредственно внутри компонента React (не внутри циклов или условий). Вызвав хук `useContext` с переданным в аргументы названием контекста (в нашем случае `AuthContext`), `useContext` сообщает React, что компонент хочет прочитать `AuthContext`. Результат вызова записывают в переменную `authContext` — это и будет значением контекста, тем, что передавали в `value` провайдера 👇🏻

```javascript
import { useContext } from "react";
import { AuthContext } from "@/app/context/app-context";

export const Component = (props) => {
  const authContext = useContext(AuthContext);
  return (
    <>
      {!AuthContext.isAuth && <button onClick="() => authContext.login()">}
    </>
  )
}
```

В переменной `authContext` сохранён объект с ключами: `isAuth`, `user`, `token`, `login`, `logout`. Поэтому, обращаясь к `authContext` через точку, можно получить значения этих ключей и использовать их в JSX-разметке.

## Контекст в Pindie

Контекст поможет избавиться от лишних импортов и дополнительных `props` внутри компонентов. Компоненты станут более независимыми друг от друга, компактными и простыми.

### Шаг 1. Создай контекст

Создай папку `context`, а в ней файл `app-context.js` с кодом 👇🏻

```javascript
import {createContext} from 'react';

export const AuthContext = createContext(null);
```

### Шаг 2. Оберни компоненты в провайдер

Компонент `App` со значением и провайдером уже разобрали, готовый код можно найти под тогглом ниже 👇🏻

```javascript
'use client';

import { Header } from './components/Header/Header';
import { Footer } from './components/Footer/Footer';

import { useState, useEffect } from 'react';
import {AuthContext} from './context/app-context';

import { endpoints } from './api/config';
import { getJWT, setJWT, removeJWT, getMe } from './api/api-utils';

export const App = (props) => {
  const [isAuth, setIsAuth] = useState(false);
  const [user, setUser] = useState(null);
  const [token, setToken] = useState('');

  const login = (user, token) => {
    setIsAuth(true);
    setUser(user);
    setToken(token);
    setJWT(token);
  };

  const logout = () => {
    setIsAuth(false);
    setUser(null);
    setToken('');
    removeJWT();
  };

  const checkAuth = async () => {
    const token = getJWT();
    if(token) {
      const me = await getMe(endpoints.me, token);
      if(me) {
        login(me, token);
      } else {
        logout();
      }
    }
  };

  useEffect(() => {
	  async function check() {
		  await checkAuth();
	  };
	  check();
  }, []);

  return (
    <AuthContext.Provider value={{isAuth, user, token, login, logout}}>
      <Header />
      {props.children}
      <Footer />
    </AuthContext.Provider>
  )
    
};
```

### Шаг 3. Используй контекст в `Header` для кнопки авторизации

```javascript
"use client";

import { useState, useEffect } from "react";

import Styles from "./Header.module.css";
import { Overlay } from "../Overlay/Overlay";
import { Popup } from "../Popup/Popup";
import { AuthForm } from "../AuthForm/AuthForm";

import { endpoints } from "@/app/api/config";
import { getJWT, removeJWT, getMe, isResponseOk } from "@/app/api/api-utils";

import Link from "next/link";
import { usePathname } from "next/navigation";

export const Header = () => {
  const [isAuthorized, setIsAuthorized] = useState(false);
  const [popupIsOpened, setPopupIsOpened] = useState(false);

  const openPopup = () => {
    setPopupIsOpened(true);
  };
  const closePopup = () => {
    setPopupIsOpened(false);
  };

  const pathname = usePathname();
  useEffect(() => {
    const jwt = getJWT();
    if (jwt) {
      getMe(endpoints.me, jwt).then((userData) => {
        if (isResponseOk(userData)) {
          setIsAuthorized(true);
        } else {
          setIsAuthorized(false);
          removeJWT();
        }
      });
    }
  }, []);
  const handleLogout = () => {
    setIsAuthorized(false);
    removeJWT();
  };
  return (
    <header className={Styles["header"]}>
      {pathname === "/" ? (
        <span className={Styles["logo"]}>
          <img
            className={Styles["logo__image"]}
            src="/images/logo.svg"
            alt="Логотип Pindie"
          />
        </span>
      ) : (
        <Link href="/" className={Styles["logo"]}>
          <img
            className={Styles["logo__image"]}
            src="/images/logo.svg"
            alt="Логотип Pindie"
          />
        </Link>
      )}
      <nav className={Styles["menu"]}>
        <ul className={Styles["menu__list"]}>
          <li className={Styles["menu__item"]}>
            <Link
              href="/new"
              className={`${Styles["menu__link"]} ${
                pathname === "/new" && Styles["menu__link_active"]
              }`}
            >
              Новинки
            </Link>
          </li>
          <li className={Styles["menu__item"]}>
            <Link
              href="/popular"
              className={`${Styles["menu__link"]} ${
                pathname === "/popular" && Styles["menu__link_active"]
              }`}
            >
              Популярные
            </Link>
          </li>
          <li className={Styles["menu__item"]}>
            <Link
              href="/shooters"
              className={`${Styles["menu__link"]} ${
                pathname === "/shooters" && Styles["menu__link_active"]
              }`}
            >
              Шутеры
            </Link>
          </li>
          <li className={Styles["menu__item"]}>
            <Link
              href="/runners"
              className={`${Styles["menu__link"]} ${
                pathname === "/runners" && Styles["menu__link_active"]
              }`}
            >
              Ранеры
            </Link>
          </li>
          <li className={Styles["menu__item"]}>
            <Link
              href="/pixel-games"
              className={`${Styles["menu__link"]} ${
                pathname === "/pixel-games" && Styles["menu__link_active"]
              }`}
            >
              Пиксельные
            </Link>
          </li>
          <li className={Styles["menu__item"]}>
            <Link
              href="/tds"
              className={`${Styles["menu__link"]} ${
                pathname === "/tds" && Styles["menu__link_active"]
              }`}
            >
              TDS
            </Link>
          </li>
        </ul>
        <div className={Styles["auth"]}>
          {isAuthorized ? (
            <button className={Styles["auth__button"]} onClick={handleLogout}>
              Выйти
            </button>
          ) : (
            <button className={Styles["auth__button"]} onClick={openPopup}>
              Войти
            </button>
          )}
          
        </div>
      </nav>
      <Overlay isOpened={popupIsOpened} close={closePopup} />
      <Popup isOpened={popupIsOpened} close={closePopup}>
        <AuthForm close={closePopup} setAuth={setIsAuthorized}/>
      </Popup>
    </header>
  );
};
```

В компоненте `App` хранятся данные о пользователе, его статусе авторизации, а самое главное — методы `login` и `logout`. Их будем получать из контекста.

В этом компоненте больше не понадобится использовать JWT-методы и данные `api`, поэтому смело удаляй импорты 👇🏻

```javascript
import { endpoints } from "@/app/api/config";
import { getJWT, removeJWT, getMe, isResponseOk } from "@/app/api/api-utils";
```

Благодаря переменным контекста больше всё это тебе не пригодится 👇🏻

```javascript
const [isAuthorized, setIsAuthorized] = useState(false);

useEffect(() => {
  const jwt = getJWT();
  if (jwt) {
    getMe(endpoints.me, jwt).then((userData) => {
      if (isResponseOk(userData)) {
        setIsAuthorized(true);
      } else {
        setIsAuthorized(false);
        removeJWT();
      }
    });
  }
}, []);

// Перепишем с использованием функции из контекста
const handleLogout = () => {
  setIsAuthorized(false);
  removeJWT();
};
```

Да, первым делом импортируй в компонент хук `useContext` и сам контекст `AuthContext` 👇🏻

```javascript
import { useContext } from "react";
import { AuthContext } from "@/app/context/app-context";
```

Внутри компонента вызывай хук `useContext` и сохраняй полученное значение в переменную `authContext` 👇🏻

```javascript
const authContext = useContext(AuthContext);
```

Клик по кнопке `Войти` открывает всплывающее окно — компонент `Popup`. А клик по кнопке с надписью `Выйти` должен разлогинить пользователя, для этого в контексте из компонента `App` передай функцию `logout`. Перепиши обработчик клика `handleLogout` 👇🏻

```javascript
export const Header = () => {

  const authContext = useContext(AuthContext);

  const handleLogout = () => {
    authContext.logout(); // Метод logout из контекста
  };

  return (
    <header className={Styles["header"]}>
      {/* JSX-код компонента */}
    </header>
  );
}
```

Осталось использовать значения из контекста в JSX-разметке компонента `Header` для кнопки авторизации 👇🏻

```javascript
<div className={Styles["auth"]}>
  {/* Определяем, авторизован ли пользователь */}
  {authContext.isAuth ? ( 
    <button className={Styles["auth__button"]} onClick={handleLogout}>
      Выйти
    </button>
    ) : (
    <button className={Styles["auth__button"]} onClick={openPopup}>
      Войти
    </button>
  )}
</div>
```

Используй отображение кнопки по условию: для этого определяй, авторизован ли пользователь, переменной из контекста `authContext.isAuth` и используй обработчик клика `handleLogout` для кнопки `Выйти`. Всё как на видео 👇🏻

{video:https://code.s3.yandex.net/kids-web/vids/Мои_проект_(3).mp4|controls:true|autoplay:0|pip:false|controlsList:nodownload}

### Шаг 4. Используй контекст в компоненте формы для регистрации `AuthForm`

Сохранение данных о зарегистрированном пользователе, а также сохранение токена будут происходить в методе `login`, который получим из контекста. Поэтому в компоненте `AuthForm` больше не понадобится использовать `JWT` и состояние для данных пользователя `userData` , удаляй👇🏻

```javascript
import { setJWT } from "@/app/api/api-utils";

const [userData, setUserData] = useState(null);
```

Импортируй хук и контекст 👇🏻

```javascript
import { useContext } from "react";
import { AuthContext } from "@/app/context/app-context";
```

Внутри компонента получишь значение из контекста 👇🏻

```javascript
export const AuthForm = (props) => {
  const authContext = useContext(AuthContext);
  // Остальной код компонента...
}
```

В обработчике `handleSubmit` перепиши три строчки кода с авторизацией пользователя на `authContext.login(userData.user, userData.jwt)` 👇🏻

```javascript
const handleSubmit = async (e) => {
  e.preventDefault();
  const userData = await authorize(endpoints.auth, authData);
  if(isResponseOk(userData)) {
    authContext.login(userData.user, userData.jwt); // login из контекста
    setMessage({ status: "success", text: "Вы авторизовались!" });
  } else {
    setMessage({ status: "error", text: "Неверные почта или пароль" });
  }
};
```

В хуке `useEffect` вместо `userData` используй значение из контекста `authContext.user` 👇🏻

```javascript
useEffect(() => {
  let timer; 
  if(authContext.user) { // Данные о user из контекста
    timer = setTimeout(() => {
      setMessage({ status: null, text: null});
      props.close();
    }, 1000);
  }
  return () => clearTimeout(timer);
}, [authContext.user]); // Данные о user из контекста
```

На этом форма авторизации готова. Скринкаст со всем вышеописанным для подстраховки 👇🏻

{video:https://code.s3.yandex.net/kids-web/vids/Мои_проект_(3)_2.mp4|controls:true|autoplay:0|pip:false|controlsList:nodownload}

### Шаг 5. Используй контекст в `GamePage`

В этом компоненте больше не понадобится использовать функции, связанные с авторизацией и токеном, поэтому со спокойной душой убирай импорты для `getJWT`, `removeJWT`, `getMe`

Удали пару переменных состояния и проверку токена 👇🏻

```javascript
const [isAuthorized, setIsAuthorized] = useState(false);
const [currentUser, setCurrentUser] = useState(null);

const jwt = getJWT();
if (jwt) {
	getMe(endpoints.me, jwt).then((userData) => {
	  if (isResponseOk(userData)) {
	    setIsAuthorized(true);
      setCurrentUser(userData);
    } else {
      setIsAuthorized(false);
      removeJWT();
    }
  });
}
```

Теперь импортируй хук и контекст 👇🏻

```javascript
import { useContext } from "react";
import { AuthContext } from "@/app/context/app-context";
```

Внутри компонента получишь значение из контекста 👇🏻

```javascript
export default function GamePage(props) {
  const authContext = useContext(AuthContext);
	// Остальной код компонента...
}
```

Перепиши хуки `useEffect` с использованием контекста 👇🏻

```javascript
useEffect(() => {
  async function fetchData() {
	  setPreloaderVisible(true);
    const game = await getNormalizedGameDataById(
      endpoints.games,
      props.params.id
    );
    isResponseOk(game) ? setGame(game) : setGame(null);
    setPreloaderVisible(false);
  }
  fetchData();
}, []);
  
useEffect(() => { // Данные о пользователе получаем из контекста authContext.user
	authContext.user && game ? setIsVoted(checkIfUserVoted(game, authContext.user.id)) : setIsVoted(false);
}, [authContext.user, game]);
```

И измени функцию с использованием переменных их контекста 👇🏻

```javascript
const handleVote = async () => {
	const jwt = authContext.token; // Данные о токене получаем из контекста
  let usersIdArray = game.users.length
	  ? game.users.map((user) => user.id)
    : [];
  usersIdArray.push(authContext.user.id); // Данные о пользователе получаем из контекста
  const response = await vote(
	  `${endpoints.games}/${game.id}`,
    jwt,
    usersIdArray
  );
  if (isResponseOk(response)) {
	  setGame(() => {
	    return {
	      ...game,
        // Данные о пользователе получаем из контекста
        users: [...game.users, authContext.user],
      };
    });
		setIsVoted(true);
  }
```

Замени в JSX-разметке отображение кнопки 👇🏻

```javascript
// Заменим isAuthorized на authContext.isAuth
<button
	disabled={!authContext.isAuth || isVoted}
  className={`button ${Styles["about__vote-button"]}`}
  onClick={handleVote}
>
  {isVoted ? "Голос учтён" : "Голосовать"}
</button>
```

{video:https://code.s3.yandex.net/kids-web/vids/new-screen.mp4|controls:true|autoplay:0|pip:false|controlsList:nodownload}

### Подведём итоги

Теперь авторизация пользователя работает эталонно 👇🏻

{video:https://code.s3.yandex.net/kids-web/vids/Запись_экрана_2024-02-08_в_22.37.02.mp4|controls:true|autoplay:0|pip:false|controlsList:nodownload}

После заполнения формы AuthForm и авторизации пользователя данные в контексте меняются и при следующем обновлении интерфейса молниеносно обновляются статусы кнопок в компонентах `Header` и `GamePage`

Не возражаем: компоненты стали более независимыми, благодаря им уменьшилось количество импортов и использования различной логики авторизации. Теперь она сконцентрирована в одном месте — компоненте `App`, а в дочерних компонентах просто используются переменные и методы из контекста. Всё это сделало компоненты компактнее и проще для поддержки.

Да, есть один нюанс. React работает так, что компонент перерисовывается, когда изменяются пропсы. Следовательно, если мы прокидываем пропс сквозь множество компонентов, то много компонентов перерисовывается.

{quiz-task}
    background: |
        #f1f1ef
    content: |
        ❗ Возникает проблема перерисовок, и она — прямое следствие изменения пропсов, приходящих в компонент. Провайдер оборачивает группу компонентов и прокидывает пропсы сквозь них, проблема перерисовки остаётся.
{/quiz-task}