# Curriculum Gates · вход / выход спринтов

После аудита. Пакеты A07+ создаются по [LESSON-PACKET-STANDARD.md](./LESSON-PACKET-STANDARD.md); здесь — **критерии** и правки последовательности.

## Блок A

### Sprint 1 · A01–A06 · Pulse FM v1
| | |
| --- | --- |
| **Вход** | Python знаком; VS Code; нет требования знать HTML |
| **Выход** | Баннер+шапка+витрина; demo day; 1 CSS-приём своими словами |
| **Риск** | Толстая доставка → закрыт пакетами teacher-first |
| **Отстающий** | минимум: link + одна карточка | **Быстрый** | второй визуальный акцент / помочь peer |

### Sprint 2 · A07–A12 · MusicHub
| | |
| --- | --- |
| **Вход** | Pulse FM v1 после A06 |
| **Выход** | Каталог MusicHub на grid; showcase A12 |
| **Ресеквенс** | **A09:** mobile-first **вместе** с Grid (сначала 1 колонка → 2+). `position`: только `relative/absolute/sticky` на конкретном плеере — не четыре модели за урок |
| **Риск** | Перегруз position + grid | **Один концепт/урок** держать |

| Код | Входной критерий | Выходной артефакт |
| --- | --- | --- |
| A07 | умеет link+cascade наивно | переменные `:root`, тема |
| A08 | flex-шапка A04 | flex-плеер внизу |
| A09 | flex+box | grid + mobile-first; sticky/absolute точечно |
| A10 | обложки A03 | визуальная иерархия каталога |
| A11 | стабильный layout | 1–2 CSS-анимации без JS |
| A12 | A07–A11 собраны | showcase MusicHub |

### Sprint 3 · A13–A18 · PulseBeat
| | |
| --- | --- |
| **Вход** | MusicHub жив |
| **Выход** | Мини-игра / beat UI; showcase A18 |
| **Ресеквенс** | **A13–A14:** не два дня синтаксиса. Таблица **Python → JS** на slides; быстрее DOM (A15) и события (A16) |
| **Риск** | Скука «мы это в Python знали» |

| Код | Фокус |
| --- | --- |
| A13 | map типов + `const/let`, функции как в Python |
| A14 | циклы/массивы на данных треков (коротко) |
| A15 | DOM query + textContent |
| A16 | click/keydown |
| A17 | game loop / requestAnimationFrame упрощённо |
| A18 | showcase |

### Sprint 4 · A19–A24 · MerchShop
| | |
| --- | --- |
| **Вход** | DOM+events |
| **Выход** | Магазин с корзиной; showcase A24 |
| **Ресеквенс** | Сначала **единая модель состояния + `render()`** (A20–A21), потом localStorage; **fetch (A22) только после** локальных данных и уверенного Live Server |
| **Риск** | cart+storage+fetch в одной каше |

### Sprint 5–6 · A25–A34 · Flask assemble
| | |
| --- | --- |
| **Вход** | MerchShop клиент |
| **Выход** | Склейка + polish + защита A |
| **Маркер** | Любая session / «логин» = **учебная**, реплика «это не банк» |

## Блок B

### Sprint 1 · B01–B06 · Studio
**Вход:** финал A. **Выход:** UI-kit на Pages.  
**Setup:** [SETUP-CHECKLISTS.md](./SETUP-CHECKLISTS.md) Git+Vite до кода.

### Sprint 2 · B07–B12 · Client truth
**Выход:** каталог с честными UI-состояниями сети.  
**Риск:** забытый offline в DevTools на showcase.

### Sprint 3 · B13–B18 · API
**Выход:** три запроса в Network.  
**Маркер:** session lite ≠ production auth.

### Sprint 4 · B19–B24 · Glue
Лидерборд, auth-lite, 401, валидация сервера, deploy docs, showcase.

### Sprint 5 · B25–B31 · Python inside
Вынос логики, JSON files, top3, pytest-lite, UX, видео, черновая защита.

### Sprint 6 · B32–B34 · Diploma
Чек-лист → защита → ретро. Рубрика: `templates/diploma.md`.

## Матрица showcase

| Урок | Продукт | Слот | Peer |
| --- | --- | --- | --- |
| A06 | Pulse FM | 6×N | да |
| A12 | MusicHub | 6×N | да |
| A18 | PulseBeat | 6×N | да |
| A24 | MerchShop | 6×N | да |
| A34 | защита A | по рубрике | — |
| B06/12/18/24 | срезы B | 6×N | да |
| B33 | диплом | рубрика диплома | — |
