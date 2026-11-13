# -*- coding: utf-8 -*-
"""
Генератор презентации урока 8 · Шаблоны и статика: переезд сайта на сервер.
Запуск из этой папки:  python generate-slides.py
Результат: A08-шаблоны-и-статика.pptx

Стиль: живая, мемная подача для подростков 12–14 лет.
Картинки: img/spaghetti-monster.jpg, img/jinja-taxi-meme.jpg, img/404-meme.jpg

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


def footer(slide, num, total=11):
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
            "PULSELAB · BLOCK A · LESSON 08", size=17, color=ACCENT, bold=True)
    textbox(s, Inches(0.8), Inches(2.1), Inches(11.7), Inches(1.7),
            "Шаблоны и статика:\nпереезд сайта на сервер 🚀", size=46,
            color=TEXT, bold=True)
    textbox(s, Inches(0.8), Inches(4.15), Inches(11.0), Inches(0.8),
            "Как отдать красивый HTML с картинками и стилями, не сломав Python.",
            size=22, color=MUTED)
    footer(s, 1)


# ---------- 02 · Retrieval ----------

def s02():
    s = add_slide()
    header(s, "ВСПОМНИМ ПРОШЛОЕ! 🧠", "На прошлом уроке наш сервер делал вот так:")

    card(s, Inches(0.7), Inches(1.8), Inches(11.9), Inches(1.2), fill=CARD_CODE)
    textbox(s, Inches(1.0), Inches(2.1), Inches(11.0), Inches(0.8),
            'return "<h1>PulseLab жив</h1>"', size=32, color=TEXT, font="Consolas")

    textbox(s, Inches(0.7), Inches(3.5), Inches(11.9), Inches(0.5),
            "Вопросы на засыпку:", size=24, color=ACCENT, bold=True)
    
    bullets(s, Inches(1.0), Inches(4.2), Inches(11.0), Inches(2.0), [
        "Кто превратил эти теги в красивый заголовок?",
        "А что если нам нужно вернуть сайт на 500 строк кода? Удобно ли это писать в одной строке?",
    ], size=22, space=15)
    
    footer(s, 2)


# ---------- 03 · Проблема ----------

def s03():
    s = add_slide()
    header(s, "ХЬЮСТОН, У НАС ПРОБЛЕМА 🚨", "Писать HTML внутри Python — это боль!")
    
    picture(s, "spaghetti-monster.jpg", Inches(7.0), Inches(1.5), Inches(5.5))
    
    bullets(s, Inches(0.7), Inches(2.0), Inches(6.0), Inches(3.0), [
        "Ломаются кавычки (один class=\"card\" и всё взрывается 💥)",
        "Нет подсветки HTML (всё сливается в один цвет)",
        "Полный хаос (код и дизайн перемешаны в кашу)",
    ], size=20, space=15)
    
    prompt(s, "Решение: Разделяй и властвуй! Код отдельно, верстка отдельно.")
    footer(s, 3)


# ---------- 04 · Архитектура ----------

def s04():
    s = add_slide()
    header(s, "ИДЕАЛЬНЫЙ ПОРЯДОК 📁", "У Flask есть строгие правила, где что должно лежать")

    card(s, Inches(0.7), Inches(1.7), Inches(6.0), Inches(4.5), fill=CARD_CODE)
    textbox(s, Inches(1.0), Inches(1.9), Inches(5.5), Inches(4.0),
            "my_site/\n"
            "  app.py\n"
            "  templates/\n"
            "    index.html\n"
            "  static/\n"
            "    css/styles.css\n"
            "    img/cover.svg",
            size=20, color=TEXT, font="Consolas")

    bullets(s, Inches(7.0), Inches(2.0), Inches(5.5), Inches(3.0), [
        "app.py 🐍 <- Мозг (логика на Python)",
        "templates/ 📄 <- Лицо (HTML-шаблоны)",
        "static/ 🎨 <- Одежда (стили, картинки, звуки)",
        "#(Спойлер: назовешь папку template без s — всё сломается!)",
    ], size=20, space=15)

    footer(s, 4)


# ---------- 05 · render_template ----------

def s05():
    s = add_slide()
    header(s, "МАГИЯ FLASK 🪄", "render_template()")

    card(s, Inches(0.7), Inches(1.7), Inches(11.9), Inches(3.5), fill=CARD_CODE)
    textbox(s, Inches(1.0), Inches(2.0), Inches(11.0), Inches(3.0),
            "from flask import Flask, render_template\n\n"
            "app = Flask(__name__)\n\n"
            "@app.route(\"/\")\n"
            "def home():\n"
            "    return render_template(\"index.html\")",
            size=22, color=TEXT, font="Consolas")

    prompt(s, "Flask сам пойдет в папку templates/ и найдет там index.html. Умно, да? 😎")
    footer(s, 5)


# ---------- 06 · Jinja2 ----------

def s06():
    s = add_slide()
    header(s, "ЗНАКОМЬТЕСЬ: JINJA2 🥷", "Движок, который читает шаблоны")
    
    picture(s, "jinja-taxi-meme.jpg", Inches(0.7), Inches(1.5), Inches(6.0))
    
    bullets(s, Inches(7.0), Inches(2.5), Inches(5.5), Inches(3.0), [
        "Берет ваш HTML",
        "Вставляет в него данные прямо из Python",
        "Отдает готовый результат браузеру",
        "#(Кстати, Jinja по-японски — «храм» ⛩️)",
    ], size=22, space=15)

    footer(s, 6)


# ---------- 07 · Ловушка ----------

def s07():
    s = add_slide()
    header(s, "ЛОВУШКА 😱", "Где мои стили?!")
    
    picture(s, "404-meme.jpg", Inches(7.0), Inches(1.5), Inches(5.5))
    
    textbox(s, Inches(0.7), Inches(1.7), Inches(6.0), Inches(0.5),
            "Если написать в HTML по старинке:", size=20, color=TEXT)
    
    card(s, Inches(0.7), Inches(2.3), Inches(6.0), Inches(0.8), fill=CARD_CODE)
    textbox(s, Inches(0.9), Inches(2.5), Inches(5.6), Inches(0.5),
            "<link rel=\"stylesheet\" href=\"style.css\">", size=16, color=DANGER, font="Consolas")
    
    bullets(s, Inches(0.7), Inches(3.5), Inches(6.0), Inches(2.0), [
        "На главной / браузер запросит /style.css (404!)",
        "На странице /item/track запросит /item/style.css (404!)",
    ], size=18, space=10)
    
    prompt(s, "Вывод: Статическим файлам нужен надежный GPS-навигатор! 🧭")
    footer(s, 7)


# ---------- 08 · url_for ----------

def s08():
    s = add_slide()
    header(s, "СПЕШИТ НА ПОМОЩЬ 🦸‍♂️", "url_for()")

    card(s, Inches(0.7), Inches(1.7), Inches(11.9), Inches(3.5), fill=CARD_CODE)
    textbox(s, Inches(1.0), Inches(2.0), Inches(11.0), Inches(3.0),
            "<!-- Подключаем стили как профи -->\n"
            "<link rel=\"stylesheet\" href=\"{{ url_for('static', filename='css/styles.css') }}\">\n\n"
            "<!-- Подключаем картинку -->\n"
            "<img src=\"{{ url_for('static', filename='img/cover.svg') }}\" alt=\"Обложка\">",
            size=18, color=TEXT, font="Consolas")

    prompt(s, "Главное правило: filename — это путь ВНУТРИ папки static/. Не пиши слово static дважды! 🚫")
    footer(s, 8)


# ---------- 09 · Сеть ----------

def s09():
    s = add_slide()
    header(s, "СЕТЬ ПОД МИКРОСКОПОМ 🔬", "Один клик — целая очередь HTTP-запросов")

    bullets(s, Inches(0.7), Inches(2.0), Inches(11.9), Inches(3.0), [
        "1. GET / -> 200 OK (Ура, приехал HTML!)",
        "2. GET /static/css/styles.css -> 200 OK (Подъехали стили 🎨)",
        "3. GET /static/img/cover.svg -> 200 OK (Картинка на месте 🖼️)",
    ], size=24, space=20)

    prompt(s, "Открой DevTools -> Network (Сеть): все полоски должны быть зелеными! 🟢")
    footer(s, 9)


# ---------- 10 · Checkpoint ----------

def s10():
    s = add_slide()
    header(s, "CHECKPOINT 🎯", "Давайте проверим, кто не спал")

    bullets(s, Inches(0.7), Inches(2.0), Inches(11.9), Inches(4.0), [
        "В какую папку Flask смотрит, когда видит render_template?",
        "Что подставит Flask вместо {{ url_for('static', filename='css/styles.css') }}?",
        "Почему нельзя писать filename='static/css/styles.css'?",
    ], size=24, space=25)

    footer(s, 10)


# ---------- 11 · Практика ----------

def s11():
    s = add_slide()
    header(s, "ПРАКТИКА: YOU DO 💻", "Миссия: Переезд на сервер!")

    bullets(s, Inches(0.7), Inches(1.8), Inches(11.9), Inches(4.0), [
        "Создай папки templates/ и static/ (внутри static сделай css и img).",
        "В app.py отдай index.html через render_template.",
        "Все стили и картинки подключи через url_for('static', ...).",
        "Адрес в браузере должен быть http://127.0.0.1:5000/ (никаких file://!).",
        "В DevTools -> Network нет красных ошибок 404.",
    ], size=22, space=15)

    prompt(s, "Exit ticket: Скинь скриншот своего работающего сайта на 127.0.0.1:5000 в чат группы! 📸")
    footer(s, 11)


def build():
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    for fn in (s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11):
        fn()

    out = HERE / "A08-шаблоны-и-статика.pptx"
    prs.save(out)
    print(f"Готово: {out.name} ({len(prs.slides)} слайдов)")


if __name__ == "__main__":
    build()
