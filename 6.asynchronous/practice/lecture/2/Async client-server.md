[[6.asynchronous/practice/lecture/2/sever.py|sever]] [[6.asynchronous/practice/lecture/2/client.py|client]] [[6.asynchronous/practice/lecture/2/errors ClientConnnectorError/client.py|client (errors variant)]]

---
tags:
  - python
  - asyncio
  - aiohttp
---

# Асинхронный HTTP клиент-сервер — конспект

Мини-приложение из двух процессов: [[6.asynchronous/practice/lecture/2/sever.py|sever.py]] поднимает `aiohttp.web`-сервер с двумя роутами, а [[6.asynchronous/practice/lecture/2/client.py|client.py]] конкурентно опрашивает оба роута через `ClientSession` + `TaskGroup`. Папка `errors ClientConnnectorError/` — та же пара клиент/сервер с доработками и демонстрацией ошибки подключения.

> [!NOTE] Не сырые сокеты
> Несмотря на название папки ("2"), здесь используется не `asyncio.open_connection`/стримы, а полноценный HTTP поверх `aiohttp` — сервер (`aiohttp.web`) и клиент (`aiohttp.ClientSession`).

## 1. Сервер: `RouteTableDef`

```python
route = web.RouteTableDef()

@route.get("/stocks")
async def get_stocks(request: web.Request):
    await asyncio.sleep(1)          # имитация задержки похода в БД/внешний API
    return web.json_response(data={"stocks": ["A", "B"]})

@route.get("/weather")
async def get_weather(request: web.Request):
    return web.json_response(data={"weather": "sunny", "temperature": 25})

def main():
    app = web.Application()
    app.add_routes(route)
    web.run_app(app, host="127.0.0.1", port=8080)
```

`RouteTableDef` — декоратор-реестр: роуты собираются в объект `route`, а подключаются к приложению одним вызовом `app.add_routes(route)`.

## 2. Клиент: конкурентные запросы через `TaskGroup`

```python
async def get_api(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def run_main():
    async with TaskGroup() as tg:
        stocks_task = tg.create_task(get_api(create_url("/stocks")))
        weather_task = tg.create_task(get_api(create_url("/weather")))

    log.info(f"Stocks: {stocks_task.result()}")
    log.info(f"Weather: {weather_task.result()}")
```

`asyncio.TaskGroup` (Python 3.11+) — структурный аналог `gather`: обе задачи стартуют параллельно, `async with` дожидается завершения **обеих** при выходе из блока, а если одна упадёт с исключением — вторая будет автоматически отменена. Результаты забираются через `.result()` уже после блока.

> [!WARNING] Мёртвая функция в `common.py`
> ```python
> def create_url(path: str) -> str:
>     return urllib.parse.urljoin(base, path)   # base нигде не определена
> ```
> В [[6.asynchronous/practice/lecture/2/common.py|common.py]] есть своя версия `create_url`, но она обращается к необъявленному имени `base` и упадёт с `NameError`, если её вызвать. На практике не используется: `client.py` не импортирует эту функцию, а определяет собственную `create_url(base, path)` с явным параметром.

## 3. Вариант `errors ClientConnnectorError/`

Та же пара клиент/сервер с добавками:

```python
policy = asyncio.WindowsSelectorEventLoopPolicy()
asyncio.set_event_loop_policy(policy)
```

Явная установка `WindowsSelectorEventLoopPolicy` — про это подробнее в [[Event loop policies]].

```python
conn = aiohttp.TCPConnector(limit_per_host=5)

async with ClientSession() as session:
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()
```

`response.raise_for_status()` превращает HTTP-ошибку (4xx/5xx) в исключение `aiohttp.ClientResponseError` — без него плохой ответ молча прошёл бы дальше как обычный JSON.

> [!WARNING] `TCPConnector` создаётся, но не используется
> `conn = aiohttp.TCPConnector(limit_per_host=5)` — коннектор с ограничением на 5 одновременных соединений к хосту создаётся, но никогда не передаётся в `ClientSession(connector=conn)`. Сессия ниже создаётся без него (`ClientSession()`), поэтому лимит фактически не применяется — это заготовка, которую не докрутили.

Название папки (`ClientConnnectorError`, с опечаткой) намекает на цель упражнения: если запустить `client.py` до старта `sever.py`, `session.get(...)` упадёт с `aiohttp.client_exceptions.ClientConnectorError: Cannot connect to host 127.0.0.1:8080` — это стандартная ошибка "сервер недоступен", с которой стоит уметь работать (try/except вокруг `get_api`), хотя в текущем коде она ещё не перехватывается явно.

В самом низу файла есть отдельный пример реального похода в интернет:

```python
async def main():
    url = "https://stackoverflow.com/"
    async with ClientSession(trust_env=True) as session:
        async with session.get(url) as resp:
            print(resp.status)
```

`trust_env=True` заставляет `aiohttp` учитывать системные переменные окружения (`HTTP_PROXY`/`HTTPS_PROXY`) при запросе.

## Файлы варианта `errors ClientConnnectorError/`

[[6.asynchronous/practice/lecture/2/errors ClientConnnectorError/common.py|common.py]] в этой папке - просто `setup_logging()`
(формат лога с `%(asctime)s - %(name)s - %(levelname)s`), отдельная от [[6.asynchronous/practice/lecture/2/common.py|common.py]]
на уровень выше. [[6.asynchronous/practice/lecture/2/errors ClientConnnectorError/sever.py|sever.py]] - тот же сервер
(`/stocks`, `/weather`), что и в основном [[6.asynchronous/practice/lecture/2/sever.py|sever.py]], с двумя добавками:
попыткой подключить `aiohttp_cors` (если не установлен - просто пропускается через `try/except ImportError`) и установкой
`WindowsSelectorEventLoopPolicy` **дважды** (один раз в начале файла, второй раз - идентичным блоком прямо перед `if __name__`) -
безвредная, но лишняя дублирующаяся настройка.

Пустой (0 байт) [[6.asynchronous/practice/lecture/2/2.py|2.py]] на уровень выше - судя по номеру, черновик/заготовка
для этого урока, ещё не заполненная содержимым.

## Дальше по теме

- [[Asyncio basics]] — `gather`/`create_task` без HTTP.
- [[Event loop policies]] — зачем менять политику event loop на Windows.
- [[Aiohttp polls demo]] — полноценное веб-приложение на `aiohttp.web`.
