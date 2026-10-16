# -*- coding: utf-8 -*-
"""
Генератор презентации A03 · Типографика и обложка трека.
Запуск:  python generate-slides.py
Результат: A03-типографика-и-медиа.pptx (в той же папке).

Требуется: pip install python-pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# ---------- Палитра PulseLab ----------
BG = RGBColor(0x0B, 0x0F, 0x1A)      # тёмно-синий фон
CARD = RGBColor(0x14, 0x1A, 0x2A)    # карточка
TEXT = RGBColor(0xF4, 0xF1, 0xEA)    # основной текст
MUTED = RGBColor(0x9A, 0xA3, 0xB8)   # приглушённый
ACCENT = RGBColor(0x2E, 0xE6, 0xA6)  # зелёный акцент
DANGER = RGBColor(0xFF, 0x6B, 0x6B)  # красный для «жвачки»
BORDER = RGBColor(0x2A, 0x33, 0x48)  # границы

SW, SH = Inches(13.333), Inches(7.5)  # широкий экран 16:9

prs = Presentation()
prs.slide_width = SW
prs.slide_height = SH
BLANK = prs.slide_layouts[6]


# ---------- Хелперы ----------

def add_slide():
    """Пустой слайд с тёмным фоном."""
    slide = prs.slides.add_slide(BLANK)
    bg = slide.shapes.add_shape(1, 0, 0, SW, SH)  # 1 = прямоугольник
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG
    bg.line.fill.background()
    bg.shadow.inherit = False
    return slide


def textbox(slide, x, y, w, h, text, size=24, color=TEXT, bold=False,
            align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    """Текстовая рамка с одним абзацем."""
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
    run.font.name = "Segoe UI"
    return box


def bullets(slide, x, y, w, h, items, size=22, color=TEXT, space=10):
    """Список маркеров. items: список строк, первая строка может начинаться с «●».
    Если строка начинается с '#' — это подзаголовок, красится в MUTED."""
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
    """Заголовок слайда: мелкая строка-«лейбл» + крупный заголовок."""
    textbox(slide, Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.4),
            kicker, size=16, color=ACCENT, bold=True)
    textbox(slide, Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.9),
            title, size=40, color=TEXT, bold=True)


def card(slide, x, y, w, h, fill=CARD):
    """Карточка-подложка с рамкой."""
    shape = slide.shapes.add_shape(1, x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = BORDER
    shape.line.width = Pt(1)
    shape.shadow.inherit = False
    return shape


def footer(slide, num):
    textbox(slide, Inches(12.4), Inches(7.0), Inches(0.7), Inches(0.4),
            str(num), size=14, color=MUTED, align=PP_ALIGN.RIGHT)


# ---------- Слайд 1 · Титул ----------

def s01_title():
    s = add_slide()
    textbox(s, Inches(0.8), Inches(2.1), Inches(11.7), Inches(0.5),
            "PULSELAB · УРОК A03", size=18, color=ACCENT, bold=True)
    textbox(s, Inches(0.8), Inches(2.6), Inches(11.7), Inches(1.6),
            "Типографика и обложка трека", size=54, color=TEXT, bold=True)
    textbox(s, Inches(0.8), Inches(4.1), Inches(11.7), Inches(0.6),
            "Квадрат без «жвачки» · alt своими словами · голос шрифтов",
            size=24, color=MUTED)
    textbox(s, Inches(0.8), Inches(6.4), Inches(11.7), Inches(0.4),
            "Группа смотрит на стену", size=14, color=MUTED)
    footer(s, 1)


# ---------- Слайд 2 · Повторение ----------

def s02_retrieval():
    s = add_slide()
    header(s, "ПОВТОРЕНИЕ · 60 СЕК", "Зачем у картинки атрибут alt?")
    card(s, Inches(0.8), Inches(2.1), Inches(11.7), Inches(3.2))
    bullets(s, Inches(1.3), Inches(2.4), Inches(10.7), Inches(2.6), [
        "Поднимите руки, кто помнит",
        "Ждём один ответ",
        "#Подсказка: у неё есть смысл даже тогда, когда картинку не видно",
    ], size=26, space=14)
    footer(s, 2)


# ---------- Слайд 3 · Проблема «жвачка» ----------

def s03_problem():
    s = add_slide()
    header(s, "ПРОБЛЕМА", "Фото 4000×3000 в рамку 200×200 без правил")

    # левая карточка — «было»
    card(s, Inches(0.8), Inches(2.0), Inches(5.5), Inches(4.2), fill=CARD)
    textbox(s, Inches(1.1), Inches(2.2), Inches(4.9), Inches(0.5),
            "Было — без правил", size=20, color=DANGER, bold=True)
    # «растянутый» квадрат (сильно растянут по вертикали)
    shape = s.shapes.add_shape(1, Inches(1.6), Inches(2.9), Inches(3.2), Inches(2.6))
    shape.fill.solid(); shape.fill.fore_color.rgb = RGBColor(0x3A, 0x2A, 0x3A)
    shape.line.color.rgb = DANGER; shape.line.width = Pt(2)
    shape.shadow.inherit = False
    textbox(s, Inches(1.1), Inches(5.7), Inches(4.9), Inches(0.4),
            "браузер растянул — «жвачка»", size=16, color=DANGER)

    # стрелка
    textbox(s, Inches(6.5), Inches(3.6), Inches(0.8), Inches(0.6),
            "→", size=40, color=ACCENT, align=PP_ALIGN.CENTER)

    # правая карточка — «стало»
    card(s, Inches(7.4), Inches(2.0), Inches(5.5), Inches(4.2), fill=CARD)
    textbox(s, Inches(7.7), Inches(2.2), Inches(4.9), Inches(0.5),
            "Стало — с правилами", size=20, color=ACCENT, bold=True)
    shape = s.shapes.add_shape(1, Inches(8.2), Inches(2.9), Inches(3.2), Inches(2.6))
    shape.fill.solid(); shape.fill.fore_color.rgb = RGBColor(0x14, 0x3A, 0x2A)
    shape.line.color.rgb = ACCENT; shape.line.width = Pt(2)
    shape.shadow.inherit = False
    textbox(s, Inches(7.7), Inches(5.7), Inches(4.9), Inches(0.4),
            "плотный квадрат — cover + aspect-ratio", size=16, color=ACCENT)

    textbox(s, Inches(0.8), Inches(6.5), Inches(11.7), Inches(0.5),
            "Кто виноват — фото или браузер?", size=20, color=MUTED, bold=True)
    footer(s, 3)


# ---------- Слайд 4 · Иерархия текста ----------

def s04_hierarchy():
    s = add_slide()
    header(s, "ПРАВИЛО", "Иерархия: один главный смысл")

    card(s, Inches(0.8), Inches(2.0), Inches(6.0), Inches(4.4), fill=CARD)
    textbox(s, Inches(1.2), Inches(2.3), Inches(5.2), Inches(0.5),
            "Pixel Tide", size=34, color=TEXT, bold=True)
    textbox(s, Inches(1.2), Inches(3.3), Inches(5.2), Inches(0.5),
            "Nova Park", size=20, color=MUTED)
    textbox(s, Inches(1.2), Inches(4.0), Inches(5.2), Inches(0.5),
            "3:14", size=16, color=MUTED)

    bullets(s, Inches(7.4), Inches(2.1), Inches(5.4), Inches(4.0), [
        "название — h2, крупный, яркий",
        "исполнитель — p, поменьше",
        "длительность — p, приглушённая",
        "#глаз за секунду находит, что смотреть",
    ], size=22, space=16)

    textbox(s, Inches(0.8), Inches(6.6), Inches(11.7), Inches(0.4),
            "Спроси: что на вашей карточке поставишь самым заметным?",
            size=18, color=MUTED, bold=True)
    footer(s, 4)


# ---------- Слайд 5 · object-fit три режима ----------

def s05_object_fit():
    s = add_slide()
    header(s, "РЕЖИМЫ", "object-fit · что выбрать")

    labels = [("cover", "заполнил кадр,\nкрая обрезал", ACCENT),
              ("contain", "вся картинка,\nполя по бокам", MUTED),
              ("fill", "растянул под рамку\n(обычно ломает)", DANGER)]
    x0 = Inches(1.0)
    w = Inches(3.5)
    gap = Inches(0.35)

    for i, (name, desc, col) in enumerate(labels):
        x = x0 + i * (w + gap)
        card(s, x, Inches(2.0), w, Inches(4.4), fill=CARD)
        # рамка-«картинка»
        shape = s.shapes.add_shape(1, x + Inches(0.5), Inches(2.3),
                                   Inches(2.5), Inches(2.5))
        shape.fill.solid(); shape.fill.fore_color.rgb = BG
        shape.line.color.rgb = col; shape.line.width = Pt(2)
        shape.shadow.inherit = False
        # внутри — паттерн, разный для каждого режима
        inner = s.shapes.add_shape(1, x + Inches(0.75), Inches(2.55),
                                   Inches(2.0), Inches(2.0))
        inner.fill.solid()
        if i == 0:
            inner.fill.fore_color.rgb = RGBColor(0x14, 0x3A, 0x2A)
            inner.line.color.rgb = ACCENT
        elif i == 1:
            inner.fill.fore_color.rgb = RGBColor(0x1A, 0x22, 0x3A)
            inner.line.color.rgb = MUTED
            inner.width = Inches(1.0); inner.height = Inches(2.0)
            inner.left = x + Inches(1.25); inner.top = Inches(2.55)
        else:
            inner.fill.fore_color.rgb = RGBColor(0x3A, 0x22, 0x1A)
            inner.line.color.rgb = DANGER
            inner.width = Inches(2.0); inner.height = Inches(1.6)
            inner.left = x + Inches(0.75); inner.top = Inches(2.75)
        inner.shadow.inherit = False

        textbox(s, x, Inches(4.95), w, Inches(0.6), name, size=28,
                color=col, bold=True, align=PP_ALIGN.CENTER)
        textbox(s, x, Inches(5.55), w, Inches(0.9), desc, size=15,
                color=MUTED, align=PP_ALIGN.CENTER)

    textbox(s, Inches(0.8), Inches(6.6), Inches(11.7), Inches(0.5),
            "Для обложки в квадрате — какой режим и почему?", size=20,
            color=ACCENT, bold=True)
    footer(s, 5)


# ---------- Слайд 6 · Предикт ----------

def s06_predict():
    s = add_slide()
    header(s, "ПРЕДСКАЗАНИЕ · РУКИ", "Квадрат 200×200, фото 4000×3000")

    card(s, Inches(0.8), Inches(2.0), Inches(11.7), Inches(3.6))
    bullets(s, Inches(1.3), Inches(2.3), Inches(10.7), Inches(3.0), [
        "1.  cover — что будет с краями фото?",
        "2.  fill — что будет с лицом?",
        "#Проговариваем, потом я нажимаю на стенде",
    ], size=26, space=18)

    textbox(s, Inches(0.8), Inches(6.2), Inches(11.7), Inches(0.5),
            "Сначала слова — потом клик.", size=20, color=MUTED, bold=True)
    footer(s, 6)


# ---------- Слайд 7 · alt ----------

def s07_alt():
    s = add_slide()
    header(s, "ДОСТУПНОСТЬ", "alt · слова вместо картинки")

    # плохо
    card(s, Inches(0.8), Inches(2.0), Inches(5.5), Inches(3.4), fill=CARD)
    textbox(s, Inches(1.1), Inches(2.2), Inches(4.9), Inches(0.5),
            "Плохо", size=20, color=DANGER, bold=True)
    textbox(s, Inches(1.1), Inches(2.8), Inches(4.9), Inches(1.8),
            '<img src="oblozhka.jpg"\n     alt="img1">',
            size=20, color=TEXT)
    textbox(s, Inches(1.1), Inches(4.7), Inches(4.9), Inches(0.5),
            "есть место — нет смысла", size=16, color=DANGER)

    # хорошо
    card(s, Inches(6.9), Inches(2.0), Inches(5.6), Inches(3.4), fill=CARD)
    textbox(s, Inches(7.2), Inches(2.2), Inches(5.0), Inches(0.5),
            "Хорошо", size=20, color=ACCENT, bold=True)
    textbox(s, Inches(7.2), Inches(2.8), Inches(5.0), Inches(1.8),
            '<img src="oblozhka.jpg"\n     alt="Обложка трека Pixel Tide">',
            size=20, color=TEXT)
    textbox(s, Inches(7.2), Inches(4.7), Inches(5.0), Inches(0.5),
            "смысл не пропал, даже если фото нет", size=16, color=ACCENT)

    bullets(s, Inches(0.8), Inches(5.7), Inches(11.7), Inches(1.2), [
        "Для кого пишем? Скринридер · отвалившийся интернет · поиск",
    ], size=20, space=0)
    footer(s, 7)


# ---------- Слайд 8 · Критерий «готово» ----------

def s08_done():
    s = add_slide()
    header(s, "ДЕЛАЕШЬ САМ · КРИТЕРИЙ «ГОТОВО»", "Заглушка → настоящая обложка")

    card(s, Inches(0.8), Inches(2.0), Inches(11.7), Inches(4.4))
    bullets(s, Inches(1.3), Inches(2.3), Inches(10.7), Inches(3.8), [
        "вместо заглушки-градиента — настоящая картинка",
        "object-fit: cover, квадрат, без «жвачки»",
        "alt своими словами: что на обложке",
        "название трека заметно крупнее подписи",
        "#открой task.md и иди по шагам 1–5",
    ], size=24, space=16)

    footer(s, 8)


# ---------- Слайд 9 · Выход ----------

def s09_exit():
    s = add_slide()
    header(s, "ВЫХОД", "Что уносим с урока")

    card(s, Inches(0.8), Inches(2.0), Inches(11.7), Inches(4.2))
    bullets(s, Inches(1.3), Inches(2.3), Inches(10.7), Inches(3.6), [
        "1.  Назови один термин своими словами: object-fit / alt / иерархия",
        "2.  Кидай скрин обложки в чат группы",
        "3.  Прогноз: почему fill не берём для обложки?",
        "#Домашка: подключить шрифты PulseLab, проверить cover и alt",
    ], size=24, space=18)

    footer(s, 9)


# ---------- Сборка ----------

def build():
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    s01_title()
    s02_retrieval()
    s03_problem()
    s04_hierarchy()
    s05_object_fit()
    s06_predict()
    s07_alt()
    s08_done()
    s09_exit()

    out = "A03-типографика-и-медиа.pptx"
    prs.save(out)
    print(f"Готово: {out} ({len(prs.slides.__iter__.__self__._sldIdLst)} слайдов)")


if __name__ == "__main__":
    build()
