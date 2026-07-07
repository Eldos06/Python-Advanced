[[9.AnotationType/4.instpect/inspect.ipynb|inspect]]

---
tags:
  - python
  - inspect
  - decorators
  - introspection
---

# Модуль `inspect`

`inspect` - стандартная библиотека для интроспекции объектов в рантайме: определить, что за объект перед тобой
(функция/генератор/корутина), и разобрать его сигнатуру программно.

## 1. `is*` проверки типа объекта

```python
def func(): pass
def gen(): yield
async def afunc(): pass

inspect.isfunction(func)           # True
inspect.isfunction(gen)            # True  - обычная функция ДО вызова, генератором становится результат её вызова
inspect.isgenerator(func)          # False - func() ещё не вызвана
inspect.isgeneratorfunction(gen)   # True  - а вот это проверяет именно "функция с yield внутри"
inspect.iscoroutinefunction(afunc) # True
```

> [!NOTE] Разница `isgenerator` vs `isgeneratorfunction`
> `gen` - это обычный объект-функция, пока её не вызвали. `isgeneratorfunction(gen)` смотрит на **байт-код**
> функции (есть ли в ней `yield`) и потому `True` ещё до вызова. `isgenerator(gen())` (уже вызванный объект)
> проверял бы, что это именно генератор-итератор, а не функция.

## 2. Как `@wraps` чинит интроспекцию декорированной функции

Без `functools.wraps`:

```python
def log_dec(func):
    def wrapper(*a, **kw):
        ...
    return wrapper

@log_dec
def power(num, e): ...

power.__name__  # 'wrapper' - имя и сигнатура исходной функции потеряны
```

С `@wraps(func)`:

```python
from functools import wraps

def log_dec(func):
    @wraps(func)
    def wrapper(*a, **kw): ...
    return wrapper

power        # <function __main__.power(num, e)> - имя и подпись снова видны инструментам (IDE, help(), inspect)
power.__wrapped__  # ссылка на оригинальную (недекорированную) функцию - wraps добавляет и её
```

`@wraps` не только копирует `__name__`/`__doc__`, но и кладёт `__wrapped__` - по нему `inspect.signature()` и
подобные умеют "просвечивать" обёртку и достать реальную сигнатуру исходной функции.

## 3. `inspect.getfullargspec` — разбор сигнатуры

```python
def func(a: int, b: int, c: int = 0.5, *, d=None) -> list: ...

inspect.getfullargspec(func)
# FullArgSpec(args=['a', 'b', 'c'], varargs=None, varkw=None,
#             defaults=(0.5,), kwonlyargs=['d'], kwonlydefaults={'d': None},
#             annotations={'return': list, 'a': int, 'b': int, 'c': int})
```

`args` - позиционные/позиционно-именованные параметры, `kwonlyargs` - те, что после `*` (только по имени),
`varargs`/`varkw` - имена `*args`/`**kwargs`, если они есть в сигнатуре.

### Практическое применение: безопасный вызов колбэка с "лишними" kwargs

```python
async def safe_callback(callback, **kwargs):
    spec = inspect.getfullargspec(callback)
    if spec.varkw:
        accepted_kwargs = kwargs                     # есть **kwargs - колбэк примет всё
    else:
        accepted_args = spec.args + spec.kwonlyargs
        accepted_kwargs = {k: v for k, v in kwargs.items() if k in accepted_args}  # фильтруем лишнее

    if inspect.iscoroutinefunction(callback):
        result = await callback(**accepted_kwargs)   # async-функцию нужно await'ить
    else:
        result = callback(**accepted_kwargs)          # обычную - вызвать напрямую
    return result
```

Идея: `safe_callback` не знает заранее, какую функцию ей передадут (обычную или `async def`, с конкретными
параметрами или без) - `getfullargspec` позволяет на лету отфильтровать только те `kwargs`, которые колбэк реально
примет (не упасть с `TypeError: unexpected keyword argument`), а `iscoroutinefunction` решает, нужно ли `await`.
Это и есть паттерн, который используют DI-фреймворки и веб-роутеры (FastAPI, pytest fixtures) под капотом.
