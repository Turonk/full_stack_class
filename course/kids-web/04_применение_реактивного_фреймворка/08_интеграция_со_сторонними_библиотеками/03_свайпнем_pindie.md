# Свайпнем Pindie

URL: https://practicum.yandex.ru/learn/kids-web/courses/232ea8d5-ae43-4072-aa39-ade914d25935/sprints/190124/topics/400cce86-70c5-4448-b47d-5bba20048e1c/lessons/9b25f954-c5af-4547-b359-1151d74835e5/

Course: Применение реактивного фреймворка

Topic: Интеграция со сторонними библиотеками

Type: web

---

# Свайпнем Pindie

Всё так! Красивые с точки зрения дизайна элементы страницы должны быть просты в использовании и интерактивны, чтобы привлекать внимание и побуждать пользователя к взаимодействию. Чрезмерное улучшение и попытка совместить несовместимое не приведут ни к чему хорошему. Разве что к визуальному шуму.

Для оптимизации интерфейса и более интерактивного взаимодействия с пользователем мы добавим динамики в списки игр. Научим тебя использовать крутой слайдер, чтобы список игр перелистывался на мобильных устройствах и анимированно прокручивался на компьютерах 👇🏻

{video:https://code.s3.yandex.net/kids-web/vids/demo.mp4|controls:true|autoplay:0|pip:false|controlsList:nodownload}

Такой слайдер можно реализовать самостоятельно, но это задача непростая. Самая сложная часть — предусмотреть все особенности различных устройств и браузеров пользователя. Сделать красивый, стабильный и оптимальный слайдер на все случаи жизни — задача не на один день. Но, как говорится, зачем придумывать свой «велосипед», когда существуют крутые готовые решения. Вот популярное и универсальное решение для слайдеров — `Swiper.js`

{video:https://code.s3.yandex.net/kids-web/vids/Untitled_Artwork.mp4}

## Поговорим о Swiper

Чтобы ознакомиться с библиотекой, залетай на [сайт](https://swiperjs.com){target="_blank"} проекта. Там же для юзеров собраны примеры применения самых популярных слайдеров 👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1581_1710156364.png)

Библиотекой предусмотрена гибкая настройка типов анимаций и способов взаимодействия с интерфейсом слайдера.

**Swiper** — универсальное решение для любых платформ. Его можно использовать в веб-приложениях, написанных при помощи разных библиотек. Под каждую из них есть своя версия свайпера. Но в то же время существует классическая JavaScript-версия, которую можно встроить вообще в любой клиентский JS-код 👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1582_1710156376.png)

Чтобы установить и использовать библиотеку Swiper в своём проекте, жми на раздел **Docs**, где содержится вся-вся инфа👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1583_1710156388.png)

В зависимости от использованных технологий инструкция может отличаться. К сожалению, на момент разработки проекта Pindie, Swiper для React-компонентов скорее всего перестанет поддерживаться в следующих обновлениях и будет удален. Мы с тобой будем использовать **классическое решение** на JavaScript, оно самое универсальное и поможет разобраться в этапах добавления сторонней библиотеки.

{video:https://code.s3.yandex.net/kids-web/vids/get_started.mp4|controls:true|autoplay:0|pip:false|controlsList:nodownload}

Разработчики постарались сделать работу со Swiper максимально простой, чтобы добавление и использование библиотеки не вызывало трудностей. Но перед тем, как её подключать, разберёмся, где и как будем использовать слайдеры в Pindie.

## Адаптируем проект

Сейчас в проекте есть компонент `CardsList`, он объединяет информацию об отображаемой коллекции игр и список карточек с ними. Разделим эту логику на отдельные компоненты:

- Компонент `CardsSlider` при помощи библиотеки Swiper будет отображать список карточек с анимацией их перелистывания.
- Компонент `CardsList` будет отображать статичный список карточек, как это было раньше.
- Отдельный компонент `CardsListSection` будет управлять отображением разных списков карточек. Используя переменную `type`, будем отображать слайдеры (компонент `CardsSlider`) для главной страницы Pindie — для этого передадим пропс `type="slider"`. Для страниц с играми, отсортированными по жанрам, будем использовать статичные списки игр (компонент `CardsList`).

Папку в проекте `app/components/CardsList` переименуй в `CardsListSection`, то же самое сделай с файлом `css`

Создай одноимённый файл с компонентом `CardsListSection`, в котором будешь использовать стили для секции из файла `CardsListSection.module.css`, и опиши только информацию о секции. Используя условное отображение, тернарным оператором проверяется значение `props.type` и отображается компонент `CardsSlider`, если `props.type === 'slider'`, в противном случае — компонент `CardsList` 👇🏻

```javascript
// Файл CardsListSection.jsx

import Styles from "./CardsListSection.module.css";
import { CardsList } from "./CardsList";
import { CardsSlider } from "./CardsSlider";

export const CardsListSection = (props) => {
  return (
    <section className={Styles["list-section"]}>
      <h2 className={Styles["list-section__title"]} id={props.id}>
        {props.title}
      </h2>
      {props.type === 'slider' ? <CardsSlider data={props.data} /> : <CardsList data={props.data} />}
    </section>
  );
};
```

В файле `CardsList.jsx` используй стили из `CardsListSection.module.css`, а компонент `CardsList` будет возвращать статичный список карточек с играми 👇🏻

```javascript
// Файл CardsList.jsx 

import Link from "next/link";
import { Card } from "../Card/Card";
import Styles from "./CardsListSection.module.css";

export const CardsList = (props) => {
  return (
    <ul className={Styles["cards-list"]}>
      {props.data.map((item) => {
        return (
          <li className={Styles["cards-list__item"]} key={item.id}>
            <Link href={`/games/${item.id}`} className={Styles["card-list__link"]}>
              <Card
                {...item}
              />
            </Link>
          </li>
        );
      })}
    </ul>
  );
};
```

В папках с отдельными страницами по жанрам игр (`new`, `pixel-games`, `popular`, `runners`, `shooters`, `tds`) замени использование компонента `CardsList` на новый компонент `CardsListSection`👇🏻

```javascript
// Компонент New в файле app/new/page.js
import { endpoints } from "@/app/api/config";
import { useGetDataByCategory } from "@/app/api/api-hooks";
import { CardsList } from "../components/CardsList/CardsList"; // удалить
import { CardsListSection } from "../components/CardsListSection/CardsListSection"; // добавить
import { Preloader } from "@/app/components/Preloader/Preloader";

export default function New() {
  const newGames = useGetDataByCategory(endpoints.games, "new");
  return (
    <main className="main-inner">
	    {/* Используем CardsListSection вместо CardsList */}
      {newGames ? <CardsListSection id="new" title="Новые" data={newGames} /> : <Preloader />}
    </main>
  );
}
```

Подготовка проекта завершена. Осталось установить библиотеку Swiper и описать компонент слайдера с играми `CardsSlider`

## Используем Swiper в проекте

На сайте Swiper, в разделе **Swiper Demos,** можно выбрать подходящий вариант слайдера. Для Pindie сделаем тип анимации `Autoplay` для компьютеров👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1584_1710156507.png)

А для мобильных гаджетов — тип `Pagination fraction` 👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1585_1710156518.png)

Каждая библиотека содержит собственную инструкцию по установке и API для взаимодействия с инструментами. В Swiper это сделано максимально просто. Зайди в раздел **Getting Started** и выполни инструкцию по установке 👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1586_1710156529.png)

В терминале редактора кода введи команду `npm install swiper`

После установки библиотеки создай компонент слайдера: файл `CardsSlider.jsx` в папке `CardsListSection` по адресу в проекте `app/components/CardsListSection`. Это будет клиентский компонент, который будет отображать список карточек, как и компонент `CardsList`, только при этом он может использовать дополнительные возможности из библиотеки Swiper.

### **Опишем компонент `CardsSlider`**

### Шаг 1. Импорты

Для корректной работы слайдера нужно:

- Импортировать основной модуль `Swiper` из одноимённой библиотеки `import Swiper from 'swiper'`
- Добавить CSS-стили для управления элементами слайдера и их стилизации `import 'swiper/css'`
- Для слайдеров `Autoplay` и  `Pagination fraction` нужно отдельно импортировать соответствующие модули: `import { Autoplay, Pagination } from "swiper/modules"` (так как по умолчанию Swiper экспортирует только базовую версию без дополнительных модулей, таких как навигация, нумерация страниц и т. п.).
- Для постраничной нумерации пригодятся дополнительные CSS-классы, импортируй их, как это описано в инструкции по установке библиотеки **Getting Started With Swiper**: `import 'swiper/css/pagination'`

```javascript
import Swiper from "swiper";
import { Autoplay, Pagination } from "swiper/modules";
import "swiper/css";
import "swiper/css/pagination";
```

### Шаг 2. Из списка в слайдеры

Теперь, как в разделе **Add Swiper HTML Layout,** добавим ключевые классы для превращения списка карточек в слайдер.

Для этого добавь файл `CardsSlider.module.css` в папку `app/components/CardsListSection` со своими CSS-стилями для правильного позиционирования и отображения слайдера в проекте Pindie.

{quiz-task}
    background: |
        #f1f1ef
    content: |
        📩 Стили для `CardsSlider` можешь скачать из [GitHub](https://github.com/Yandex-Practicum/pindie-prebuild-components/blob/main/CardsListSection/CardsSlider.module.css){target="_blank"}.
{/quiz-task}

В компоненте `CardsSlider` пометь основные элементы классами `swiper...` для работы библиотеки Swiper:

- Фрагмент со слайдером `className={``swiper ${Styles["slider"]}``}`
- Выдели список карточек внутри слайдера через классы: `className={``swiper-wrapper ${Styles["slider-wrapper"]}``}`
- Укажи для каждого элемента списка класс: `className={``swiper-slide ${Styles["slide"]}``}`
- Добавь дополнительный элемент `div` с классом `className={``swiper-pagination ${Styles["pagination"]}``}` для нумерации слайдов на мобильных устройствах.

Чекай 👇🏻

```javascript
export const CardsSlider = (props) => {
  return (
    <>
			// Slider main container / Главный контейнер слайдера
      <div className={`swiper ${Styles["slider"]}`}>
				// Additional required wrapper / Дополнительная обёртка для списка карточек 
        <ul className={`swiper-wrapper ${Styles["slider-wrapper"]}`}>
          {props.data.map((item, i) => {
            return (
							// Slides / Слайды
              <li className={`swiper-slide ${Styles["slide"]}`} key={i}>
                <Link href={`/games/${item.id}`}>
                  <Card {...item} />
                </Link>
              </li>
            );
          })}
        </ul>
				// If we need pagination / Класс для постраничной нумерации
        <div className={`swiper-pagination ${Styles["pagination"]}`}></div>
      </div>
    </>
  );
};
```

Благодаря этим классам код библиотеки Swiper сможет определить, как и какие элементы должны быть анимированы.

### Шаг 3. Запуск

Чтобы настроить и запустить слайдер, достаточно вызвать экземпляр класса с набором опций `new Swiper(".swiper", options)`

О том, какие опции тебе пригодятся, расскажет раздел сайта **Swiper Core/API** 👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1587_1710156844.png)

Ранее мы решили, что на разных разрешениях экрана слайдер должен отличаться. В этом поможет параметр `breakpoints` 👇🏻

![](https://pictures.s3.yandex.net:443/resources/Frame_1588_1710156889.png)

В объекте `options` укажи ключ `breakpoints`, а в его значение положи другой объект, который будет содержать описание для выбранной ширины экрана. Для устройств с шириной экрана от `450px` укажи следующие параметры 👇🏻

```javascript
const options = {
      breakpoints: {
				// Параметры слайдера для мониторов > 450px
        450: {
          loop: true, // Установи бесконечное переключение слайдов
          spaceBetween: 20, // Установи расстояние между слайдами в 20px
          slidesPerView: "auto", // Количество отображаемых слайдов (в зависимости от ширины экрана)
          allowTouchMove: false, // Запрети пользователю перемещать слайды
          speed: 6500, // Установи скорость анимации в миллисекундах
					// Включи автовоспроизведение анимации — модуль Autoplay
          autoplay: {
            enabled: true,
            delay: 0,
          },
					// Отключи постраничную навигацию — модуль Pagination
          pagination: {
            enabled: false,
          },
        },
      },
      modules: [Autoplay, Pagination],
    };
```

Для экранов мобильных устройств опиши другие параметры 👇🏻

```javascript
    const options = {
			// Параметры слайдера для экранов мобильных гаджетов шириной < 450px
      loop: false, // Отключи бесконечное переключение слайдов
      spaceBetween: 10, // Установи расстояние между слайдами в 10px
      allowTouchMove: true, // Позволь пользователю перемещать слайды
      slidesPerView: 1, // Количество отображаемых слайдов за раз = 1
			// Отключи автовоспроизведение — модуль Autoplay
      autoplay: {
        enabled: false,
      },
			// Параметры слайдера для мониторов компьютеров
      pagination: {
        el: ".swiper-pagination",
        type: "fraction",
        enabled: true,
        clickable: true,
      },
			// Параметры слайдера для мониторов > 450px
      breakpoints: {
        450: {
          loop: true,
          spaceBetween: 20,
          slidesPerView: "auto",
          allowTouchMove: false,
          speed: 6500,
          autoplay: {
            enabled: true,
            delay: 0,
          },
          pagination: {
            enabled: false,
          },
        },
      },
			// Используй модули для разных типов анимации
      modules: [Autoplay, Pagination],
    };
```

Осталось запустить слайдер в момент монтирования компонента. Для этого используй хук `useEffect` и вызови экземпляр класса `Swiper` с выбранными параметрами 👇🏻

```javascript
useEffect(() => {
    const options = {
      loop: false,
      spaceBetween: 10,
      allowTouchMove: true,
      slidesPerView: 1,
      autoplay: {
        enabled: false,
      },
      pagination: {
        el: ".swiper-pagination",
        type: "fraction",
        enabled: true,
        clickable: true,
      },
      breakpoints: {
        450: {
          loop: true,
          spaceBetween: 20,
          slidesPerView: "auto",
          allowTouchMove: false,
          speed: 6500,
          autoplay: {
            enabled: true,
            delay: 0,
          },
          pagination: {
            enabled: false,
          },
        },
      },
      modules: [Autoplay, Pagination],
    };
		new Swiper(".swiper", options);
  }, []);
```

```javascript
"use client";

import Swiper from "swiper";
import { Autoplay, Pagination } from "swiper/modules";
import "swiper/css";
import "swiper/css/pagination";
import { useEffect } from "react";
import { Card } from "../Card/Card";
import Styles from "./CardsSlider.module.css";
import Link from "next/link";

export const CardsSlider = (props) => {
  useEffect(() => {
    const options = {
	    // Параметры слайдера для экранов мобильных гаджетов шириной < 450px
      loop: false,
      spaceBetween: 10,
      allowTouchMove: true,
      slidesPerView: 1,
      autoplay: {
        enabled: false,
      },
      pagination: {
        el: ".swiper-pagination",
        type: "fraction",
        enabled: true,
        clickable: true,
      },
			// Параметры слайдера для мониторов компьютера
      breakpoints: {
        450: {
          loop: true,
          spaceBetween: 20,
          slidesPerView: "auto",
          allowTouchMove: false,
          speed: 6500,
          autoplay: {
            enabled: true,
            delay: 0,
          },
          pagination: {
            enabled: false,
          },
        },
      },
      modules: [Autoplay, Pagination],
    };
    new Swiper(".swiper", options);
  }, []);
  return (
    <>
      <div className={`swiper ${Styles["slider"]}`}>
        <ul className={`swiper-wrapper ${Styles["slider-wrapper"]}`}>
          {props.data.map((item, i) => {
            return (
              <li className={`swiper-slide ${Styles["slide"]}`} key={i}>
                <Link href={`/games/${item.id}`}>
                  <Card {...item} />
                </Link>
              </li>
            );
          })}
        </ul>
        <div className={`swiper-pagination ${Styles["pagination"]}`}></div>
      </div>
    </>
  );
};
```

## Подведём итоги

Используя сторонние библиотеки, важно помнить, что проект может стать зависимым от других разработчиков. Необходимо постоянно следить за его работой и взаимодействием со сторонними библиотеками, так как существует множество причин для сбоев:

- При очередном обновлении библиотеки может измениться принцип взаимодействия элементов.
- Возможно возникновение конфликтов с кодом других библиотек или версий фреймворка.
- Устаревание кодовой базы и отсутствие поддержки библиотек.

В реальных проектах часто возникают трудности при адаптации стороннего кода. Swiper имеет простой и гибкий интерфейс, однако даже от него порой сложно добиться желаемого результата. Но, несмотря на все минусы, это всё ещё отличное решение. При самостоятельной разработке подобного слайдера пришлось бы потратить гораздо больше времени и ресурсов.