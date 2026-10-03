# Свойство Flex и другие флекс-свойства

URL: https://practicum.yandex.ru/learn/kids-web/courses/dff9140f-4a32-45e9-9e61-e7f3e971dcae/sprints/195810/topics/fffbb60d-2661-440d-902f-210b147c01b1/lessons/1db970fb-1f48-4cfc-a2fd-704fe0932555/

Course: Вёрстка на HTML и CSS

Topic: Больше HTML и CSS

Type: web

---

# Свойство Flex и другие флекс-свойства

![](https://pictures.s3.yandex.net:443/resources/Untitled_Artwork_417_1696945888.png)



Теперь, научившись упаковывать элементы своей вёрстки в контейнеры, ты узнаешь, как с помощью всего нескольких правил можно ими легко управлять: выравнивать, центрировать и упорядочивать. В этом нам поможет flexbox — специальная фича в CSS для быстрой и простой вёрстки интерфейсов любой сложности. Короче, в этом уроке научим тебя флексить по-программистски 🌚

Ещё разок. Flexbox (гибкий контейнер) — это CSS-технология, которая помогает решать ряд проблем в веб-дизайне, связанных с размещением и выравниванием элементов внутри контейнеров.

Проблема в том, что выравнивание, центрирование, равномерное распределение элементов по контейнеру требуют написания множества стилей как для контейнера, так и для элементов в нём. А flexbox позволяет это сделать буквально с помощью нескольких строк.

Базовые полезности технологии следующие:

- **Центрирование элементов**
Flexbox позволяет легко центрировать элементы как по горизонтали, так и по вертикали внутри их контейнера, что до его изобретения было не всегда просто и требовало множества CSS-правил.

{video:https://code.s3.yandex.net/kids-web/Untitled_Artwork_2.mp4}

- **Равномерное распределение пространства**
Можно равномерно распределять доступное пространство между элементами флекс-контейнера, что полезно, например, для создания горизонтальных и вертикальных меню.

{video:https://code.s3.yandex.net/kids-web/Untitled_Artwork_3.mp4}

- **Автоматическое выравнивание элементов разной высоты**
Во Flexbox элементы могут выравниваться так, чтобы их высота не влияла на выравнивание других элементов в контейнере.

{video:https://code.s3.yandex.net/kids-web/Untitled_Artwork_4.mp4}

- **Устранение пустых пространств**
Flexbox может автоматически удалять или заполнять пустое пространство в контейнере, что полезно для создания динамических макетов.

{video:https://code.s3.yandex.net/kids-web/Untitled_Artwork_5.mp4}

О, это интересная история. Дело в том, что потребность в адаптиве появилась не сразу.

Долгое время веб-интерфейсы разрабатывались только под десктопные устройства (персональные компьютеры, ноутбуки) — собственно, именно с них юзеры сайты и смотрели. 

Но всё изменил выход первого айфона в 2007 году. Тогда-то и пришлось задуматься об адаптивности, а достигнуть её в то время можно было только путём написания правил для каждого элемента.

С первым айфоном число пользователей мобильного интернета на планете стало резко расти. Из-за его популярности разработчикам понадобился инструмент, который позволил бы легче изменять блочную модель документа. Так и родился флекс в мире кодинга.

Ага!

Сейчас покажем, как работает технология, на примере. Рекомендуем открыть свой VSCode и флексить с нами. 

Сверстаем музыкальный сайтик по макету, точнее блок с заголовком «Популярные треки». Вот, к слову, макет:


![](https://pictures.s3.yandex.net:443/resources/Glavnaia_6_1_1697815095.png)

Это html:



```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ТРЕКИ — И ТОЧКА.</title>
    <link href="./style.css" rel="stylesheet">
</head>
<body>
    <main class="main">
        <section class="content">
            <h2 class="content__title"> ❤️‍🔥 Плейлист меланхоличный, Октябрь 2023 </h2>
            <div class="content__cards">
                <div class="card">
                    <img alt="Ski Head" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/1.jpeg" class="card__image" />
                    <div class="card__info">
                        <a class="card__link" href="https://music.yandex.ru/album/191417/track/1932452" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Ski Head</h3>
                            <p class="card__text card__text_author">by Frazier Chorus</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Ami" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/2.png" class="card__image" />
                    <div class="card__info">
                        <a class="card__link" href="https://music.yandex.ru/album/8704945/track/57748857" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Ami</h3>
                            <p class="card__text card__text_author">by Devendra Banhart</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Ancora Tu" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/3.jpeg" class="card__image" />
                    <div class="card__info">
                        <a class="card__link" href="https://music.yandex.ru/album/5977070/track/43696602" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Ancora Tu</h3>
                            <p class="card__text card__text_author">by Róisín Murphy</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Shell" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/4.jpeg" class="card__image" />
                    <div class="card__info card__info_yellow">
                        <a class="card__link" href="https://www.youtube.com/watch?v=wtd_SgWo4Vw" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Shell</h3>
                            <p class="card__text card__text_author">by Sunny War</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="All the Tired Horses" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/5.jpeg" class="card__image" />
                    <div class="card__info">
                        <a class="card__link card__link_longer-title" href="https://music.yandex.ru/album/18861236/track/93557371" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">All the Tired Horses</h3>
                            <p class="card__text card__text_author">by Bob Dylan</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Strange" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/6.jpg" class="card__image" />
                    <div class="card__info card__info_green">
                        <a class="card__link" href="https://music.yandex.ru/album/965419/track/560522" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Strange</h3>
                            <p class="card__text card__text_author">by Patsy Cline</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Baby" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/7.jpeg" class="card__image" />
                    <div class="card__info">
                        <a class="card__link card__link_longer-author" href="https://music.yandex.ru/album/719229/track/6690568" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Baby</h3>
                            <p class="card__text card__text_author">by Ariel Pink's Haunted Graffiti</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Foreigners" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/8.png" class="card__image" />
                    <div class="card__info">
                        <a class="card__link" href="https://music.yandex.ru/album/3300905/track/27584658" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Foreigners</h3>
                            <p class="card__text card__text_author">by Joe Mubare</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="It’s Good for the Soul" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/9.jpeg" class="card__image" />
                    <div class="card__info">
                        <a class="card__link card__link_long" href="https://music.yandex.ru/album/442068/track/3926762" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">It’s Good for the Soul</h3>
                            <p class="card__text card__text_author">by The Salsoul Orchestra</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Sign Your Name" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/10.png" class="card__image" />
                    <div class="card__info">
                        <a class="card__link" href="https://music.yandex.ru/album/9418994/track/60745743" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Sign Your Name</h3>
                            <p class="card__text card__text_author">by Sananda Maitreya</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Cherry" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/11.jpeg" class="card__image" />
                    <div class="card__info">
                        <a class="card__link" href="https://music.yandex.ru/album/90459/track/810198" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Cherry</h3>
                            <p class="card__text card__text_author">by J.J. Cale</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Rain" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/12.png" class="card__image" />
                    <div class="card__info card__info_pink">
                        <a class="card__link" href="https://music.yandex.ru/album/21946/track/215079" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Rain</h3>
                            <p class="card__text card__text_author">by Madonna</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Bad Influence" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/13.jpeg" class="card__image" />
                    <div class="card__info card__info_blue">
                        <a class="card__link card__link_longer-author" href="https://music.yandex.ru/album/11472049/track/68922978" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Bad Influence</h3>
                            <p class="card__text card__text_author">by Sebastian Maschat & Erlend Øye</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Baby Bye Bye (Demo)" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/14.jpeg" class="card__image" />
                    <div class="card__info">
                        <a class="card__link card__link_wide" href="https://music.yandex.ru/album/11889963/track/70411796" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Baby Bye Bye (Demo)</h3>
                            <p class="card__text card__text_author">by Mac DeMarco</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Ride Like the Wind" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/15.jpeg" class="card__image" />
                    <div class="card__info">
                        <a class="card__link card__link_wide" href="https://music.yandex.ru/album/56494/track/34174528" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Ride Like the Wind</h3>
                            <p class="card__text card__text_author">by Christopher Cross</p>
                        </a>
                    </div>
                </div>
                <div class="card">
                    <img alt="Choo Choo Gatagoto" src="https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/images/16.png" class="card__image" />
                    <div class="card__info">
                        <a class="card__link card__link_wide" href="https://music.yandex.ru/album/6472367/track/47594088" target="_blank" rel="norefferer">
                            <h3 class="card__text card__text_title">Choo Choo Gatagoto</h3>
                            <p class="card__text card__text_author">by Haruomi Hosono</p>
                        </a>
                    </div>
                </div>
            </div>
        </section>
    </main> 
</body>
</html>
```

Это стили:

```css
@font-face {
    font-family: "Anonymous Pro";
    src: url(https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/styles/fonts/AnonymousPro-Regular.woff) format('woff'), 
    url(https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/styles/fonts/AnonymousPro-Regular.ttf) format('truetype');
    font-weight: 400;
    font-style: normal;
    display: swap;
}

@font-face {
    font-family: "Anonymous Pro";
    src: url(https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/styles/fonts/AnonymousPro-Bold.woff) format('woff'), 
    url(https://sandbox-teens.practicum-team.ru/tasks/03-more-html-and-css-sprint/01-flex-sandboxes/06-header-and-footer/sandbox-01/pre/styles/fonts/AnonymousPro-Bold.ttf) format('truetype');
    font-weight: 700;
    font-style: normal;
    display: swap;
}

body {
    margin: 0;
}

.main {
    display: block;
    width: 100%;
    min-height: 100vh;
    background: linear-gradient(156deg, #FFED00 0%, #FF3DFE 51.89%, #5253FF 100%);
    flex: 1 0 auto;
    color: #121723;
}

.content {
    margin: 68px auto 26px;
	  display: block;
    width: 90%;
    max-width: 1290px;
}

.content__title {
    color: #121723;
    font-family: "Anonymous Pro", sans-serif;
    font-size: 42px;
    font-style: normal;
    font-weight: 700;
    line-height: 100%;
    margin: 0;
}

.content__cards {
	  display: block;
    width: 100%;
    margin: 26px 0 0;
}

.card {
  	display: inline-block;
    width: 100%;
    max-width: 300px;
    margin: 4px;
}

.card__image {
    width: 100%;
    height: 100%;
    max-height: 300px;
    object-fit: cover;
    object-position: center;
    border-radius: 12px;
}

.card__info {
    display: block;
    margin: 0;
    border-radius: 12px;
    background: white;
    padding: 24px 12px;
    min-height: 72px;
}

.card__info_yellow {
    background: #FAFF00;
}

.card__info_green {
    background: #24FF00;
}

.card__info_pink {
    background: #FFB4EA;
}

.card__info_blue {
    background: #03E7FC;
}

.card__link {
    width: 85%;
    color: #121723;
    text-decoration: none;
}

.card__text {
    font-family: "Anonymous Pro", sans-serif;
    font-size: 20px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    margin: 0;
}

.card__text_title {
    font-size: 26px;
}

.card__text_author {
    font-size: 20px;
    font-weight: 400;
}
```

В этом коде карточки выстроены в ряд с помощью свойства, которое мы проходили на прошлых уроках — `display: inline-block;`(оно делает элемент блочным, но при этом заставляет его находиться в строке).

Так тоже можно, но карточки выстроены не по макету, а про адаптив речи вообще не идёт. Будем исправлять, а пока копируй как есть и посмотри, как выглядит страница сейчас.

![](https://pictures.s3.yandex.net:443/resources/Snimok_ekrana_2023-10-19_v_17.13.25_1698229080.png)

Ну что, погнали! 

## Шаг 1

Первое, что мы сделаем, — это зададим всему контейнеру с карточками (у него класс `content__cards`) `display: flex;`, а у класса `card` уберём свойства `display: inline-block;` и `margin-right: 30px;` – заменим `display` на `flex`, а `margin` вообще уберём.

Получится такая вот очередь в школьную столовую:


![](https://pictures.s3.yandex.net:443/resources/Snimok_ekrana_2023-10-19_v_17.20.06_1698229564.png)

```css
.content__cards {
	display: flex;
    width: 100%;
    margin: 26px 0 0;
}
.card {
		display: flex;
    flex-direction: column;
    width: 100%;
		min-height: 72px;
    max-width: 300px;
}
```

## Шаг 2

Теперь для контейнера с классом `content__cards` пропишем свойство `flex-wrap: wrap;`

Оно заставляет элементы внутри контейнера переноситься на следующую строчку, если они не помещаются. Наши карточки встанут в ряд по четыре штуки на каждой строке.


![](https://pictures.s3.yandex.net:443/resources/Snimok_ekrana_2023-10-19_v_17.21.09_1698229736.png)

## Шаг 3

Как видишь, карточки всё ещё прилипают друг к другу. А теперь открой DevTools и наведи на контейнер. Ты увидишь, что фиолетовым выделено пустое пространство справа.


![](https://pictures.s3.yandex.net:443/resources/Snimok_ekrana_2023-10-19_v_17.22.38_1698229784.png)


Мы это тоже сейчас поправим одним правилом. 

Нужно в этот же селектор контейнера `content__cards` дописать `justify-content: space-between;`

Это свойство регулирует распределение пространства между элементами внутри контейнера. Мы установили ему значение `space-between;`, что буквально означает «пространство между». При таком выборе крайние элементы прижимаются к границам родительского контейнера, а оставшиеся выстраиваются внутри него равномерно, так, чтобы между ними были одинаковые отступы.

Гляди:


![](https://pictures.s3.yandex.net:443/resources/Snimok_ekrana_2023-10-19_v_17.24.07_1698229891.png)



Для `justify-content` можно задать и другие значения, чекай в [доке](https://doka.guide/css/justify-content/){target="_blank"}.

```css
.content__cards {
	  display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    width: 100%;
    margin: 26px 0 0;
}
```

## Шаг 4

Сделаем нашу страничку адаптивной — в том числе для смартфонов. 

Создадим медиазапрос `@media (max-width: 768px) {}` и напишем в нём, что контейнер `content__cards` будет иметь правило `flex-direction: column;`

Это свойство отвечает за направление flex-элементов: значение `row` задаёт горизонтальное направление, то есть заставляет элементы выстраиваться в ряд, а `column` задаёт вертикальное направление, то есть элементы будут выстраиваться в колонку.

Теперь наша страница на разрешениях до 768px выглядит так:


![](https://pictures.s3.yandex.net:443/resources/Snimok_ekrana_2023-10-19_v_17.26.36_1698230027.png)

Не совсем то, что нам нужно – элементы прижимаются к левому краю. Но и это мы можем поправить всего одним правилом. 

Для `content__cards` зададим `align-items: center;`

Теперь колонка карточек будет выглядеть так:


![](https://pictures.s3.yandex.net:443/resources/Snimok_ekrana_2023-10-19_v_17.27.54_1698230069.png)



`align-items` отвечает за выравнивание элементов в текущем флекс-направлении (в нашем случае — в колонке), сейчас мы указали выравнивание по центру — `center`

Можно указать и другие значения: например, `flex-end` (элементы выравниваются по нижнему краю при расположении в строку или по правому краю при расположении в столбик), это выглядит так:


![](https://pictures.s3.yandex.net:443/resources/Snimok_ekrana_2023-10-19_v_17.28.25_1698230092.png)



А значение `flex-start` (элементы прижимаются к краю, от которого начинается основная ось) даст вот такой эффект:


![](https://pictures.s3.yandex.net:443/resources/Snimok_ekrana_2023-10-19_v_17.28.36_1698230116.png)



Есть ещё приличное количество других, но мы остановимся на `align-items: center;`

Кстати, его можно записать **НЕ** в медиазапрос, а в обычный селектор `content__cards`, так как выравнивание не помешает на любых разрешениях экрана. 

Сейчас на десктопе разницы не будет видно, потому что все карточки у нас одинакового размера. 

Теперь наша страница довольно-таки адаптивна 💁🏻‍♀️

![](https://pictures.s3.yandex.net:443/resources/Screenshot_2023-10-05_at_21.38.19_1696947223.png)

```css
.content__cards {
	  display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    width: 100%;
    align-items: center;
    margin: 26px 0 0;
}

@media (max-width: 768px) {
    .content__cards {
        flex-direction: column;
    }
}
```

Пфф. Ну а смысл нам врать? Сейчас покажем последний финт в этом уроке. 

Нужно задать немного отступов для карточек.

## Шаг 5

Сейчас снизу от карточки у нас нет отступов, а в макете они есть. Нужно задать 22px снизу и 30px сбоку, и это тоже можно очень просто сделать с помощью флексов. 

Для того же контейнера `content__cards` зададим свойство `column-gap` со значением `30px` и `row-gap` со значением `22px`.

Первое значение отмеряет расстояние между флекс-элементами по вертикали, второе — по горизонтали. Мы сейчас увидим только работу значения по вертикали, так как у нас ранее прописано `justify-content: space-between;`  и из-за этого элементы разбегаются по краям контейнера, оставляя между собой пространство. Но без `justify-content` расстояние между карточками будет 30px, можешь убрать его и удостовериться.



![](https://pictures.s3.yandex.net:443/resources/Snimok_ekrana_2023-10-19_v_17.37.27_1698230210.png)

```css
.content__cards {
    width: 100%;
		display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    column-gap: 22px;
    row-gap: 30px;
    margin: 26px 0 0;
}
```

Наши поздравления! 

Теперь ты в курсе следующих вещей:

- Знаешь, что такое flexbox и для чего его применяют
- Умеешь выравнивать элементы, да ещё и по разным краям, с помощью `align-items`
- Можешь легко управлять элементами и пространством, которое они занимают, с помощью `justify-content`
- Можешь создавать отступы с помощью `gap`
- И лёгким движением руки можешь сделать адаптив и не только, задав направление флекс-элементам с помощью `flex-direction`

![](https://pictures.s3.yandex.net:443/resources/Frame_95_1697815834.png)