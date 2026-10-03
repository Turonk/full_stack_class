# Generates remaining PulseLab lesson files. Run from repo root.
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] if Path(__file__).name == "gen_lessons.py" else Path("c:/Dev/Coddy_fullstack")
COURSE = ROOT / "course"

A = [
    {
        "id": "A03-text-lists-media",
        "title": "Текст, списки, ссылки, картинки",
        "project": "Pulse FM",
        "goal": "Ученик собирает хит недели: обложка, исполнитель, маркированный список фактов, внешняя ссылка.",
        "screen": "Секция хита с картинкой 400px по ширине, списком и ссылкой на трек.",
        "topic": "- img всегда с alt.\n- a: href, и не «нажми сюда».\n- ul/ol/li — списки фактов, не абзацы с дефисами.\n- figure + figcaption для обложки.",
        "practice": "1. Картинка хита (можно picsum.photos или своя).\n2. figcaption.\n3. ul из 3 фактов.\n4. Ссылка на безопасный внешний URL.\n5. Проверка: без картинки alt читается.",
        "errors": "- Картинка без alt.\n- Слишком тяжёлый jpg с телефона (сжимаем или ставим заглушку).\n- Ссылка без https.",
        "hw": "Добавь второй список: «сегодня в эфире» из 4 пунктов. Сдать HTML + скрин.",
        "hwcrit": "Есть img+alt, ul или ol, осмысленный текст ссылки, семантика прошлого урока на месте.",
        "practicum": "изображения, ссылки, списки",
        "kind": "lesson",
    },
    {
        "id": "A04-track-cards",
        "title": "Карточки треков",
        "project": "Pulse FM",
        "goal": "Три article-карточки трека с заголовком, исполнителем и длительностью.",
        "screen": "Секция tracks: 3 карточки друг под другом.",
        "topic": "- article — самостоятельная карточка.\n- h2/h3 иерархия: один h1 на странице.\n- time можно текстом «3:14».\n- Повтор структуры — это ок, потом придёт CSS.",
        "practice": "1. Три article.\n2. В каждой h3, p, span длительности.\n3. Разные тексты, не копипаст одного трека трижды.\n4. Проверка иерархии заголовков.",
        "errors": "- Три h1.\n- Карточка из одних div без заголовка.\n- Одинаковые id.",
        "hw": "Четвёртая карточка «мой трек».",
        "hwcrit": "4 article, уникальные названия, один h1.",
        "practicum": "вложенность тегов, блоки",
        "kind": "lesson",
    },
    {
        "id": "A05-search-form",
        "title": "Форма «найти трек» без JS",
        "project": "Pulse FM",
        "goal": "Собирает доступную форму поиска: label, input, button. Понимает method get.",
        "screen": "Секция search с формой. После submit в адресной строке появляется ?q=...",
        "topic": "- form, label for + id.\n- input type=search.\n- button type=submit.\n- GET показывает запрос в URL — это нормально и наглядно.",
        "practice": "1. Форма method=get.\n2. Label связан с полем.\n3. Placeholder не вместо label.\n4. Submit, смотрим URL.\n5. required на поле.",
        "errors": "- Нет label, только placeholder.\n- button без type в другой форме.\n- input вне form.",
        "hw": "Поле + выпадающий жанр select (3 жанра).",
        "hwcrit": "label, name у полей, select, форма отправляется.",
        "practicum": "формы на уровне HTML",
        "kind": "lesson",
    },
    {
        "id": "A06-showcase-music-static",
        "title": "Showcase: страница музыкального сервиса",
        "project": "Pulse FM",
        "goal": "Каждый показывает законченную статичную страницу и объясняет разметку.",
        "screen": "Полный Pulse FM: хиты, 3 карточки, форма, footer.",
        "topic": "См. шаблон showcase. Не чиним вёрстку всем классом — слушаем рассказ.",
        "practice": "Карточка выступления: экран → фича → тег, которым гордишься → ошибка, которую починил.",
        "errors": "- Читает HTML вслух вместо показа продукта.\n- Нет якорей.\n- Битые картинки.",
        "hw": "Дополировать must-have к спринту 2 (список из PROJECT.md).",
        "hwcrit": "Чек-лист минипроекта 1 закрыт.",
        "practicum": "повтор HTML",
        "kind": "showcase",
    },
    {
        "id": "A07-css-cascade-vars",
        "title": "CSS: каскад, селекторы, переменные",
        "project": "MusicHub",
        "goal": "Подключает CSS-файл, задаёт :root переменные PulseLab, красит body и header.",
        "screen": "Тёмный фон, светлый текст, фиолетовый акцент на ссылках.",
        "topic": "- style vs файл css.\n- Специфичность: тег < класс < не дерите !important.\n- :root --bg --text --accent.\n- Наследование цвета и шрифта.",
        "practice": "1. styles.css + link.\n2. Переменные из STYLE.md.\n3. body фон и шрифт.\n4. header padding.\n5. Цвет ссылок через var.",
        "errors": "- CSS внутри каждой карточки дублируется.\n- Опечатка в имени переменной.\n- Подключили файл не из той папки.",
        "hw": "Класс .muted для подписей.",
        "hwcrit": "Внешний css, минимум 4 переменные, нет !important.",
        "practicum": "правила CSS, файл стилей, наследование",
        "kind": "lesson",
    },
    {
        "id": "A08-flex-header-player",
        "title": "Flex: шапка, плеер, сетка карточек",
        "project": "MusicHub",
        "goal": "Кладёт шапку в строку, карточки — в ряд на широком экране через flex.",
        "screen": "Лого слева, меню справа. Карточки в ряд. Внизу полоска плеера.",
        "topic": "- display:flex, gap, align-items, justify-content.\n- flex-wrap.\n- Плеер: position sticky bottom.\n- Не используем float.",
        "practice": "1. header flex space-between.\n2. .tracks display:flex; wrap.\n3. Карточка min-width.\n4. .player sticky.\n5. Проверка при сужении окна.",
        "errors": "- Забыли flex-wrap — вылезает за экран.\n- height:100vh на каждой карточке.\n- Плеер перекрывает контент без padding-bottom у main.",
        "hw": "Выровнять кнопки плеера в ряд: prev / play / next.",
        "hwcrit": "Шапка и карточки на flex, плеер виден.",
        "practicum": "блоки, отступы, раскладка",
        "kind": "lesson",
    },
    {
        "id": "A09-grid-mobile-first",
        "title": "Grid и адаптив, mobile-first",
        "project": "MusicHub",
        "goal": "Строит сетку треков через grid и медиазапрос от 720px. На 360px — одна колонка.",
        "screen": "Телефон: колонка. Планшет: 2 колонки. Десктоп: 3.",
        "topic": "- Mobile-first: база = телефон.\n- grid-template-columns repeat(auto-fit, minmax(220px, 1fr)).\n- @media (min-width: 720px).\n- Viewport meta уже должен быть.",
        "practice": "1. Сетка карточек grid.\n2. База 1 колонка.\n3. 720px → 2+.\n4. Проверка DevTools device toolbar.\n5. Горизонтальный скролл = баг, чиним.",
        "errors": "- max-width медиа вместо min-width при mobile-first.\n- Картинка шире экрана без max-width:100%.\n- Фиксированная ширина 1200px на body.",
        "hw": "Хит недели: картинка+текст в grid на десктопе, колонкой на телефоне.",
        "hwcrit": "Нет горизонтального скролла на 360px.",
        "practicum": "больше вёрстки, блоки",
        "kind": "lesson",
    },
    {
        "id": "A10-typography-visual",
        "title": "Типографика и визуальный стиль PulseLab",
        "project": "MusicHub",
        "goal": "Подключает Google Fonts Syne + IBM Plex Sans, выстраивает шкалу заголовков, скругления карточек.",
        "screen": "Узнаваемый PulseLab: тёмный, крупный заголовок, карточки 20px radius, тень.",
        "topic": "- link на fonts.google.com (Syne, IBM Plex Sans).\n- Шкала: h1 2.4rem, h2 1.6rem, body 1rem.\n- line-height 1.5.\n- border-radius и box-shadow из STYLE.",
        "practice": "1. Подключить шрифты.\n2. Назначить display/body.\n3. Карточки: фон --bg-elev, radius, padding.\n4. Иерархия не прыгает.\n5. Контраст текста проверить глазом.",
        "errors": "- Декоративный шрифт на длинных абзацах.\n- Серый текст на сером.\n- Пять разных размеров «на глаз».",
        "hw": "Стиль кнопки .btn (акцент, hover).",
        "hwcrit": "Два шрифта, карточки в стиле гайда, кнопка есть.",
        "practicum": "типографика, оформление",
        "kind": "lesson",
    },
    {
        "id": "A11-css-animations",
        "title": "CSS-анимации и hover-состояния",
        "project": "MusicHub",
        "goal": "Добавляет hover карточки и анимацию эквалайзера/пульса на обложке хита. Учитывает prefers-reduced-motion.",
        "screen": "Наведение поднимает карточку. Обложка хита дышит. Плеер-кнопка светится.",
        "topic": "- transition на transform и box-shadow.\n- :hover и :focus-visible.\n- @keyframes pulse.\n- prefers-reduced-motion: animation: none.",
        "practice": "1. transition 200ms.\n2. hover: translateY(-4px).\n3. keyframes на .eq-bar или обложке.\n4. focus-visible outline.\n5. Отключить анимацию в media reduced.",
        "errors": "- Анимация на всё подряд, рябит.\n- Нет focus, только hover — клавиатура слепнет.\n- animation бесконечная и тяжёлая на 10 карточках.",
        "hw": "Анимация кнопки Play (scale).",
        "hwcrit": "hover+focus, одна keyframes, reduced-motion учтён.",
        "practicum": "декорирование",
        "kind": "lesson",
    },
    {
        "id": "A12-showcase-musichub",
        "title": "Showcase: адаптивный MusicHub",
        "project": "MusicHub",
        "goal": "Презентация адаптивной версии. Показать телефон и десктоп.",
        "screen": "MusicHub в двух ширинах + одна анимация.",
        "topic": "Сценарий демо: открыл 360px, потом 1200px, навёл на карточку, кликнул якорь.",
        "practice": "Таймер 6 минут. DevTools открыт заранее.",
        "errors": "- Показывают только десктоп.\n- Анимация сломана в Safari — иметь запасной transition.",
        "hw": "Список багов после фидбека, 3 пункта.",
        "hwcrit": "Must-have проекта 2 закрыт.",
        "practicum": "повтор CSS",
        "kind": "showcase",
    },
    {
        "id": "A13-js-basics",
        "title": "JS-база: переменные, типы, функции",
        "project": "PulseBeat",
        "goal": "Пишет скрипт, который считает очки в консоли: переменные, функция addScore.",
        "screen": "Пустая страница игры + DevTools Console показывает 0 → 10.",
        "topic": "- script defer vs в конце body.\n- let/const, не var.\n- number, string, boolean.\n- function declaration и вызов.\n- console.log как рентген, не как продукт.",
        "practice": "1. app.js + defer.\n2. const MAX_LIVES = 3.\n3. let score = 0.\n4. function addScore(n).\n5. Вызвать дважды, логи.",
        "errors": "- script в head без defer — не находит DOM потом.\n- Сравнение = вместо ===.\n- Боятся консоли.",
        "hw": "Функция takeHit(), уменьшает lives.",
        "hwcrit": "Файл js подключён, две функции, без var.",
        "practicum": "переменные, функции JS",
        "kind": "lesson",
    },
    {
        "id": "A14-conditions-loops-arrays",
        "title": "Условия, циклы, массивы",
        "project": "PulseBeat",
        "goal": "Хранит площадки в массиве, циклом рендерит их названия в консоль, if по жизням.",
        "screen": "В консоли список площадок. if lives===0 → 'game over'.",
        "topic": "- array literals, push, length.\n- for...of.\n- if/else.\n- Не учим map ещё, достаточно цикла.",
        "practice": "1. Массив pads = ['A','S','D','F'].\n2. for...of log.\n3. if score>20 message.\n4. lives check.\n5. Проговорить вслух порядок строк.",
        "errors": "- Путают массив и объект.\n- Бесконечный while — не даём while на этом уроке.",
        "hw": "Массив из 4 сообщений победы, вывести случайное (Math.random).",
        "hwcrit": "Массив, цикл, условие.",
        "practicum": "массивы, условия",
        "kind": "lesson",
    },
    {
        "id": "A15-dom",
        "title": "DOM: найти, изменить, создать элемент",
        "project": "PulseBeat",
        "goal": "Выводит счёт на страницу, создаёт кнопки-площадки из массива.",
        "screen": "Четыре кнопки и span#score.",
        "topic": "- document.querySelector.\n- textContent vs innerHTML (не вставляем сырой HTML от игрока).\n- createElement, append.\n- classList.add.",
        "practice": "1. #score в HTML.\n2. JS пишет score в span.\n3. Цикл создаёт кнопки.\n4. Контейнер #pads.\n5. Без innerHTML для имён.",
        "errors": "- querySelector null — скрипт слишком рано.\n- innerHTML в цикле каждую миллисекунду.",
        "hw": "Элемент #lives, рисует сердца текстом.",
        "hwcrit": "Счёт на экране, кнопки из JS.",
        "practicum": "DOM, элементы страницы",
        "kind": "lesson",
    },
    {
        "id": "A16-events",
        "title": "События: click и клавиатура",
        "project": "PulseBeat",
        "goal": "Клик по площадке и клавиши A S D F начисляют очки.",
        "screen": "Живая реакция кнопок, keydown в игре.",
        "topic": "- addEventListener click.\n- event.target.\n- keydown, event.key.\n- prevent повторного bind в цикле — вешаем один раз.",
        "practice": "1. click → addScore(1).\n2. Подсветка кнопки классом is-hit.\n3. keydown A/S/D/F.\n4. Игнор клавиш если игра не стартовала (флаг).\n5. Не используем onclick в HTML.",
        "errors": "- Слушатель внутри другого слушателя → двойной счёт.\n- keyCode устарел, учим key.",
        "hw": "Пробел ставит игру на паузу (пока флаг).",
        "hwcrit": "Мышь и клавиатура работают.",
        "practicum": "события",
        "kind": "lesson",
    },
    {
        "id": "A17-game-loop",
        "title": "Игровой цикл, счёт, CSS-анимация удара",
        "project": "PulseBeat",
        "goal": "Раунд 30 секунд: случайная площадка вспыхивает, успел кликнуть — очко, нет — жизнь.",
        "screen": "Таймер, вспышки, game over, рестарт.",
        "topic": "- setInterval / clearInterval.\n- Math.floor random index.\n- CSS class is-active + animation.\n- Кнопка restart обнуляет state.",
        "practice": "1. startGame().\n2. interval 800ms выбирает pad.\n3. hit / miss.\n4. timer 30s.\n5. restart.",
        "errors": "- Несколько interval параллельно.\n- Нет clearInterval.\n- Слишком быстрый темп для 12 лет — 800–1000ms.",
        "hw": "Уровни: каждые 10 очков interval короче, но не меньше 400ms.",
        "hwcrit": "Старт, конец, рестарт, анимация вспышки.",
        "practicum": "таймеры на уровне идеи, DOM",
        "kind": "lesson",
    },
    {
        "id": "A18-showcase-game",
        "title": "Showcase: JS-игра со счётом",
        "project": "PulseBeat",
        "goal": "Живое демо раунда. Рассказ: состояние, события, таймер.",
        "screen": "Полный раунд на проекторе.",
        "topic": "Показать код startGame на 20 секунд, не весь файл.",
        "practice": "Демо 5–7 мин, один зритель играет.",
        "errors": "- Игра не рестартится.\n- Звук обязательным не делаем (наушники/класс).",
        "hw": "Записать 3 улучшения к магазину/порталу.",
        "hwcrit": "Must-have проекта 3.",
        "practicum": "повтор JS",
        "kind": "showcase",
    },
    {
        "id": "A19-form-validation",
        "title": "Формы и валидация на JS",
        "project": "MerchShop",
        "goal": "Форма заказа не уходит пустой: имя и email проверяются, ошибка на экране.",
        "screen": "Красные подсказки под полями, кнопка не «молча мёртвая».",
        "topic": "- input.value.trim().\n- Простая проверка email через includes('@').\n- setCustomValidity или свой span.error.\n- submit + preventDefault пока не ок.",
        "practice": "1. Форма заказа.\n2. preventDefault.\n3. Проверки.\n4. Показать ошибку.\n5. Успех: сообщение «заказ принят» (пока без сервера).",
        "errors": "- alert на каждую букву.\n- Проверка только CSS :invalid без текста.\n- email без @ проходит.",
        "hw": "Поле телефона: только цифры и +.",
        "hwcrit": "Пустая форма не «успех», ошибки видны.",
        "practicum": "формы, условия",
        "kind": "lesson",
    },
    {
        "id": "A20-json-localstorage",
        "title": "Объекты, JSON, localStorage",
        "project": "MerchShop",
        "goal": "Сохраняет корзину массивом объектов в localStorage и читает её после F5.",
        "screen": "Добавил товар, обновил страницу — товар на месте.",
        "topic": "- object {id, title, price}.\n- JSON.stringify/parse.\n- localStorage setItem/getItem.\n- try/catch на parse.",
        "practice": "1. saveCart / loadCart.\n2. Ключ pulse.cart.\n3. F5 проверка.\n4. Кнопка «очистить».\n5. Не храним функции в JSON.",
        "errors": "- Забыли stringify — [object Object].\n- parse от null.\n- Огромные картинки в storage.",
        "hw": "Сохранять ещё имя покупателя draft.",
        "hwcrit": "F5 не убивает корзину.",
        "practicum": "объекты, JSON",
        "kind": "lesson",
    },
    {
        "id": "A21-cart",
        "title": "Корзина: добавить / удалить / сумма",
        "project": "MerchShop",
        "goal": "Полный сценарий корзины: qty, удаление строки, сумма.",
        "screen": "Список позиций, сумма, кнопки +/−/удалить.",
        "topic": "- Найти товар по id.\n- Если есть — qty++ иначе push.\n- reduce или цикл для суммы.\n- Перерисовка renderCart().",
        "practice": "1. addToCart(id).\n2. removeLine(id).\n3. changeQty.\n4. render.\n5. Пустая корзина — текст «пусто».",
        "errors": "- Дубли строк вместо qty.\n- Сумма строкой «199»+«199»=«199199».\n- Не вызывают render после изменения.",
        "hw": "Кнопка «купить ещё» скроллит к каталогу.",
        "hwcrit": "Добавление, удаление, сумма числом.",
        "practicum": "массивы, DOM",
        "kind": "lesson",
    },
    {
        "id": "A22-fetch-mock",
        "title": "fetch и мок-данные каталога",
        "project": "MerchShop",
        "goal": "Каталог грузится из products.json через fetch, карточки строятся в JS.",
        "screen": "6 карточек с сервера-файла, без хардкода в HTML.",
        "topic": "- fetch(url).then или async/await база.\n- response.ok.\n- Создавать карточки из данных.\n- Жить через Live Server, не file:// (CORS).",
        "practice": "1. products.json.\n2. fetch.\n3. map в карточки.\n4. Ошибка загрузки — сообщение.\n5. Кнопка «в корзину» с data-id.",
        "errors": "- Открыли как file:// — fetch падает.\n- Не проверяют ok.\n- Жёстко прошили 6 карточек и fetch «для галочки».",
        "hw": "Поле поиска фильтрует уже загруженный массив (filter).",
        "hwcrit": "Каталог из JSON, корзина жива.",
        "practicum": "запросы к данным на уровне идеи",
        "kind": "lesson",
    },
    {
        "id": "A23-nav-glue",
        "title": "Склейка: музыка + игра + магазин",
        "project": "MerchShop",
        "goal": "Общая шапка портала на трёх страницах, единый CSS, ссылки не 404.",
        "screen": "PulseLab nav: Музыка / Игра / Магазин.",
        "topic": "- Относительные ссылки.\n- Общий styles.css.\n- Единый header копипастой пока (шаблоны будут во Flask).\n- Главная-заглушка index-хаб.",
        "practice": "1. index.html хаб.\n2. Скопировать nav.\n3. Проверить все ссылки.\n4. Активный пункт меню классом.\n5. Favicon общий.",
        "errors": "- Ссылки в абсолютных путях учителя.\n- Разный header на каждой странице без нужды.",
        "hw": "Футер с тремя ссылками везде.",
        "hwcrit": "Три раздела открываются, стиль общий.",
        "practicum": "структура сайта",
        "kind": "lesson",
    },
    {
        "id": "A24-showcase-shop",
        "title": "Showcase: магазин с корзиной",
        "project": "MerchShop",
        "goal": "Сценарий покупки на проекторе + F5 + валидация формы.",
        "screen": "Каталог → корзина → форма.",
        "topic": "Показать кусок loadCart и fetch, не весь магазин.",
        "practice": "Демо 6 минут. Гость добавляет товар.",
        "errors": "- JSON не лежит рядом, fetch 404 на чужом ноуте — проверить пути.",
        "hw": "Баг-лист к Flask-спринту.",
        "hwcrit": "Must-have проекта 4.",
        "practicum": "повтор JS+формы",
        "kind": "showcase",
    },
    {
        "id": "A25-flask-hello",
        "title": "Что такое сервер. Flask hello",
        "project": "Flask-финал",
        "goal": "Поднимает venv, ставит Flask, открывает http://127.0.0.1:5000 и видит «PulseLab жив».",
        "screen": "Страница из Python, не из файла.",
        "topic": "- Браузер просит, сервер отвечает.\n- venv, pip install flask.\n- app = Flask(__name__), @app.route, return строку/html.\n- flask --app app run --debug.\n- Это не замена Python, который они знают: это библиотека.",
        "practice": "1. python -m venv .venv.\n2. activate (Windows PowerShell ExecutionPolicy при необходимости).\n3. pip install flask.\n4. app.py hello.\n5. Открыть URL.",
        "errors": "- pip в системный Python, потом «модуля нет».\n- Запустили файл, он сразу закрылся — нет app.run и нет flask run.\n- Порт занят.",
        "hw": "Маршрут /about возвращает имя ученика.",
        "hwcrit": "Сервер стартует, / открывается.",
        "practicum": "нет, только наш урок",
        "kind": "lesson",
    },
    {
        "id": "A26-flask-routes",
        "title": "Роуты и несколько страниц",
        "project": "Flask-финал",
        "goal": "Четыре маршрута: дом, музыка, игра, магазин. Пока простой HTML-строкой или render заглушки.",
        "screen": "Переключение URL руками.",
        "topic": "- Один app — много route.\n- Имена функций уникальны.\n- 404 если опечатка в URL.\n- url_for позже, сначала явные пути.",
        "practice": "1. / /music /game /shop.\n2. Разный заголовок на каждой.\n3. Ссылки <a href> между ними.\n4. Сломать URL, увидеть 404 Werkzeug.\n5. debug reload.",
        "errors": "- Два route на одну функцию без понимания.\n- Windows: путают слэши.",
        "hw": "Роут /contact.",
        "hwcrit": "4+ страницы открываются.",
        "practicum": "нет",
        "kind": "lesson",
    },
    {
        "id": "A27-jinja",
        "title": "Jinja: шаблоны, наследование, циклы",
        "project": "Flask-финал",
        "goal": "base.html + music.html. Цикл по списку треков из Python.",
        "screen": "Одинаковая шапка на страницах, список треков из render_template.",
        "topic": "- templates/ папка.\n- {% extends %}, {% block %}.\n- {{ variable }}.\n- {% for t in tracks %}.\n- Данные живут в Python, HTML их показывает.",
        "practice": "1. base.html nav.\n2. index.html extends.\n3. Список dict треков в app.py.\n4. for в шаблоне.\n5. title через block.",
        "errors": "- templates не в той папке.\n- {{ }} внутри {% %}.\n- Безопасность: не учим |safe на пользовательском вводе.",
        "hw": "Страница shop крутит 3 товара из списка Python.",
        "hwcrit": "Наследование работает, цикл выводит 3+ элемента.",
        "practicum": "нет",
        "kind": "lesson",
    },
    {
        "id": "A28-flask-static",
        "title": "Статика: CSS и JS в Flask",
        "project": "Flask-финал",
        "goal": "Подключает styles.css и app.js через url_for('static', filename=...). MusicHub выглядит как в блоке CSS.",
        "screen": "Тёмная тема PulseLab на серверных страницах.",
        "topic": "- static/css, static/js.\n- url_for не хардкод /static/... вразнобой, но путь понятен.\n- Кеш в debug.\n- Перенос эталона CSS в static.",
        "practice": "1. Перенести css.\n2. link в base.html.\n3. JS defer.\n4. Картинки в static/img.\n5. Ctrl+F5.",
        "errors": "- Оставили file:// css.\n- Неверный filename.",
        "hw": "Фавиконка из static.",
        "hwcrit": "Стили применяются через Flask.",
        "practicum": "нет",
        "kind": "lesson",
    },
    {
        "id": "A29-flask-forms",
        "title": "Формы POST и flash-сообщения",
        "project": "Flask-финал",
        "goal": "Контактная форма POST, сервер читает имя, flash «спасибо», redirect.",
        "screen": "Отправил форму — зелёная плашка.",
        "topic": "- request.method, request.form.\n- secret_key для session/flash.\n- redirect + url_for.\n- GET форму показывать, POST обрабатывать.",
        "practice": "1. contact.html form post.\n2. route GET/POST.\n3. flash.\n4. get_flashed_messages в base.\n5. Пустое имя — ошибка flash.",
        "errors": "- Нет secret_key — flash не работает.\n- Форма GET случайно.\n- Не делают redirect, двойной POST при обновлении.",
        "hw": "Сохранять обращения в список в памяти процесса (пропадут при рестарте — это обсуждаем).",
        "hwcrit": "POST работает, flash виден.",
        "practicum": "нет",
        "kind": "lesson",
    },
    {
        "id": "A30-flask-json",
        "title": "JSON-ответ и fetch с фронта",
        "project": "Flask-финал",
        "goal": "Роут /api/hits отдаёт jsonify. Главная JS рисует хиты.",
        "screen": "Хиты появляются без перезагрузки шаблона, из API.",
        "topic": "- jsonify.\n- fetch('/api/hits').\n- JSON vs HTML: два языка ответа.\n- DevTools Network.",
        "practice": "1. Данные hits в python list.\n2. /api/hits.\n3. fetch + then/await.\n4. Нарисовать 3 карточки.\n5. Смотреть статус 200.",
        "errors": "- fetch на чужой домен без нужды.\n- Шаблон и API расходятся данными — сверяем один источник.",
        "hw": "API /api/products для магазина.",
        "hwcrit": "Network показывает JSON, карточки из fetch.",
        "practicum": "нет",
        "kind": "lesson",
    },
    {
        "id": "A31-assemble-hub",
        "title": "Сборка MediaGameHub на шаблонах",
        "project": "Flask-финал",
        "goal": "Игра и магазин встроены: шаблоны + старый JS. Навигация единая.",
        "screen": "Портал: музыка, игра PulseBeat, корзина (localStorage ещё ок).",
        "topic": "- Не выкидываем клиентский JS: сервер отдаёт страницу, JS оживляет.\n- Идентичные id, которые ждёт скрипт.\n- Общий base.",
        "practice": "1. game.html + script.\n2. shop.html + cart js.\n3. Прогон трёх сценариев.\n4. Баг-лист.\n5. README черновик.",
        "errors": "- Два разных css конфликтуют.\n- JS ищет #pads, в шаблоне другое имя.",
        "hw": "Починить 3 бага из списка.",
        "hwcrit": "Три раздела живые под Flask.",
        "practicum": "нет",
        "kind": "lesson",
    },
    {
        "id": "A32-polish",
        "title": "Доводка: 404, адаптив, README",
        "project": "Flask-финал",
        "goal": "Своя страница 404, адаптив не развалился, README на 3 команды.",
        "screen": "Кривой URL → брендовый 404 PulseLab.",
        "topic": "- @app.errorhandler(404).\n- Прогон 360px.\n- README: venv, install, run.\n- .gitignore: venv, pycache.",
        "practice": "1. 404.html.\n2. gitignore.\n3. README.\n4. Адаптив проверка.\n5. Друг запускает по README (парами).",
        "errors": "- README «просто открой html».\n- venv в git.",
        "hw": "Скрин 404 и скрин телефона.",
        "hwcrit": "Чужой человек поднимает по README.",
        "practicum": "нет",
        "kind": "lesson",
    },
    {
        "id": "A33-rehearsal",
        "title": "Репетиция защиты финала A",
        "project": "Flask-финал",
        "goal": "Прогон 5-минутного рассказа по рубрике. Список вопросов.",
        "screen": "Таймер, один зритель ломает форму.",
        "topic": "Структура защиты как в templates/diploma.md, укороченная.",
        "practice": "Парные репетиции 2 круга. Преподаватель — 3 жёстких вопроса: что такое шаблон, зачем Flask, где живут данные.",
        "errors": "- Читают код с первой строки.\n- Не могут запустить сервер с нуля.",
        "hw": "Карточка выступления на бумаге/в notes, 8 строк.",
        "hwcrit": "Карточка сдана, сервер стартует за 2 минуты.",
        "practicum": "нет",
        "kind": "lesson",
    },
    {
        "id": "A34-defense",
        "title": "Защита финала блока A",
        "project": "Flask-финал",
        "goal": "Публичная защита MediaGameHub v1.",
        "screen": "Демо сценария + 2 вопроса комиссии (преподаватель + 1 ученик).",
        "topic": "Рубрика: работает / шаблоны / JS / рассказ / самостоятельность.",
        "practice": "Очередь. Пока один защищается, другие заполняют лист фидбека «1 сильно / 1 улучшить».",
        "errors": "- Чинить прод на защите 20 минут — стоп, показываем что есть.",
        "hw": "Каникулы: список хотелок к блоку B, 5 пунктов.",
        "hwcrit": "Защита проведена, фидбек выдан.",
        "practicum": "нет",
        "kind": "defense",
    },
]

B = [
    ("B01-git-pages", "Git, ветки, GitHub Pages", "Studio", "Создаёт репозиторий MediaGameHub, первый push, gh-pages для статики UI-кита.", "Репозиторий с README на GitHub.", "- init, status, add, commit, branch.\n- remote, push.\n- Pages для static preview.\n- .gitignore уже есть.", "1. git init.\n2. Коммит эталона A как архива или чистый ui-kit.\n3. GitHub remote.\n4. Pages.\n5. Ссылка в чат группы.", "- commit -a без понимания.\n- token светит в чат — только HTTPS login через credential manager.", "Сделать .gitignore идеальным.", "Есть remote, минимум 2 коммита.", "нет, наш урок", "lesson"),
    ("B02-vite-modules", "Модули ES и Vite", "Studio", "Поднимает Vite-проект, import/export двух модулей кнопки и темы.", "localhost:5173 с кнопкой из модуля.", "- npm create vite.\n- type=module.\n- import { button } from './ui.js'.\n- Зачем сборка.", "1. create vite vanilla.\n2. Два модуля.\n3. CSS import.\n4. npm run dev.\n5. build.", "- Смешали Flask static и Vite без прокси слишком рано.\n- node не установлен — чек в начале.", "Модуль heading.js.", "Dev-сервер стартует, import работает.", "организация кода", "lesson"),
    ("B03-components-no-fw", "Компонентное мышление без фреймворка", "Studio", "Функция renderCard(data) возвращает DOM, список карт из массива.", "Каталог UI-кита: 3 компоненты.", "- Компонент = функция + контракт данных.\n- Не React в 13 лет как must.\n- Один файл — одна роль.", "1. card.js.\n2. nav.js.\n3. page собирает.\n4. Не дублировать HTML строками без нужды — DOM API или шаблон-строка осознанно.\n5. Пропсы-объект.", "- Бог-файл app.js 800 строк.", "Компонент Badge.", "3 функции-компонента.", "нет", "lesson"),
    ("B04-motion", "Анимации: keyframes и WAAPI база", "Motion-UI", "Кнопка Ripple через CSS, появление карточки через Element.animate.", "Живой UI-кит, не цирк.", "- Когда CSS, когда JS animation.\n- duration, easing.\n- Не блокировать reduced-motion.", "1. Ripple css.\n2. animate() 1 пример.\n3. Тоггл темы с transition.\n4. Чек reduced.\n5. Запись gif не обязательна.", "- Анимация 5 секунд на каждый клик.", "Стейт hover у input.", "Две анимации, reduced учтён.", "декор CSS", "lesson"),
    ("B05-a11y", "Доступность: фокус, aria, контраст", "Motion-UI", "Клавиатурный проход меню, aria-label на иконках, контраст 4.5:1.", "Tab по всем кнопкам виден.", "- focus-visible.\n- кнопка vs div-клик.\n- alt и aria-label.\n- contrast checker вручную.", "1. Убрать div onclick.\n2. skip-link.\n3. aria на плеере.\n4. Контраст.\n5. Проход только клавиатурой.", "- outline:none без замены.", "Подписи к иконкам.", "Клавиатура проходит сценарий.", "доступность на уровне идеи", "lesson"),
    ("B06-showcase-uikit", "Showcase: UI-кит PulseLab", "Motion-UI", "Страница-галерея компонентов + Pages-ссылка.", "Живой styleguide.", "Демо: кнопка, карточка, нав, motion, tab-фокус.", "6 минут. Показать GitHub Pages.", "- Нет ссылки на Pages.", "Исправить a11y-замечания.", "Must-have UI-кита: 5 компонентов.", "повтор", "showcase"),
    ("B07-async", "async/await и ошибки сети", "API-клиент", "Обёртка request(url) с try/catch, показ ошибки пользователю.", "Индикатор ошибки при оффлайне.", "- Promise в одном абзаце.\n- async/await.\n- Не ловить ошибку молча.", "1. async function load.\n2. try/catch.\n3. UI error box.\n4. Кнопка retry.\n5. DevTools offline.", "- then-ад и await вместе без нужды.", "Таймаут через AbortController optional челлендж.", "Ошибка видна, retry есть.", "JS асинхронность если есть в бесплатной части", "lesson"),
    ("B08-rest-contract", "REST глазами фронта", "API-клиент", "Читает контракт hits: GET список, GET :id. Рисует таблицу полей.", "Документ api.md в репо.", "- GET/POST.\n- статус 200/404/400/500.\n- JSON ключи стабильны.", "1. Описать контракт на доске.\n2. api.md.\n3. Примеры JSON.\n4. Не менять ключи как попало.\n5. Обсудить идемпотентность GET.", "- Выдумывают GraphQL.", "Нарисовать 404 JSON {error}.", "api.md сдан.", "нет", "lesson"),
    ("B09-list-detail", "Список и карточка из API", "API-клиент", "Список хитов, клик — детальная (мок json-server или Flask заглушка из A).", "Два экрана: list/detail.", "- Маршрутизация пока query ?id=.\n- Шарить load функции.", "1. Список.\n2. Деталь.\n3. Кнопка назад.\n4. 404 id.\n5. Скелетон простой.", "- Всё в одном HTML без состояния.", "Пустой список — empty state.", "Список и деталь работают.", "DOM+fetch", "lesson"),
    ("B10-ui-states", "Состояния UI: loading / empty / error", "API-клиент", "Три состояния не путаются. Спиннер не вечный.", "Явные экраны состояний.", "- Один source of truth status.\n- Не три флага врага друг другу.", "1. status = 'loading'.\n2. render switch.\n3. empty массив.\n4. error.\n5. disable кнопок в loading.", "- Спиннер поверх ошибки.", "Тост «повторная попытка».", "Три состояния воспроизводимы.", "нет", "lesson"),
    ("B11-client-filter", "Фильтры и поиск на клиенте", "API-клиент", "Поиск по имени трека, фильтр жанра, без нового запроса (пока).", "Живой фильтр.", "- filter + includes lowerCase.\n- debounce 200ms челлендж.", "1. input search.\n2. select genre.\n3. applyFilters.\n4. empty.\n5. Сброс.", "- Фильтр бьёт API 60 раз в секунду.", "Сортировка по году.", "Поиск работает по загруженным данным.", "массивы", "lesson"),
    ("B12-showcase-catalog", "Showcase: каталог из API", "API-клиент", "Демо list/detail/filter/error.", "Полный клиент.", "Показать Network и offline.", "Гость вводит поиск.", "- Мок только в памяти без fetch — не защита этого спринта.", "Записать 3 вопроса к своему API.", "Must-have каталога.", "повтор", "showcase"),
    ("B13-flask-as-api", "Flask-приложение как API", "PulseAPI", "Отделяем html-роуты от /api/*. Blueprint можно упомянуть, но must — префикс.", "Пустой JSON {ok:true} на /api/health.", "- API = контракт, не страница.\n- return jsonify.\n- debug и reload.", "1. /api/health.\n2. Папка api мысль.\n3. Проверка через браузер и через fetch.\n4. Статус 200.\n5. Лог.", "- render_template на /api.", "Добавить version в health.", "health жив.", "нет", "lesson"),
    ("B14-get-api", "JSON API: GET списков и записи", "PulseAPI", "GET /api/tracks и /api/tracks/<id>.", "JSON в Network.", "- Динамический route.\n- abort(404).\n- данные из list dict.", "1. Данные в python.\n2. list endpoint.\n3. detail.\n4. 404.\n5. фронт переключить на этот URL.", "- id строка vs int.", "Пагинация не нужна, limit=20 челлендж.", "Оба GET работают.", "нет", "lesson"),
    ("B15-post-api", "POST: новый скор / заказ", "PulseAPI", "POST /api/scores JSON body, append в список, ответ 201.", "Игра шлёт скор.", "- request.get_json.\n- валидация полей.\n- 400 если нет name/score.", "1. post route.\n2. fetch POST headers Content-Type.\n3. Обновить лидерборд.\n4. Неверный JSON.\n5. DevTools payload.", "- GET с побочным эффектом.", "POST заказа магазина.", "201 и запись появляется в GET.", "нет", "lesson"),
    ("B16-session-lite", "Сессия-лайт: cookie и dict", "PulseAPI", "Логин учебный: POST /api/login, session['user']. /api/me.", "После логина «привет, Имя».", "- flask session.\n- secret_key.\n- это НЕ прод-безопасность, говорим честно.\n- пароли не хешируем в этом уроке, учебный pin.", "1. login form.\n2. session.\n3. me.\n4. logout.\n5. Разговор: почему так нельзя в банке.", "- «Мы сделали настоящую авторизацию» — нет, учебная.", "Страница кабинета.", "login/me/logout работают.", "нет", "lesson"),
    ("B17-cors-vite", "CORS и связка Vite-dev с Flask", "PulseAPI", "Фронт 5173, API 5000, flask-cors, proxy как альтернатива.", "Каталог с живого API.", "- Same origin.\n- CORS заголовки.\n- vite server.proxy /api.", "1. Показать ошибку CORS.\n2. Починить proxy ИЛИ cors.\n3. fetch относительный /api.\n4. Документировать запуск двух процессов.\n5. Скрипт в README.", "- cors=* в проде как единственный навык.", "npm script concurrently челлендж.", "Два сервера, fetch 200.", "нет", "lesson"),
    ("B18-showcase-api", "Showcase: свой API + фронт", "PulseAPI", "Сценарий: логин, список, пост скора.", "Full demo.", "Показать 3 запроса в Network.", "Комиссия ломает POST без JSON.", "- API только в Postman, фронт мёртв — мало.", "Починить замечания.", "Контракт + UI.", "повтор", "showcase"),
    ("B19-leaderboard", "Лидерборд через API", "Fullstack", "Таблица топ-10, сортировка на Python.", "Игра → API → таблица.", "- sorted key=lambda.\n- отдаём уже отсортированное.\n- фронт только рисует.", "1. endpoint /api/scores.\n2. sort reverse.\n3. UI table.\n4. После game over POST.\n5. refresh списка.", "- Сортировка только в JS при живом сервере — дубли.", "Медали топ-3.", "Скор появляется в таблице.", "python списки", "lesson"),
    ("B20-auth-lite", "Авторизация-лайт: логин, кто я", "Fullstack", "UI логина, спрятать «кабинет» гостю.", "Нав меняется.", "- Условный рендер.\n- Не доверять только скрытой кнопке: сервер тоже проверяет.", "1. Форма логина.\n2. me fetch.\n3. nav.\n4. Гость видит публичное.\n5. Сообщение ошибки pin.", "- Спрятали кнопку и думаем, что защитили API.", "Remember me не делаем.", "Гость и пользователь различаются.", "нет", "lesson"),
    ("B21-protected-route", "Защищённый роут и кабинет", "Fullstack", "GET /api/cabinet 401 без сессии, 200 с данными заказов.", "Кабинет заказов.", "- Декоратор login_required учебный.\n- 401 JSON.", "1. decorator.\n2. cabinet.\n3. фронт редирект на логин.\n4. 401 обработка.\n5. Тест руками.", "- 302 HTML на API.", "Список последних скоров в кабинете.", "401 и 200 воспроизводимы.", "нет", "lesson"),
    ("B22-server-validation", "Валидация на сервере", "Fullstack", "Сервер режет score<0, пустое имя, слишком длинные строки.", "POST мусора → 400 с текстом.", "- Никогда не верить только фронту.\n- Единый формат {error, field}.", "1. Правила.\n2. 400.\n3. Фронт показывает field.\n4. Позитивный кейс.\n5. Обсуждение читерства в игре.", "- Валидация только alert.", "Лимит 5 заказов в сессии челлендж.", "Негативные тесты руками пройдены.", "нет", "lesson"),
    ("B23-deploy-docs", "Деплой: Pages + инструкция бэка", "Fullstack", "Фронт на Pages (сборка Vite), бэк — инструкция Render/Fly или локальный ngrok как демо учителя.", "Публичная ссылка на фронт.", "- Статика vs процесс Python.\n- env переменные секрет.\n- Честно: бесплатный хостинг меняется, важна инструкция.", "1. vite build.\n2. Pages.\n3. README backend.\n4. Не коммитить secret_key в открытый вид — вынести в env пример.\n5. Видео 30 сек запуска локально.", "- Жёстко прошить API localhost в проде Pages — сразу сломается. Показать import.meta.env.", "env пример .env.example.", "Фронт открывается по HTTPS ссылке.", "нет", "lesson"),
    ("B24-showcase-fullstack", "Showcase: fullstack-срез", "Fullstack", "Сквозной сценарий портала.", "Музыка, игра, скор, кабинет.", "Network + UI.", "Гость ломает, пользователь проходит.", "- Только фронт без API.", "Список долгов диплома.", "Срез живой.", "повтор", "showcase"),
    ("B25-python-inside-flask", "Python, который они знают, внутри Flask", "Python-bridge", "Вынести бизнес-логику из роутов в functions.py: чисто Python, тесты мышкой.", "Роут тонкий, логика читаемая.", "- MVC-лайт: route / logic / data.\n- Импорт своих модулей.", "1. functions.py top_tracks.\n2. route вызывает.\n3. print debug аккуратно.\n4. Не писать циклы в jinja сложные.\n5. Повторить срезы списков.", "- Вся логика в шаблоне.", "Модуль cart.py.", "Логика без Flask-импортов в functions.py.", "python функции", "lesson"),
    ("B26-json-files", "Данные в JSON-файлах", "Python-bridge", "tracks.json на диске, read/write с pathlib, аккуратная запись.", "Рестарт сервера не убивает треки/скоры.", "- open encoding utf-8.\n- dump ensure_ascii False.\n- гонки не решаем, говорим что есть.", "1. load_tracks.\n2. save_scores.\n3. Рестарт проверка.\n4. Файл в .gitignore если персональный? нет, учебные данные коммитим sample.\n5. backup copy челлендж.", "- Пишут JSON руками с запятой в конце.", "sample-data README.", "Данные переживают рестарт.", "файлы python", "lesson"),
    ("B27-top3-algorithm", "Мини-алгоритм: топ-3", "Python-bridge", "Топ-3 треков по plays или скоров. Объясняют алгоритм вслух.", "Виджет топ-3 на главной.", "- sorted[:3].\n- сложность словами «перебрали все».\n- ничьи.", "1. Функция top3.\n2. Тест глазами 5 строк данных.\n3. API /api/top.\n4. UI.\n5. Ничья — по имени.", "- Хардкод трёх id.", "Топ жанра.", "Виджет совпадает с ручным подсчётом.", "python сортировка", "lesson"),
    ("B28-pytest-lite", "Тесты API глазами ученика", "Python-bridge", "2–3 теста pytest + Flask test client: health, 404, post validation.", "pytest зелёный.", "- зачем тесты.\n- assert.\n- app.test_client().", "1. pip pytest.\n2. test_health.\n3. test_404.\n4. test_bad_post.\n5. npm не нужен.", "- Тесты зависят от живого порта 5000.", "test_top3 unit без flask.", "pytest проходит.", "нет", "lesson"),
    ("B29-ux-polish", "Полировка UX диплома", "Диплом", "Пустые состояния, кнопки, фокус, мобильный прогон всего портала.", "Чек-лист UX закрыт.", "- 10 эвристик очень коротко: понятно, отзыв, ошибка, выход.", "1. Пройти 360px.\n2. Все формы.\n3. Игра.\n4. Кабинет.\n5. Баг-лист приоритетов.", "- Новые фичи вместо полировки.", "Починить топ-5 багов.", "Нет блокеров на телефоне.", "нет", "lesson"),
    ("B30-docs-video", "Документация и видео-демо 60 сек", "Диплом", "README диплома + запись экрана 60 секунд без монтажа-оперы.", "Ссылка на видео (диск/unlisted).", "- Структура README.\n- Команды copy-paste.\n- Не читать README на защите — это страховка.", "1. README шаблон.\n2. env.example.\n3. Запись демо.\n4. Скрин архитектуры boxes.\n5. Лицензия учебная.", "- Видео 12 минут.", "Схема в mermaid в README.", "README + видео сданы.", "нет", "lesson"),
    ("B31-draft-defense", "Черновая защита в классе", "Диплом", "Полный прогон, жёсткие вопросы, таймер.", "Замечания в журнал.", "Рубрика диплома.", "2 круга по 7 минут.", "- Дописывают фичи во время чужой защиты.", "Исправить блокеры.", "Есть список блокеров.", "нет", "lesson"),
    ("B32-diploma-prep", "Диплом: подготовка и репетиция", "Диплом", "Чек-лист must-have закрыт, речь выучена, серверы поднимаются с нуля.", "Карточка защиты.", "templates/diploma.md.", "Чек-лист в парах. Холодный старт машины.", "- «У меня дома работало».", "Спать. Не кодить всю ночь.", "Чек-лист подписан преподавателем.", "нет", "diploma"),
    ("B33-diploma-defense", "Диплом: защита", "Диплом", "Официальная защита MediaGameHub v2.", "Комиссия: преподаватель, возможно куратор.", "5–7 минут + вопросы.", "Очередь, фидбек-листы.", "- Чинить деплой 30 минут публично — запасной локальный запуск.", "Нет домашки.", "Защита состоялась.", "нет", "diploma"),
    ("B34-diploma-retro", "Диплом: рефлексия и портфолио", "Диплом", "Письмо себе, обновлённый GitHub, список навыков, праздник.", "README портфолио.", "- Что забрать в следующий проект.\n- Как показывать родителям.", "1. 5 навыков.\n2. 2 провала.\n3. Ссылка портфолио.\n4. Скрин отзывов группы.\n5. Архив проекта.", "- Удалить репозиторий «потому что стыдно».", "Поделиться ссылкой с семьёй.", "Рефлексия сдана.", "нет", "diploma"),
]


def write_lesson(block: str, item: dict):
    folder = COURSE / f"block-{block}" / "lessons" / item["id"]
    folder.mkdir(parents=True, exist_ok=True)
    kind = item["kind"]
    header_kind = {"lesson": "обычный", "showcase": "showcase", "defense": "защита", "diploma": "диплом"}[kind]
    teacher = f"""# Урок {item["id"].split("-")[0]}. {item["title"]}

- Блок: {block.upper()}
- Тип: {header_kind}
- Длительность: 120 минут
- Минипроект: {item["project"]}
- Практикум (опционально): {item["practicum"]}

## Цель урока

{item["goal"]}

## Результат на экране

{item["screen"]}

## План 120 минут

| Минуты | Блок | Преподаватель | Ученики |
| --- | --- | --- | --- |
| 0–15 | Разогрев и повтор | 3 вопроса по прошлому файлу | Отвечают, открывают проект |
| 15–60 | Live-coding | Одна идея, кодим вслух | Повторяют |
| 60–100 | Практика | Чек-лист, хождение по залу | Шаги практики |
| 100–120 | Демо и домашка | 2–3 показа, критерии | Записывают ДЗ |

Для showcase/защиты: использовать тайминг из `course/templates/showcase.md` или `diploma.md` вместо таблицы выше.

## Новая тема

{item["topic"]}

## Практика в классе

{item["practice"]}

## Частые ошибки 12–14 лет

{item["errors"]}

## Домашка

См. `homework.md`. Ориентир 45–70 минут.

## Эталон

`etalon/` в этой папке и/или эталон спринта в `block-{block}/projects/`.

## Для преподавателя

- Must-have дня: цель урока без nice-to-have.
- Рано закончил: челлендж из PROJECT.md.
- Отстаёт: закрыть только must-have шаги 1–3 практики.
"""
    (folder / "teacher.md").write_text(teacher, encoding="utf-8")
    hw = f"""# Домашка {item["id"].split("-")[0]} · 45–70 минут

{item["hw"]}

## Критерии приёмки

{item["hwcrit"]}

## Формат сдачи

Файлы проекта + короткий скрин результата. Для Flask — ещё и команды запуска в README, если менялись.
"""
    (folder / "homework.md").write_text(hw, encoding="utf-8")
    (folder / "starter").mkdir(exist_ok=True)
    (folder / "etalon").mkdir(exist_ok=True)
    readme = folder / "etalon" / "README.md"
    if not readme.exists():
        readme.write_text(
            f"Эталон урока {item['id']}: см. также спринт `block-{block}/projects/` и teacher.md.\n",
            encoding="utf-8",
        )


def from_tuple(t):
    keys = ["id", "title", "project", "goal", "screen", "topic", "practice", "errors", "hw", "hwcrit", "practicum", "kind"]
    return dict(zip(keys, t))


def main():
    for item in A:
        write_lesson("a", item)
    for t in B:
        write_lesson("b", from_tuple(t))
    print("wrote", len(A), "A remaining +", len(B), "B")


if __name__ == "__main__":
    main()
