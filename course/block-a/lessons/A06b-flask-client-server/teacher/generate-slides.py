# -*- coding: utf-8 -*-
"""
Генератор презентации урока 7 · Клиент и сервер: как браузер получает страницу.
Запуск из этой папки:  python generate-slides.py
Результат: A06b-кто-отвечает-браузеру.pptx

Стиль: инженерная подача для подростков 12–14 лет. Заголовок слайда —
утверждение, тело — определение, контраст, код или критерий проверки.
Аналогии остаются только в устной лекции, не в терминах на экране.

Картинки: img/poster-vs-cafe.jpg, hall-vs-kitchen.jpg,
request-envelope.jpg. Подписи — на слайдах.

Требуется: pip install python-pptx
"""

from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

HERE = Path(__file__).resolve().parent
IMG = HERE / "img"

BG = RGBColor(0x0B, 0x0F, 0x1A)
CARD = RGBColor(0x14, 0x1A, 0x2A)
CARD_CODE = RGBColor(0x0E, 0x24, 0x1D)
TEXT = RGBColor(0xF4, 0xF1, 0xEA)
MUTED = RGBColor(0x9A, 0xA3, 0xB8)
ACCENT = RGBColor(0x2E, 0xE6, 0xA6)
DANGER = RGBColor(0xFF, 0x6B, 0x6B)
BORDER = RGBColor(0x2A, 0x33, 0x48)

SW, SH = Inches(13.333), Inches(7.5)

prs = Presentation()
prs.slide_width = SW
prs.slide_height = SH
BLANK = prs.slide_layouts[6]


def add_slide():
    slide = prs.slides.add_slide(BLANK)
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG
    bg.line.fill.background()
    bg.shadow.inherit = False
    return slide


def textbox(slide, x, y, w, h, text, size=24, color=TEXT, bold=False,
            align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, font="Segoe UI"):
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.name = font
    return box


def bullets(slide, x, y, w, h, items, size=22, color=TEXT, space=10):
    """items: строки. '#'-префикс — приглушённая сноска без маркера."""
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    first = True
    for item in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_after = Pt(space)
        if item.startswith("#"):
            p.text = item[1:].strip()
            p.runs[0].font.color.rgb = MUTED
            p.runs[0].font.size = Pt(size - 4)
            p.runs[0].font.bold = False
        else:
            p.text = "•  " + item
            p.runs[0].font.color.rgb = color
            p.runs[0].font.size = Pt(size)
        p.runs[0].font.name = "Segoe UI"
    return box


def header(slide, kicker, title):
    textbox(slide, Inches(0.7), Inches(0.32), Inches(11.2), Inches(0.32),
            kicker, size=15, color=ACCENT, bold=True)
    textbox(slide, Inches(0.7), Inches(0.64), Inches(12.0), Inches(0.72),
            title, size=31, color=TEXT, bold=True)


def card(slide, x, y, w, h, fill=CARD):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = BORDER
    shape.line.width = Pt(1.25)
    shape.shadow.inherit = False
    return shape


def footer(slide, num, total=16):
    textbox(slide, Inches(10.6), Inches(7.05), Inches(2.2), Inches(0.32),
            f"{num:02d} / {total}", size=13, color=MUTED, align=PP_ALIGN.RIGHT)


def picture(slide, name, x, y, w):
    path = IMG / name
    if not path.exists():
        raise FileNotFoundError(path)
    return slide.shapes.add_picture(str(path), x, y, width=w)


def prompt(slide, text):
    textbox(slide, Inches(0.7), Inches(6.55), Inches(12.0), Inches(0.42),
            text, size=17, color=ACCENT, bold=True)


# ---------- 01 · Титул ----------

def s01():
    s = add_slide()
    textbox(s, Inches(0.8), Inches(1.65), Inches(11.7), Inches(0.4),
            "PULSELAB · BLOCK A · LESSON 07", size=17, color=ACCENT, bold=True)
    textbox(s, Inches(0.8), Inches(2.1), Inches(11.7), Inches(1.7),
            "Клиент и сервер:\nкак браузер получает страницу", size=46,
            color=TEXT, bold=True)
    textbox(s, Inches(0.8), Inches(4.15), Inches(11.0), Inches(0.8),
            "Первый сервер на Flask: HTTP-запрос, маршрут, функция-обработчик и ответ.",
            size=22, color=MUTED)
    textbox(s, Inches(0.8), Inches(6.35), Inches(11.0), Inches(0.4),
            "От локального файла Pulse FM — к программе, которая формирует страницу по запросу",
            size=15, color=MUTED)
    footer(s, 1)


# ---------- 02 · Стартовая точка ----------

def s02():
    s = add_slide()
    header(s, "СТАРТОВАЯ ТОЧКА", "До сих пор страницу отдавал готовый файл")

    card(s, Inches(0.7), Inches(1.65), Inches(5.85), Inches(4.35))
    textbox(s, Inches(1.0), Inches(1.9), Inches(5.25), Inches(0.45),
            "Модель A · локальный файл", size=19, color=MUTED, bold=True)
    bullets(s, Inches(1.0), Inches(2.5), Inches(5.25), Inches(3.1), [
        "браузер открывает index.html с диска",
        "адрес начинается с file://",
        "содержимое задано заранее",
    ], size=19, space=10)

    card(s, Inches(6.8), Inches(1.65), Inches(5.85), Inches(4.35), fill=CARD_CODE)
    textbox(s, Inches(7.1), Inches(1.9), Inches(5.25), Inches(0.45),
            "Модель B · сервер", size=19, color=ACCENT, bold=True)
    bullets(s, Inches(7.1), Inches(2.5), Inches(5.25), Inches(3.1), [
        "браузер отправляет HTTP-запрос",
        "адрес начинается с http://",
        "программа формирует ответ по запросу",
    ], size=19, space=10)

    prompt(s, "Проверка: какая модель описывает ваш Pulse FM сегодня?")
    footer(s, 2)


# ---------- 03 · Две модели доставки ----------

def s03():
    s = add_slide()
    header(s, "КОНТРАСТ", "Файл уже готов. Ответ формируется по запросу")
    picture(s, "poster-vs-cafe.jpg", Inches(2.66), Inches(1.42), Inches(8.0))
    textbox(s, Inches(2.66), Inches(6.08), Inches(3.9), Inches(0.35),
            "Локальный файл: HTML уже на диске", size=14, color=MUTED, bold=True)
    textbox(s, Inches(6.6), Inches(6.08), Inches(4.05), Inches(0.35),
            "Сервер: ответ создаётся по запросу", size=14, color=ACCENT,
            bold=True, align=PP_ALIGN.RIGHT)
    prompt(s, "Какая модель нужна, если содержимое зависит от запроса?")
    footer(s, 3)


# ---------- 04 · Frontend / backend ----------

def s04():
    s = add_slide()
    header(s, "АРХИТЕКТУРА", "Frontend и backend разделяет HTTP")
    picture(s, "hall-vs-kitchen.jpg", Inches(0.7), Inches(1.55), Inches(7.35))

    card(s, Inches(8.25), Inches(1.55), Inches(4.35), Inches(4.15))
    bullets(s, Inches(8.45), Inches(1.72), Inches(4.0), Inches(3.85), [
        "FRONTEND — браузер",
        "HTML/CSS: структура и вид",
        "рендеринг полученного HTML",
        "BACKEND — Python + Flask",
        "приём HTTP-запроса",
        "формирование тела ответа",
    ], size=16, space=7)

    prompt(s, "Граница ответственности: HTTP-запрос → HTTP-ответ")
    footer(s, 4)


# ---------- 05 · URL ----------

def s05():
    s = add_slide()
    header(s, "АДРЕС ЗАПРОСА", "URL: протокол, хост, порт и путь")
    picture(s, "request-envelope.jpg", Inches(0.55), Inches(1.55), Inches(6.5))
    bullets(s, Inches(7.2), Inches(1.65), Inches(5.6), Inches(4.5), [
        "http — протокол передачи",
        "127.0.0.1 — loopback: этот компьютер",
        "5000 — порт процесса Flask",
        "/radio — путь, ключ выбора маршрута",
        "#http://127.0.0.1:5000/radio",
    ], size=20, space=11)
    prompt(s, "Почему этот адрес не откроет вашу страницу с другого компьютера?")
    footer(s, 5)


# ---------- 06 · HTTP ----------

def s06():
    s = add_slide()
    header(s, "ПРОТОКОЛ HTTP", "Запрос задаёт действие, ответ — результат")

    card(s, Inches(0.7), Inches(1.65), Inches(5.85), Inches(4.35))
    textbox(s, Inches(1.0), Inches(1.9), Inches(5.25), Inches(0.45),
            "Запрос клиента", size=19, color=ACCENT, bold=True)
    textbox(s, Inches(1.0), Inches(2.55), Inches(5.25), Inches(1.5),
            "GET /radio HTTP/1.1\nHost: 127.0.0.1:5000",
            size=19, color=TEXT, font="Consolas")
    textbox(s, Inches(1.0), Inches(4.35), Inches(5.25), Inches(1.2),
            "Метод GET: получить ресурс по указанному пути.",
            size=17, color=MUTED)

    card(s, Inches(6.8), Inches(1.65), Inches(5.85), Inches(4.35), fill=CARD_CODE)
    textbox(s, Inches(7.1), Inches(1.9), Inches(5.25), Inches(0.45),
            "Ответ сервера", size=19, color=ACCENT, bold=True)
    textbox(s, Inches(7.1), Inches(2.55), Inches(5.25), Inches(1.7),
            "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<h1>Night Circuit</h1>",
            size=17, color=TEXT, font="Consolas")
    textbox(s, Inches(7.1), Inches(4.7), Inches(5.25), Inches(0.9),
            "Нет маршрута — 404 Not Found. Это тоже корректный ответ.",
            size=16, color=MUTED)

    footer(s, 6)


# ---------- 07 · Жизненный цикл ----------

def s07():
    s = add_slide()
    header(s, "ЖИЗНЕННЫЙ ЦИКЛ ЗАПРОСА", "Один GET проходит пять шагов")
    steps = [
        ("1", "Браузер", "формирует\nGET /radio"),
        ("2", "Flask", "принимает запрос\nна порту 5000"),
        ("3", "Маршрут", "сопоставляет путь\nс обработчиком"),
        ("4", "Функция", "выполняет код\nи возвращает строку"),
        ("5", "Браузер", "рендерит HTML\nиз тела ответа"),
    ]
    w = Inches(2.15)
    gap = Inches(0.38)
    x0 = Inches(0.55)
    for i, (num, title, note) in enumerate(steps):
        x = x0 + i * (w + gap)
        card(s, x, Inches(2.0), w, Inches(3.3))
        textbox(s, x, Inches(2.2), w, Inches(0.5),
                num, size=22, color=ACCENT, bold=True, align=PP_ALIGN.CENTER)
        textbox(s, x + Inches(0.1), Inches(2.85), w - Inches(0.2), Inches(0.65),
                title, size=19, color=TEXT, bold=True, align=PP_ALIGN.CENTER)
        textbox(s, x + Inches(0.1), Inches(3.65), w - Inches(0.2), Inches(1.15),
                note, size=15, color=MUTED, align=PP_ALIGN.CENTER)
    for i in range(len(steps) - 1):
        x = x0 + i * (w + gap) + w
        textbox(s, x, Inches(3.35), gap, Inches(0.4),
                "›", size=20, color=ACCENT, bold=True, align=PP_ALIGN.CENTER)
    prompt(s, "На каком шаге создаётся HTML для /radio?")
    footer(s, 7)


# ---------- 08 · Код Flask ----------

def s08():
    s = add_slide()
    header(s, "FLASK", "Маршрут связывает URL с функцией-обработчиком")

    card(s, Inches(0.7), Inches(1.65), Inches(6.6), Inches(4.55), fill=CARD_CODE)
    textbox(s, Inches(1.0), Inches(1.9), Inches(6.0), Inches(4.0),
            "from flask import Flask\n\n"
            "app = Flask(__name__)\n\n\n"
            "@app.route(\"/radio\")\n"
            "def radio():\n"
            "    return \"<h1>Night Circuit</h1>\"",
            size=18, color=TEXT, font="Consolas")

    card(s, Inches(7.55), Inches(1.65), Inches(5.1), Inches(4.55))
    bullets(s, Inches(7.8), Inches(1.9), Inches(4.65), Inches(4.0), [
        "@app.route — регистрация правила URL",
        "radio() — функция-обработчик пути",
        "return — тело HTTP-ответа",
        "#один путь — один обработчик",
    ], size=17, space=10)

    prompt(s, "Что изменить, чтобы обработчик отвечал по другому URL?")
    footer(s, 8)


# ---------- 09 · Тело ответа ----------

def s09():
    s = add_slide()
    header(s, "ТЕЛО ОТВЕТА", "Браузер рендерит ответ, а не файл Python")

    card(s, Inches(0.7), Inches(1.75), Inches(5.85), Inches(4.3))
    textbox(s, Inches(1.0), Inches(2.0), Inches(5.25), Inches(0.45),
            "Текстовый ответ", size=19, color=MUTED, bold=True)
    textbox(s, Inches(1.0), Inches(2.7), Inches(5.25), Inches(0.8),
            'return "PulseLab"', size=23, color=TEXT, font="Consolas")
    textbox(s, Inches(1.0), Inches(3.9), Inches(5.25), Inches(1.4),
            "Браузер покажет строку как обычный текст.",
            size=18, color=MUTED)

    card(s, Inches(6.8), Inches(1.75), Inches(5.85), Inches(4.3), fill=CARD_CODE)
    textbox(s, Inches(7.1), Inches(2.0), Inches(5.25), Inches(0.45),
            "HTML-ответ", size=19, color=ACCENT, bold=True)
    textbox(s, Inches(7.1), Inches(2.7), Inches(5.25), Inches(0.8),
            'return "<h1>PulseLab</h1>"', size=20, color=TEXT, font="Consolas")
    textbox(s, Inches(7.1), Inches(3.9), Inches(5.25), Inches(1.4),
            "Браузер разберёт разметку и отобразит заголовок.",
            size=18, color=MUTED)

    prompt(s, "Кто интерпретирует тег <h1>: Flask или браузер?")
    footer(s, 9)


# ---------- 10 · Маршруты дня ----------

def s10():
    s = add_slide()
    header(s, "ПРАКТИЧЕСКИЙ РЕЗУЛЬТАТ", "Три маршрута — три обработчика")
    routes = [
        ("/", "home()", "Проверка: сервер запущен\nи отвечает"),
        ("/radio", "radio()", "Готовый пример:\nмаршрут и обработчик"),
        ("/about", "about()", "Самостоятельно: имя\nи описание станции"),
    ]
    for i, (path, func, note) in enumerate(routes):
        x = Inches(0.7) + i * Inches(4.15)
        fill = CARD_CODE if i == 2 else CARD
        card(s, x, Inches(1.85), Inches(3.95), Inches(3.7), fill=fill)
        textbox(s, x + Inches(0.3), Inches(2.1), Inches(3.4), Inches(0.65),
                path, size=27, color=ACCENT, bold=True)
        textbox(s, x + Inches(0.3), Inches(2.95), Inches(3.4), Inches(0.65),
                func, size=22, color=TEXT, bold=True, font="Consolas")
        textbox(s, x + Inches(0.3), Inches(3.9), Inches(3.4), Inches(1.1),
                note, size=16, color=MUTED)
    prompt(s, "Ваша задача — третий маршрут. Первые два уже работают на стенде.")
    footer(s, 10)


# ---------- 11 · Термины ----------

def s11():
    s = add_slide()
    header(s, "ТЕРМИНЫ", "Словарь клиент-серверной архитектуры")
    words = [
        ("Клиент", "программа, инициирующая запрос\n\nЗдесь: браузер"),
        ("Сервер", "программа, принимающая запросы\n\nЗдесь: Flask-приложение"),
        ("Маршрут", "правило связи URL\nс обработчиком\n\n@app.route(...)"),
        ("Ответ", "статус + заголовки + тело\n\nСегодня тело — HTML"),
    ]
    for i, (word, note) in enumerate(words):
        x = Inches(0.7) + i * Inches(3.15)
        card(s, x, Inches(1.95), Inches(3.0), Inches(3.55))
        textbox(s, x + Inches(0.2), Inches(2.25), Inches(2.6), Inches(0.65),
                word, size=25, color=ACCENT, bold=True, align=PP_ALIGN.CENTER)
        textbox(s, x + Inches(0.2), Inches(3.15), Inches(2.6), Inches(1.85),
                note, size=15, color=TEXT, align=PP_ALIGN.CENTER)
    prompt(s, "Чем маршрут отличается от функции-обработчика?")
    footer(s, 11)


# ---------- 12 · Контрольная точка ----------

def s12():
    s = add_slide()
    header(s, "КОНТРОЛЬНАЯ ТОЧКА", "Проследите запрос к /radio до кода")
    card(s, Inches(0.7), Inches(1.7), Inches(11.9), Inches(4.45))
    bullets(s, Inches(1.15), Inches(1.95), Inches(11.0), Inches(3.9), [
        "1.  Назовите клиент, хост, порт и путь в URL",
        "2.  Какое правило Flask выберет обработчик?",
        "3.  Что вернёт функция и что сделает браузер с ответом?",
        "#Критерий: запрос → маршрут → функция → ответ → рендеринг",
    ], size=23, space=13)
    footer(s, 12)


# ---------- 13 · Лабораторная работа ----------

def s13():
    s = add_slide()
    header(s, "ЛАБОРАТОРНАЯ РАБОТА", "Реализуйте маршрут /about")
    card(s, Inches(0.7), Inches(1.65), Inches(11.9), Inches(4.5))
    bullets(s, Inches(1.15), Inches(1.9), Inches(11.0), Inches(4.0), [
        "Сервер запущен из student/starter; открыт http://127.0.0.1:5000/",
        "Добавлен обработчик about() для пути /about",
        "Ответ содержит ваше имя и описание вашей станции",
        "Изменение return отображается после обновления страницы",
        "#Pulse FM во Flask не переносим: проверяем механизм запроса",
    ], size=21, space=11)
    footer(s, 13)


# ---------- 14 · Диагностика ----------

def s14():
    s = add_slide()
    header(s, "ДИАГНОСТИКА", "Страница не открывается: проверяйте по слоям")
    items = [
        ("1", "Среда", "Flask установлен в .venv, из которого запускается сервер"),
        ("2", "Процесс", "сервер запущен, терминал не закрыт"),
        ("3", "Сеть", "адрес 127.0.0.1; порт 5000 не занят другим процессом"),
        ("4", "Приложение", "маршрут зарегистрирован, файл сохранён, страница обновлена"),
    ]
    for i, (num, title, note) in enumerate(items):
        y = Inches(1.6) + i * Inches(1.05)
        card(s, Inches(0.7), y, Inches(11.9), Inches(0.95))
        textbox(s, Inches(0.95), y + Inches(0.18), Inches(0.7), Inches(0.55),
                num, size=22, color=DANGER, bold=True)
        textbox(s, Inches(1.8), y + Inches(0.14), Inches(2.6), Inches(0.65),
                title, size=21, color=TEXT, bold=True, anchor=MSO_ANCHOR.MIDDLE)
        textbox(s, Inches(4.6), y + Inches(0.14), Inches(7.6), Inches(0.65),
                note, size=18, color=MUTED, anchor=MSO_ANCHOR.MIDDLE)
    prompt(s, "Порядок важен: сначала процесс и адрес, затем код маршрута.")
    footer(s, 14)


# ---------- 15 · Итог ----------

def s15():
    s = add_slide()
    header(s, "ИТОГ ЗАНЯТИЯ", "Объяснить без подсказок")
    card(s, Inches(0.7), Inches(1.7), Inches(11.9), Inches(4.45))
    bullets(s, Inches(1.15), Inches(1.95), Inches(11.0), Inches(3.9), [
        "Чем открытие file:// отличается от запроса http://",
        "Как Flask находит обработчик по пути /about",
        "Почему <h1> в теле ответа становится заголовком на экране",
        "#Артефакт: скриншот /about с видимой адресной строкой",
    ], size=23, space=13)
    footer(s, 15)


# ---------- 16 · Следующий шаг ----------

def s16():
    s = add_slide()
    header(s, "СЛЕДУЮЩИЙ ШАГ", "Завтра тот же сайт отвечает сервер")

    card(s, Inches(0.7), Inches(1.75), Inches(5.85), Inches(4.1))
    textbox(s, Inches(1.0), Inches(2.0), Inches(5.25), Inches(0.45),
            "Урок 8", size=17, color=ACCENT, bold=True)
    textbox(s, Inches(1.0), Inches(2.65), Inches(5.25), Inches(1.2),
            "templates и static", size=28, color=TEXT, bold=True)
    textbox(s, Inches(1.0), Inches(4.15), Inches(5.25), Inches(1.2),
            "Свой Pulse FM открывается на 127.0.0.1:5000 вместе со стилями и картинками.",
            size=17, color=MUTED)

    card(s, Inches(6.8), Inches(1.75), Inches(5.85), Inches(4.1), fill=CARD_CODE)
    textbox(s, Inches(7.1), Inches(2.0), Inches(5.25), Inches(0.45),
            "Дальше до урока 13", size=17, color=ACCENT, bold=True)
    textbox(s, Inches(7.1), Inches(2.65), Inches(5.25), Inches(1.2),
            "Данные, шапка, POST, 404", size=26, color=TEXT, bold=True)
    textbox(s, Inches(7.1), Inches(4.15), Inches(5.25), Inches(1.2),
            "Каскад CSS в этот спринт не входит. Сначала сервер отдаёт уже сделанный сайт.",
            size=17, color=MUTED)

    prompt(s, "Домашнее задание: персонализировать /radio и зафиксировать команды запуска.")
    footer(s, 16)


def build():
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    for fn in (s01, s02, s03, s04, s05, s06, s07, s08,
               s09, s10, s11, s12, s13, s14, s15, s16):
        fn()

    out = HERE / "A06b-кто-отвечает-браузеру.pptx"
    prs.save(out)
    print(f"Готово: {out.name} ({len(prs.slides)} слайдов)")


if __name__ == "__main__":
    build()
