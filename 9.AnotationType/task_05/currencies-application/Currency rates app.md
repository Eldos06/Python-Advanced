[[9.AnotationType/task_05/currencies-application/app.py|app]] [[9.AnotationType/task_05/currencies-application/main.py|main]] [[9.AnotationType/task_05/currencies-application/core/config.py|core/config]] [[9.AnotationType/task_05/currencies-application/core/types.py|core/types]] [[9.AnotationType/task_05/currencies-application/core/currency_exists_check.py|core/currency_exists_check]] [[9.AnotationType/task_05/currencies-application/core/currency_rates_getter.py|core/currency_rates_getter]] [[9.AnotationType/task_05/currencies-application/helpers/jsoncoders.py|helpers/jsoncoders]] [[9.AnotationType/task_05/currencies-application/helpers/request_param_reader.py|helpers/request_param_reader]]

---
tags:
  - python
  - aiohttp
  - typing
  - dataclasses
  - asyncio
---

# Currency rates app — итоговый проект (task_05)

Небольшое, но полноценное asyncio/aiohttp-приложение: отдаёт курсы валют по HTTP, с валидацией входных данных,
файловым кэшем на диске и точной арифметикой через `Decimal`. Практическое применение тем из [[9.AnotationType/1.AnotationType/Аннотации типов.md|аннотаций типов]]
(`TypedDict`, `frozen`-датаклассы, classmethod-фабрики) в реальном проекте.

## 1. Точка входа и роутинг — [[9.AnotationType/task_05/currencies-application/app.py|app.py]] + [[9.AnotationType/task_05/currencies-application/main.py|main.py]]

```python
routes = web.RouteTableDef()

@routes.get("/rates/{currency}")
@routes.get("/rates/{currency}/{date}")
async def get_currency_rates(request: web.Request) -> web.Response:
    currency, selected_date = await get_currency_and_date_from_request(request)
    getter = CurrencyRatesGetter(currency=currency, for_data=selected_date)
    info_data_bytes = await getter.get_currency_info()
    return web.json_response(text=info_data_bytes.decode("utf-8"))
```

Один и тот же обработчик навешан на два маршрута (`RouteTableDef.get` дважды) - с датой в пути и без.
`main.py` - обычный aiohttp entrypoint: создаёт папку кэша, настраивает логирование, вызывает `web.run_app(app, port=8081)`.

## 2. Конфигурация — [[9.AnotationType/task_05/currencies-application/core/config.py|core/config.py]]

Централизованные константы: `CACHE_DIR` (папка для JSON-файлов кэша, вычисленная через `pathlib.Path(__file__)`),
внешние API-урлы (`CURRENCY_API_URL`, `CURRENCIES_LIST_API_URL`), белый список валют-целей `TARGET_CURRENCIES` и
`configure_logging()`.

## 3. Типы данных — [[9.AnotationType/task_05/currencies-application/core/types.py|core/types.py]]

```python
class ResponseType(TypedDict):
    date: date
    values: dict[str, Decimal]

@dataclass(frozen=True)
class CurrencyValue:
    currency: str
    value: Decimal

@dataclass(frozen=True)
class CurrencyInfo:
    date: date
    currency: str
    values: list[CurrencyValue]

    @classmethod
    def from_currency_info_response(cls, info, source_currency, target_currencies) -> "CurrencyInfo":
        return cls(
            date=date.fromisoformat(info["date"]),
            currency=source_currency,
            values=[CurrencyValue(currency=name, value=value)
                    for name, value in info["values"].items()
                    if name in target_currencies],   # фильтр по TARGET_CURRENCIES из config.py
        )
```

`TypedDict` типизирует "сырой" JSON-ответ без создания класса-обёртки в рантайме; `frozen=True` делает
`CurrencyValue`/`CurrencyInfo` неизменяемыми - логично для объекта, представляющего исторический факт ("курс на дату X").
Фабрика `from_currency_info_response` - тот же паттерн `cls(...)` -> `ModelType`, что и в [[9.AnotationType/1.AnotationType/Аннотации типов.md|models.py]] из темы аннотаций.

## 4. Проверка существования валюты — [[9.AnotationType/task_05/currencies-application/core/currency_exists_check.py|core/currency_exists_check.py]]

```python
@dataclass
class CurrencyExistsCheck:
    cache_currencies: set[str] = field(default_factory=set)

    @classmethod
    async def get_all_currencies(cls) -> dict[str, str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(config.CURRENCIES_LIST_API_URL) as response:
                return await response.json()

    async def currency_exists(self, currency: str) -> bool:
        if not self.cache_currencies:
            self.cache_currencies.update(set(await self.get_all_currencies()))
        return currency in self.cache_currencies

check = CurrencyExistsCheck()  # общий на всё приложение объект-кэш
```

Ленивая загрузка справочника валют: полный список из интернета скачивается один раз (при первом запросе) и живёт
в `self.cache_currencies` в памяти процесса, а не перекачивается на каждый запрос.

> [!WARNING] Два подозрительных места в этом файле
> `from poetry.console.commands import self` в начале файла - нерабочий/случайный импорт (похоже на автодополнение
> IDE), никак не используется и не нужен для работы класса. И строка `log.info(f"cache_currencies : {cache_currencies}")`
> стоит прямо в теле класса (на уровне объявления полей, не внутри метода) - это выполнится **один раз при
> определении класса**, а не при создании/использовании экземпляра, и залогирует не значение поля конкретного
> объекта, а сам `field(default_factory=set)` в виде объекта dataclasses.

## 5. Получение и кэширование курсов — [[9.AnotationType/task_05/currencies-application/core/currency_rates_getter.py|core/currency_rates_getter.py]]

`CurrencyRatesGetter.get_currency_info()` - главная точка входа, реализует стратегию "кэш прежде интернета":

```python
async def get_currency_info(self) -> bytes:
    cached = await self.read_currency_info_from_cache()
    if cached is not None:
        return cached                              # файл на диске уже есть - интернет не трогаем
    return await self.read_and_save_currency_info()  # иначе: скачать -> сохранить в кэш -> вернуть
```

Имя файла кэша детерминировано датой и валютой: `get_cache_filename` -> `"2026-06-11-usd.json"` (см. реальный
файл в [[9.AnotationType/task_05/currencies-application/core/currencies-data-cache/2026-06-11-usd.json|currencies-data-cache]]).
Чтение/запись файлов идёт через `aiofiles` (асинхронный I/O, не блокирует event loop), а JSON декодируется через
кастомный `json_decode_decimal` (см. ниже) - все числа из ответа API становятся `Decimal`, а не `float`, чтобы не
потерять точность курса валют (та же мотивация, что и в [[3.Сложные простые типы/Строки, байты и Decimal.md|Decimal]] из темы 3).

## 6. JSON: `Decimal`/`date` туда и обратно — [[9.AnotationType/task_05/currencies-application/helpers/jsoncoders.py|helpers/jsoncoders.py]]

```python
def json_encode_default(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return str(obj)               # Decimal -> строка, не float (не терять точность и не терять форму записи)
    raise TypeError(...)

json_decode_decimal = json.JSONDecoder(parse_int=Decimal, parse_float=Decimal)  # обратный путь: числа из JSON -> Decimal
```

Стандартный `json` не умеет сериализовать `Decimal`/`date` сам по себе - `default=` подключает собственное правило
для "непонятных" ему типов, а `parse_int`/`parse_float` в `JSONDecoder` перехватывают числа ещё на входе.

## 7. Валидация параметров запроса — [[9.AnotationType/task_05/currencies-application/helpers/request_param_reader.py|helpers/request_param_reader.py]]

```python
async def validate_currency(currency: str) -> str:
    if await check.currency_exists(currency):
        return currency
    raise web.HTTPNotFound(...)  # 404, если валюты не существует

def validate_provided_date(provided_date: str | None) -> date:
    selected_date = date.today() - timedelta(days=1)  # по умолчанию "вчера" - у API нет котировок за сегодня
    if provided_date is not None:
        try:
            selected_date = date.fromisoformat(provided_date)
        except ValueError:
            raise web.HTTPUnprocessableEntity(...)  # 422, если дата не ISO-формата
    return selected_date
```

Оба валидатора кидают конкретные HTTP-исключения aiohttp (`HTTPNotFound`, `HTTPUnprocessableEntity`) вместо
обычных `ValueError`/`return None` - aiohttp сам превращает такое исключение в правильный HTTP-ответ с телом-JSON.

## Служебные файлы

Пустые файлы-маркеры пакетов: [[9.AnotationType/task_05/currencies-application/core/__init__.py|core/__init__.py]],
[[9.AnotationType/task_05/currencies-application/helpers/__init__.py|helpers/__init__.py]].
