# Импорт данных в Mongo

URL: https://practicum.yandex.ru/learn/kids-web/courses/fca180a1-4dc7-4494-818a-9536e5cf7aeb/sprints/190125/topics/53bf9e76-ef5e-415d-9751-d5a9e2c2d7f1/lessons/df455e24-747f-4724-b3e5-4d308f30dc2a/

Course: Основы бэкенда

Topic: Работа с сервером

Type: web

---

# Импорт данных в Mongo

Сейчас, если ты откроешь браузер и в адресной строке введёшь свой домен, то увидишь страницу с окном авторизации 👇🏻

![](https://pictures.s3.yandex.net/resources/9_1_1715787489.jpg)

![](https://pictures.s3.yandex.net/resources/Worn-Ass-Semi-Gloss_43_1715787529.jpg)

## Экспортируем коллекции из Compass

Чтобы создать в MongoDB коллекции с документами категорий, игр и юзеров, нужно сначала их экспортировать из Compass в виде JSON-файлов. 

Для этого в корневой папке проекта создай папку `compass-export`, в которую будут сохранены все JSON-файлы с коллекциями. Далее перейди в Compass и экспортируй оттуда коллекции. Для этого нажми на вкладку коллекции, а затем на кнопку `Export Data` 👇🏻

![](https://pictures.s3.yandex.net/resources/5_2_1715787543.jpg)

Затем выбери пункт меню `Export the full collection` 👇🏻

![](https://pictures.s3.yandex.net/resources/10_1_1715787556.jpg)

И в качестве формата файла, в котором будет экспортирована коллекция, выбери JSON 👇🏻

![](https://pictures.s3.yandex.net/resources/16_1715787576.jpg)

Гуд! В конце нажми на кнопку `Export…`. Далее ты увидишь окно, где тебе будет предложено выбрать папку, куда нужно сохранить файл. Выбери `compass-export`, которую мы создали ранее.

Да, в результате в проекте в папке `compass-export` у тебя будет три JSON-файла 👇🏻

- `pindie.categories.json`
- `pindie.games.json`
- `pindie.users.json`

## Загружаем коллекции на виртуальную машину

Файлы, которые мы только что получили из Compass, можно положить на виртуальную машину при помощи `git`

В корневой папке проекта выполни команду 👇🏻

```bash
git add .
```

Теперь в будущий коммит попадут все изменения, которые мы сделали на данный момент, в том числе и папка `compass-export` со всем её содержимым. Далее выполни сам коммит 👇🏻

```bash
git commit -m "коллекции для mongodb"
```

И запушь его в репозиторий 👇🏻

```bash
git push
```

Теперь подключись к удалённой машине по `ssh` — как это сделать, мы показывали в уроке «Работа с сервером по SSH». Далее в терминале нужно перейти в папку с проектом командой 👇🏻

```bash
cd <имя папки с проектом>
```

Загрузи последние изменения из удалённого репозитория, куда мы только что запушили JSON-файлы с коллекциями. Для этого, находясь в папке проекта, выполни команду 👇🏻

```bash
git pull
```

## Импортируем коллекции в MongoDB

Сейчас, когда JSON-файлы с коллекциями уже есть на виртуальной машине, настало время их импортировать в MongoDB, которая запущена на этой машине. Для этого, находясь в корневой папке проекта, перейди в папку с JSON-файлами коллекций 👇🏻

```bash
cd compass-export
```

И выполни последовательно три команды:

- Импорт коллекции игр 👇🏻

```bash
sudo mongoimport --db pindie --collection games --file pindie.games.json --jsonArray
```

- Импорт коллекции категорий 👇🏻

```bash
sudo mongoimport --db pindie --collection categories --file pindie.categories.json --jsonArray
```

- Импорт коллекции пользователей 👇🏻

```bash
sudo mongoimport --db pindie --collection users --file pindie.users.json --jsonArray
```

Лови скринкаст для наглядности 👀

{video:https://code.s3.yandex.net/kids-web/vids/M4/M4T4/Screen_Recording_2024-05-03_at_17.41.23.mp4|controls:true|autoplay:0|pip:false|controlsList:nodownload}