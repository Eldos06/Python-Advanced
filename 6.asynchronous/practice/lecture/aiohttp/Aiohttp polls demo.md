[[6.asynchronous/practice/lecture/aiohttp/create_project.sh|create_project.sh]] [[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/routes.py|routes]] [[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/views.py|views]]

---
tags:
  - python
  - asyncio
  - aiohttp
---

# Aiohttp polls demo — конспект

Официальный демо-скелет `aiohttp` ("polls demo" из документации `aiohttp`) — эталонная структура "большого" веб-приложения на `aiohttp.web`: роутинг, view-функции, шаблоны, middleware, конфиг, слой БД и интеграционные тесты разнесены по отдельным модулям.

> [!WARNING] В этом репозитории — только пустой каркас
> Все Python/HTML/YAML-файлы приложения (`aiohttpdemo_polls/routes.py`, `views.py`, `db.py`, `main.py`, `settings.py`, `middlewares.py`, `utils.py`, `__init__.py`, `__main__.py`, все `templates/*.html`, `static/style.css`, `config/*.yaml`, `requirements.txt`, `setup.py`, `tox.ini`, `Makefile`, `README.rst`, `init_db.py`, `tests/*`) на данный момент **пустые (0 байт)**. Реализация ещё не написана — это домашняя заготовка, а не рабочее приложение. Единственный файл с реальным содержимым — [[6.asynchronous/practice/lecture/aiohttp/create_project.sh|create_project.sh]].

## 1. Что реально есть: `create_project.sh`

Это ровно тот скрипт, который и породил всю пустую структуру ниже — создаёт папки и делает `touch` по каждому файлу:

```bash
mkdir -p aiohttpdemo_polls/static/images
mkdir -p aiohttpdemo_polls/templates
mkdir -p config
mkdir -p tests

touch aiohttpdemo_polls/db.py
touch aiohttpdemo_polls/__init__.py
touch aiohttpdemo_polls/__main__.py
touch aiohttpdemo_polls/main.py
touch aiohttpdemo_polls/middlewares.py
touch aiohttpdemo_polls/routes.py
touch aiohttpdemo_polls/settings.py
touch aiohttpdemo_polls/utils.py
touch aiohttpdemo_polls/views.py
...
touch init_db.py
touch Makefile
touch README.rst
touch requirements.txt
touch setup.py
touch tox.ini
```

Отсюда и все имена модулей ниже — они уже "забронированы" структурой, но без содержимого.

## 2. Какая роль предполагается за каждым модулем

Ниже — типовая архитектура именно этого канонического демо `aiohttp` (то, что предстоит реализовать в пустых файлах), а не то, что уже написано в репозитории:

| Файл | Ожидаемая роль |
|---|---|
| `routes.py` | `setup_routes(app)` — регистрация GET/POST маршрутов (список опросов, детали, голосование, результаты) и статики |
| `views.py` | обработчики запросов: список вопросов, страница вопроса, обработка голоса (POST), страница результатов |
| `db.py` | настройка подключения к БД (обычно Postgres через `aiopg`/`SQLAlchemy Core`) и `cleanup_ctx` для открытия/закрытия пула при старте/остановке приложения |
| `settings.py` | загрузка конфигурации из `config/polls.yaml` (хост, порт, доступы к БД) |
| `middlewares.py` | middleware для страниц ошибок (404 → `templates/404.html`, 500 → `templates/500.html`) |
| `main.py` / `__main__.py` | фабрика `create_app()`, подключение `aiohttp_jinja2` для шаблонов, запуск через `web.run_app` / `python -m aiohttpdemo_polls` |
| `tests/conftest.py`, `tests/test_integration.py` | интеграционные тесты через `aiohttp.pytest_plugin` (фикстура `aiohttp_client`) против тестового конфига `config/polls_test.yaml` |
| `Makefile` / `tox.ini` | команды разработки: установка зависимостей, поднятие Postgres, запуск приложения и тестов в нескольких окружениях |

## 3. Как это соотносится с более простыми примерами из этого раздела

Структура здесь — куда более "промышленная" версия того же самого `aiohttp.web`, что уже встречался раньше:

- `RouteTableDef`/`add_routes` из [[Async client-server]] — здесь эту роль на себя берёт `routes.py` с явной функцией `setup_routes(app)`.
- Простейший `web.Application()` + `handle(request)` из `server.py` в [[Aiofiles and currency project]] — концептуальный предок `views.py`/`main.py` этого демо, только с шаблонами и БД вместо одной строки текста.
- Конкурентные HTTP-запросы клиента из [[Async client-server]] пригодятся, если понадобится написать интеграционные тесты или клиент к этому API.

## Дальше по теме

- [[Asyncio basics]] — базовые примитивы asyncio, на которых работает весь `aiohttp`.
- [[Async client-server]] — минимальный сервер/клиент на `aiohttp.web`/`ClientSession` без шаблонов и БД.
- [[Aiofiles and currency project]] — асинхронная работа с файлами и внешним API, дополняющая веб-часть.

## Все файлы каркаса (пустые, 0 байт)

Приложение: [[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/__init__.py|__init__.py]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/__main__.py|__main__.py]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/db.py|db.py]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/main.py|main.py]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/middlewares.py|middlewares.py]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/settings.py|settings.py]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/utils.py|utils.py]].

Статика и шаблоны: [[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/static/style.css|static/style.css]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/static/images/background.png|static/images/background.png]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/templates/404.html|templates/404.html]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/templates/500.html|templates/500.html]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/templates/base.html|templates/base.html]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/templates/detail.html|templates/detail.html]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/templates/index.html|templates/index.html]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/templates/results.html|templates/results.html]].

Конфиг и окружение: [[6.asynchronous/practice/lecture/aiohttp/config/polls.yaml|config/polls.yaml]],
[[6.asynchronous/practice/lecture/aiohttp/config/polls_test.yaml|config/polls_test.yaml]],
[[6.asynchronous/practice/lecture/aiohttp/requirements.txt|requirements.txt]],
[[6.asynchronous/practice/lecture/aiohttp/setup.py|setup.py]],
[[6.asynchronous/practice/lecture/aiohttp/init_db.py|init_db.py]],
[[6.asynchronous/practice/lecture/aiohttp/tox.ini|tox.ini]],
[[6.asynchronous/practice/lecture/aiohttp/Makefile|Makefile]],
[[6.asynchronous/practice/lecture/aiohttp/README.rst|README.rst]].

Тесты: [[6.asynchronous/practice/lecture/aiohttp/tests/__init__.py|tests/__init__.py]],
[[6.asynchronous/practice/lecture/aiohttp/tests/conftest.py|tests/conftest.py]],
[[6.asynchronous/practice/lecture/aiohttp/tests/test_integration.py|tests/test_integration.py]].

Роутинг и вью (упомянуты в таблице выше): [[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/routes.py|routes.py]],
[[6.asynchronous/practice/lecture/aiohttp/aiohttpdemo_polls/views.py|views.py]].
