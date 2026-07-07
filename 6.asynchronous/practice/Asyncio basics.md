[[6.asynchronous/practice/easy.py|easy]] [[6.asynchronous/practice/middle.py|middle]] [[6.asynchronous/practice/lecture/1/1.py|1]]

---
tags:
  - python
  - asyncio
---

# Asyncio: основы — конспект

Разбор базовых механик `asyncio` на примерах из [[6.asynchronous/practice/easy.py|easy.py]], [[6.asynchronous/practice/middle.py|middle.py]] и [[6.asynchronous/practice/lecture/1/1.py|1.py]]: корутины, `asyncio.run`, `gather`, `create_task`, `run_in_executor`, `wait`.

## 1. Корутина и `asyncio.run`

Функция, объявленная через `async def`, при вызове не выполняется сразу — она возвращает объект корутины. Чтобы тело реально выполнилось, корутину нужно либо `await`-нуть, либо передать в `asyncio.run(...)`:

```python
async def hell0() -> None:
    log.info("Starting ...")
    await sleep(2)
    log.info("Hello")
    log.info("Done")

# run(hell0())
```

> [!WARNING] Забытый `run()`/`await`
> В `easy.py` почти все вызовы `main()`/`hell0()` закомментированы (`# run(hell0())`). Если просто написать `hell0()` без `await`/`run()`, тело функции не выполнится вообще — Python создаст объект корутины и молча его отбросит, выдав `RuntimeWarning: coroutine 'hell0' was never awaited`. Частая ошибка новичков.

## 2. `asyncio.gather` — параллельный запуск нескольких корутин

```python
async def main():
    results = await asyncio.gather(
        first(),
        second(),
        third()
    )
    log.info(f"Results: {results}")
```

`gather` запускает все переданные корутины конкурентно (на одном потоке, переключаясь на `await`) и возвращает список результатов **в том же порядке**, в котором были переданы корутины — независимо от того, какая из них завершится быстрее.

## 3. `asyncio.create_task` — запуск "в фоне" прямо сейчас

В отличие от простой корутины, `create_task` сразу планирует выполнение в event loop, не дожидаясь `await`. Пример из `middle.py`, где нужно проверить цены сразу нескольких товаров:

```python
async def task(product, price):
    global finallyCheck
    await asyncio.sleep(1)
    finallyCheck += price
    return {"product": product, "price": price}

async def main():
    selected = products[:5]
    tasks = [asyncio.create_task(task(p, randint(10, 100))) for p in selected]
    results = await asyncio.gather(*tasks)
```

Все 5 задач уходят "в полёт" одновременно ещё на этапе list comprehension, а `gather(*tasks)` лишь дожидается их завершения — поэтому суммарное время ≈ 1 секунда, а не 5.

> [!NOTE] Глобальное состояние
> `finallyCheck` — обычная глобальная переменная, к которой параллельно обращаются несколько задач. Здесь это безопасно, т.к. между `await asyncio.sleep(1)` и `finallyCheck += price` нет других точек переключения на другую задачу, но в общем случае конкурентная мутация общего состояния без блокировок — источник гонок.

## 4. Мост к блокирующему коду: `run_in_executor`

`input()` — блокирующая функция, её нельзя просто вызвать внутри корутины с `await`. `TrainingBrain` в `middle.py` решает это через executor:

```python
loop = asyncio.get_running_loop()
while True:
    user_input = await loop.run_in_executor(None, input, "Enter your answer: ")
    try:
        CheckNum = int(user_input)
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
```

`run_in_executor(None, ...)` уводит блокирующий вызов в дефолтный `ThreadPoolExecutor`, event loop при этом не блокируется и может обслуживать другие задачи.

## 5. `asyncio.wait` и отмена зависших задач

`1.py` разбирает более "ручной" способ дождаться группы задач — через `asyncio.wait`, а не `gather`:

```python
async def get_n_stocks(n_stock: int):
    tasks = {
        asyncio.create_task(get_stock(name=f"Kaspi {i:03}"), name=f"get-stock-{i}")
        for i in range(1, n_stock + 1)
    }
    done, pending = await asyncio.wait(tasks)
    for task in pending:
        task.cancel()
```

`wait` возвращает два множества — `done` и `pending`. По умолчанию (`return_when=ALL_COMPLETED`) `wait` вернётся только когда завершатся **все** задачи, поэтому `pending` в этом коде всегда будет пустым множеством, а цикл `task.cancel()` — мёртвый код. Отмена реально имела бы смысл только с `return_when=FIRST_COMPLETED` или с `timeout=...`.

> [!WARNING] Баг в `get_stock`
> ```python
> async def get_stock(name: str) -> int:
>     to_sleep = random()
>     if random > 0.4:        # сравнивается сама функция random, а не результат вызова random()
>         raise ValueError(name)
> ```
> `random` здесь — это импортированная функция `from random import random`, а не число. Сравнение функции с `float` (`if random > 0.4`) в Python 3 упадёт с `TypeError: '>' not supported between instances of 'builtin_function_or_method' and 'float'`. Нужно было `if random() > 0.4:` — правильный вызов, как строкой выше для `to_sleep`.

## Дальше по теме

- [[Async client-server]] — те же `gather`/`create_task`, но поверх реального HTTP через `aiohttp`.
- [[Event loop policies]] — какой именно event loop крутит все эти корутины.
- [[Aiofiles and currency project]] — асинхронная работа с файлами поверх тех же примитивов.

## Зависимости раздела

[[6.asynchronous/requirements.txt|requirements.txt]] - зависимости для всего раздела `6.asynchronous` (`aiohttp`, `aiofiles` и т.д.),
общие для всех уроков ниже (`Async client-server`, `Aiofiles and currency project`, `Aiohttp polls demo`).
