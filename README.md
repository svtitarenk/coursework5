## Курсовая работа по БД и Python

>  рамках проекта мы получим данные о компаниях и вакансиях с сайта `hh.ru`, спроектируем таблицы в БД `PostgreSQL` и загрузим полученные данные в созданные таблицы в БД `Postgresql`.

### Основные шаги проекта    
> Получить данные о работодателях и их вакансиях с сайта `hh.ru`. Для этого используйте публичный API hh.ru и библиотеку 
requests.  
Выбрать не менее 10 интересных вам компаний, от которых вы будете получать данные о вакансиях по API.
Спроектировать таблицы в БД `PostgreSQL` для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используйте библиотеку 
psycopg2.  
Реализовать код, который заполняет созданные в БД `PostgreSQL` таблицы данными о работодателях и их вакансиях.  
Создать класс `DBManager` для работы с данными в БД.


### Как работает сборка

#### Выбор компаний
- Поиск топа компаний по открытым вакансия  

#### Проектирование БД
- Две таблицы: vacancies & employers

#### Заполнение БД 
1. Создание БД
2. Создание таблиц
3. Заполнение таблиц


### Что используется
1. `classes` - Классы 
   - `db_manager` - для работы с выборками, которые получены через `hh_parser`
   - `hh_parser` - отвечает за выборку компаний и вакансий
2. `utils` - дополнительные функции для работы проекта
3. `.gitignore` - стандартный gitignore для Python
4. `pyproject.toml` - зависимости проекта
    - `requests` 
    - `pcycopg2` 

Конфигурация БД, как прописать логины и пароли

### БД
#### Конфигурация БД
БД создается автоматически при начале работы скрипта в utils/utils
Также при запуске загружаются данные из HH: employers and vacancies
Данные добавляются в таблицы в БД (employers and vacancies)

#### Авторизация
для авторизации в БД необходимо  

1 заполнить файл `database_example.ini`  
   - указать:
      - host="ваше имя хоста"  
      - user="ваше имя пользователя в БД"  
      - password="ваш пароль"  
      - port="ваш порт"  

2 Переименовать файл `database_example.ini`  в `database.ini`  


### Utils
создается БД (db_name="coursework")  
создаются таблицы vacancies + employers

###
### DBManager
Выборки, которые заложены в меню main файла и взаимодействие с пользователем.

###
###
### Взаимодействие с пользователем
1 Задать настройки БД (пункт Авторизация настоящего файла)  
2 Запустить файл main.py  
3 Следовать инструкции на экране  