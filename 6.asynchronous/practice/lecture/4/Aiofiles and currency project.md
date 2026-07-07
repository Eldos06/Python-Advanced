[[6.asynchronous/practice/lecture/4/main.py|main]] [[6.asynchronous/practice/lecture/4/practice.py|practice]] [[6.asynchronous/practice/lecture/4/project/main.py|project main]] [[6.asynchronous/practice/lecture/4/project/currency_rates_getter.py|currency_rates_getter]]

---
tags:
  - python
  - asyncio
  - aiofiles
  - aiohttp
---

# Aiofiles и мини-проект "курсы валют" — конспект

Урок из двух частей: [[6.asynchronous/practice/lecture/4/main.py|main.py]]/[[6.asynchronous/practice/lecture/4/practice.py|practice.py]] показывают асинхронную работу с файлами через `aiofiles`, а `project/` — небольшое (незаконченное) приложение, которое ходит за курсами валют в публичный API и кэширует их на диск.

## 1. `aiofiles`: асинхронные файлы

```python
async def read_file():
    async with aiofiles.open(FILE_NAME, mode='w') as f:
        for i in range(1, 11):
            await f.write(f"line {i}\n")

async def read_lines_from_file():
    async with aiofiles.open(FILE_NAME, mode='r') as f:
        async for line in f:
            print(line.strip())
```

`aiofiles.open` — асинхронный контекстный менеджер, `async for line in f` — асинхронная построчная итерация. Под капотом файловые операции всё равно уходят в thread pool (сам диск не умеет в `await`), но API даёт единообразный асинхронный стиль наравне с сетевыми вызовами.

Там же — временный файл и удаление:

```python
async def show_write_to_temp_file():
    async with aiofiles.tempfile.NamedTemporaryFile('w+') as f:
        await f.writelines(['foo\n', 'bar\n', 'baz\n', 'qux\n'])
        await f.seek(0)
        async for line in f:
            print(repr(line))

async def remove_file():
    await aiofiles.os.remove(FILE_NAME)
```

`practice.py` — по сути та же тема (запись/чтение/реверс строк/подсчёт строк), плюс отдельная функция копирования файла построчно с обработкой ошибок:

```python
async def async_copy_file_line_by_line(source_file, destination_file):
    try:
        async with aiofiles.open(source_file, mode='r') as src, aiofiles.open(destination_file, mode='w') as dst:
            async for line in src:
                await dst.write(line)
            await src.delete()
    except FileNotFoundError:
        print(f"Ошибка: файл '{source_file}' не найден.")
```

> [!WARNING] `src.delete()` не существует
> У объекта, который возвращает `aiofiles.open`, нет метода `delete()` — это приведёт к `AttributeError` при попытке реально скопировать файл (правильный способ удалить файл — `aiofiles.os.remove(source_file)`, как показано в `main.py`).

> [!WARNING] Мусорная строка в `practice.py`
> ```python
> from common import log
> [[MetaClass]]
> ```
> Строка `[[MetaClass]]` — похоже, случайно вставленная Obsidian-ссылка вместо кода. Синтаксически для Python это валидное выражение (список из списка с именем `MetaClass`), но оно выполняется на уровне модуля при импорте/запуске файла и упадёт с `NameError: name 'MetaClass' is not defined`, поскольку такое имя нигде не определено. Из-за этого `practice.py` не запускается как есть.

## 2. Мостик к вебу: [[6.asynchronous/practice/lecture/4/server.py|server.py]]

Небольшой классический "hello world" на `aiohttp.web`, без завязки на файлы — судя по всему, отсюда начинается переход к теме веб-сервера, продолжающейся в [[Aiohttp polls demo]]:

```python
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    return web.Response(text="Hello, " + name)

app = web.Application()
app.add_routes([web.get('/', handle), web.get('/{name}', handle)])
```

`request.match_info` — словарь именованных сегментов URL (`{name}` из маршрута `/{name}`).

## 3. `project/`: клиент курсов валют

Идея приложения: получить список валют, проверить, что запрошенная валюта существует, скачать курсы на дату и закэшировать результат на диск в виде JSON.

- [[6.asynchronous/practice/lecture/4/project/common.py|common.py]] — константы: `CACHE_DIR`, URL публичного API `@fawazahmed0/currency-api`, `TARGET_CURRENCIES = ('rub', 'usd', 'eur', 'inr', 'jpy')`, общий логгер (пишет и в `file.log`, и в консоль).
- [[6.asynchronous/practice/lecture/4/project/currency_exist_check.py|currency_exist_check.py]] — `CurrencyExistCheck`, dataclass с ленивым кэшем:
  ```python
  @dataclass
  class CurrencyExistCheck:
      cached_currencies: set = field(default_factory=set)

      @classmethod
      async def get_all_currencies(cls) -> dict[str]:
          async with aiohttp.ClientSession() as session:
              async with session.get(CURRENCIES_LIST_API_URL) as response:
                  return await response.json()

      async def currency_exists(self, currency: str) -> bool:
          if not self.cached_currencies:
              all_currencies = await self.get_all_currencies()
              self.cached_currencies.update(all_currencies.keys())
          return currency in self.cached_currencies
  ```
  Список валют скачивается только один раз (при первом вызове `currency_exists`), дальше проверка идёт по кэшу в памяти.
- [[6.asynchronous/practice/lecture/4/project/currency_types.py|currency_types.py]] — типизированные `frozen`-датаклассы `CurrencyValue`/`CurrencyInfo` и фабрика `from_currency_info_response`, которая парсит ответ API и оставляет только валюты из `TARGET_CURRENCIES`.
- [[6.asynchronous/practice/lecture/4/project/json_coders.py|json_coders.py]] — свои `json_encoder`/`json_decoder` (`json.JSONEncoder`/`JSONDecoder`) с поддержкой `Decimal` и `date`, чтобы курсы валют не терялись в точности при сериализации через `float`.
- [[6.asynchronous/practice/lecture/4/project/currency_rates_getter.py|currency_rates_getter.py]] — класс `CurrencyRatesGetter` (валюта, целевые валюты, дата, имя кэш-файла `{date}-{currency}.json`); сам метод загрузки курсов ещё не реализован.
- [[6.asynchronous/practice/lecture/4/project/client.py|client.py]] и [[6.asynchronous/practice/lecture/4/project/main.py|main.py]] — точки входа, дергающие эти компоненты.

> [!WARNING] Проект содержит цепочку реальных багов и не запускается как есть
> - `currency_rates_getter.py`: `from typing import iterable` — в модуле `typing` нет `iterable` с маленькой буквы (правильно `Iterable`) → `ImportError` уже на импорте.
> - `currency_rates_getter.py`: `from json_coders import json_decoder_decimal, json_encod` — имена не совпадают с тем, что реально определено в `json_coders.py` (`json_encoder`, `json_decoder`) → `ImportError`.
> - `json_coders.py`: `from decimal import date` — класс `date` живёт в модуле `datetime`, а не `decimal` → `ImportError`.
> - `project/main.py`: `from types import CurrencyInfo` — импортирует из стандартного модуля `types` вместо локального `currency_types` → `ImportError` (в `types` такого имени нет).
> - `currency_types.py`: `from_currency_info_response` вызывает `cls(..., value=[...])`, но поле датакласса называется `values` (множественное число) → `TypeError: unexpected keyword argument 'value'`.
> - `client.py`: `@cache` (`functools.cache`) навешан на `async def main()`. `cache` запоминает не результат, а сам объект корутины; при повторном вызове `main()` вернётся уже awaited корутина, что даст `RuntimeError: cannot reuse already awaited coroutine`. Для асинхронных функций нужны специальные кэши (например, `async_lru`), а не `functools.cache`/`lru_cache` "в лоб".

## Служебные файлы

[[6.asynchronous/practice/lecture/4/common.py|common.py]] (на этом уровне, отдельно от `project/common.py`) - настраивает
`logging.basicConfig` с двумя хендлерами сразу: `FileHandler("file.log")` и `StreamHandler` - лог одновременно пишется
в консоль и на диск. [[6.asynchronous/practice/lecture/4/project/file.log|project/file.log]] - результат работы
аналогичного логгера внутри `project/` (runtime-артефакт, перезаписывается при каждом запуске).

## Дальше по теме

- [[Asyncio basics]] — `gather`/`create_task`, лежащие в основе конкурентных запросов к API.
- [[Async client-server]] — тот же паттерн `ClientSession` + конкурентные задачи, но для собственного сервера.
- [[Aiohttp polls demo]] — куда движется тема веб-сервера на `aiohttp.web`.
