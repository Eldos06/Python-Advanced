[[2.Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/retry/retry_func_dec.py|retry_func_dec]] [[2.Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/retry/retry_class_dec.py|retry_class_dec]] [[2.Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/retry/weather_fetcher.py|weather_fetcher]] [[2.Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/retry/example_retry_func.py|example_retry_func]]

---
tags:
  - python
  - decorators
  - retry
---

# Retry decorator — конспект

Мини-проект: один и тот же декоратор повторных попыток (`retry`) реализован **и как функция, и как класс**, плюс типизация декоратора через `ParamSpec`/`TypeVar`.

## 1. Функциональный вариант ([[2.Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/retry/retry_func_dec.py|retry_func_dec.py]])

```python
P = ParamSpec("P")
R = TypeVar("R")

def retry(
    decorated_func: Callable[P, R] | None = None,
    *,
    max_retry_count: int = 3,
    initial_timeout: int = 2,
    timeout_multiplier: int = 5,
    exceptions: Sequence[Exception] = (Exception,),
):
    if decorated_func is not None:
        return retry(
            max_retry_count=max_retry_count,
            initial_timeout=initial_timeout,
            timeout_multiplier=timeout_multiplier,
            exceptions=exceptions,
        )(decorated_func)

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            timeout = initial_timeout
            for attempt in range(1, max_retry_count + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retry_count:
                        raise
                    log.warning("Caught exception: %s, will retry in %ss", e, timeout)
                    time.sleep(timeout)
                    timeout *= timeout_multiplier
        return wrapper
    return decorator
```

> [!NOTE] Необязательные скобки через рекурсию
> Тот же паттерн `_func=None`, что и в [[Вложенные декораторы|trace]], но реализован иначе: если декоратор применили без скобок (`@retry`), функция сразу получает `decorated_func` и **рекурсивно вызывает саму себя** с именованными аргументами по умолчанию, чтобы получить настоящий `decorator`, и тут же применяет его к `decorated_func`. Если вызвали с параметрами (`@retry(max_retry_count=5, ...)`), `decorated_func` остаётся `None`, и наружу просто возвращается `decorator`.

`P = ParamSpec("P")` и `R = TypeVar("R")` в сигнатуре `Callable[P, R]` нужны, чтобы статический анализатор (mypy) видел: обёрнутая функция принимает **те же аргументы** и возвращает **тот же тип**, что и исходная — типизация декоратора не "стирается" до `Callable[..., Any]`.

Экспоненциальная задержка: `timeout` стартует с `initial_timeout` и после каждой неудачной попытки умножается на `timeout_multiplier` — 2 → 10 → 50 секунд при значениях по умолчанию (`initial_timeout=2, timeout_multiplier=5`). На последней попытке (`attempt == max_retry_count`) исключение не гасится, а **пробрасывается дальше** (`raise` без аргумента — оригинальный traceback сохраняется).

## 2. Классовый вариант ([[2.Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/retry/retry_class_dec.py|retry_class_dec.py]])

```python
class Retry:
    def __init__(self, max_retry_count=3, initial_timeout=2, timeout_multiplier=5, exceptions=(Exception,)):
        self.max_retry_count = max_retry_count
        ...

    def __call__(self, func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ...
        return wrapper

default_retry = Retry()
```

Ровно та же логика, но параметры хранятся как атрибуты `self`, а сам объект `Retry(...)` становится декоратором благодаря `__call__`. Это даёт готовый преднастроенный экземпляр (`default_retry = Retry()`), который можно переиспользовать как есть: `@default_retry`, — без повторного указания аргументов по умолчанию.

| | Функция `retry(...)` | Класс `Retry(...)` |
|---|---|---|
| Хранение настроек | в замыкании (`nonlocal`-подобный доступ через видимость) | в атрибутах `self` |
| Поддержка `@retry` без скобок | да, через рекурсивный вызов | нет — `Retry` всегда вызывается как конструктор `Retry(...)` |
| Переиспользуемый преднастроенный декоратор | нужно каждый раз звать `retry(max_retry_count=5)` | можно сохранить готовый экземпляр (`default_retry`) |

## 3. Композиция мини-проекта

- [[2.Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/retry/exceptions.py|exceptions.py]] — иерархия `BaseAPIException` → `RequestError`, чтобы `retry` мог избирательно перехватывать только сетевые ошибки, а не вообще всё.
- [[2.Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/retry/weather_fetcher.py|weather_fetcher.py]] — имитация нестабильного API: `CustomWeatherFetcher` бросает `RequestError` на каждой попытке, пока номер вызова не совпадёт с `config.success_on_attempt`; `reset_call_count()` нужен, чтобы прогнать демонстрацию повторно.
- [[2.Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/retry/config.py|config.py]] — `@dataclass Config` с `success_on_attempt` и формат логов `DEFAULT_LOG_FORMAT`.
- [[2.Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/retry/common.py|common.py]] — `run_example(func)` вызывает декорированную функцию и логирует успех/неудачу.
- [[2.Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/retry/example_retry_func.py|example_retry_func.py]] / [[2.Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/retry/example_retry_class.py|example_retry_class.py]] — одна и та же демонстрация (`fetch_weather_example_1/2`) один раз через функциональный `retry`, второй раз через классовый `Retry`/`default_retry`: оба файла импортируют один и тот же `weather_fetcher`/`common.run_example`/`config.DEFAULT_LOG_FORMAT`, различается только декоратор (`@Retry(...)` с явными параметрами против `@default_retry` с параметрами по умолчанию).

> [!WARNING] `exceptions=(Exception,)` по умолчанию — перехватывает всё
> Если не сузить `exceptions` до конкретных типов (как сделано в примерах через `RequestError`), декоратор будет ретраить **любую** ошибку, включая программные баги (`TypeError`, `AttributeError` и т.п.), которые повторный вызов не исправит — это просто отложит и замаскирует настоящую причину сбоя.

## См. также

- [[Классы-декораторы]] — базовые паттерны декораторов класса, из которых вырос приём `__call__`.
- [[Обработка исключений]] — более ранние, "черновые" версии того же retry-декоратора (`WeatherDataError.py`, `copyweather.py`) без типизации и с более узким перечнем исключений.
