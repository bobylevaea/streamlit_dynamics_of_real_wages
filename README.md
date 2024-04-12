## Анализ динамики номинальных и реальных заработных плат в Российской Федерации в период с 2000 по 2023 годы

Проект подготовлен в рамках курса "Старт в Data Science" от ВШЭ

В проекте используются открытые данные из официальных источников:

Сайт Росстата (https://rosstat.gov.ru/)

Таблицы уровня инфляции в России (https://уровень-инфляции.рф)

### Описание датасета:
Датасет содержит информацию о среднемесячной номинальной начисленной заработной плате работников организаций в Российской Федерации с **2000** по **2023** годы по различным отраслям экономики.

Каждая строка представляет год и значения заработной платы для трех отраслей: строительство, образование и деятельность в области здравоохранения и социальных услуг.

Данные также включают годовую инфляцию, уровень безработицы и номинальный ВВП на душу населения России в долларах США.

### Параметры датасета:

- **year**: год отчетности.
- **construction**: среднемесячная номинальная начисленная заработная плата в сфере строительства.
- **education**: среднемесячная номинальная начисленная заработная плата в сфере образования.
- **healthcare_and_social_services**: среднемесячная номинальная начисленная заработная плата в сфере здравоохранения и социальных услуг.
- **annual_inflation**: годовая инфляция в процентах.
- **unemployment_rate**: уровень безработицы в процентах.
- **gdp_per_capita**: номинальный ВВП на душу населения России в долларах США.

Streamlit-приложение можно посмотреть по [ссылке](https://dynamics-real-wages.streamlit.app/).

## Запуск приложения локально

Для запуска Streamlit локально непосредственно в корневой папке репозитория выполните следующее:

```Командная строка
$ python -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ streamlit run app.py
```
Откройте http://localhost:8501, чтобы просмотреть приложение.


&copy; Екатерина Бобылева
