[[pet PROJECT/main.py|main]]

---
tags:
  - python
  - asyncio
  - pet-project
---

# Math trainer — pet-проект на asyncio

Мини-тренажёр устного счёта: генерирует случайный пример (`FNum symbol SNum`), асинхронно ждёт ответ с клавиатуры
и проверяет его, плюс отдельная демка параллельного запуска через `TaskGroup`.

## 1. Асинхронный `input()` — [[pet PROJECT/main.py|main.py]]

```python
loop = asyncio.get_running_loop()
user_input = await loop.run_in_executor(None, input, "Enter your answer: ")
```

`input()` - блокирующая функция (ждёт клавиатуру), её нельзя просто вызвать в `async def` без блокировки всего
event loop. `run_in_executor(None, func, *args)` уводит вызов в отдельный поток из пула по умолчанию (`None`) и
возвращает awaitable - event loop свободен обрабатывать другие корутины, пока пользователь думает над ответом.

```python
while True:
    user_input = await loop.run_in_executor(...)
    try:
        CheckNum = int(user_input)
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
```

Цикл с `try/except ValueError` - защита от нечислового ввода: пока пользователь не введёт что-то конвертируемое
в `int`, вопрос не отпускает.

> [!WARNING] `raise ValueError("not zero %s", SNum)` не форматирует строку
> В отличие от `logger.warning("...%s", SNum)`, у исключений `%s`-подстановка **не** применяется автоматически -
> `ValueError(msg, arg)` просто кладёт кортеж `("not zero %s", SNum)` в `.args`, и `str(exc)` покажет что-то вроде
> `('not zero %s', 0)`, а не отформатированную строку. Для форматирования сообщения исключения нужна f-строка:
> `ValueError(f"not zero {SNum}")`.

## 2. `TaskGroup` и фильтрация успешных результатов

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        one = tg.create_task(first_training_session())
        two = tg.create_task(second_training_session())

    results = [one.result(), two.result()]
    successful_results = filter_successful_tasks(results)
```

```python
def filter_successful_tasks(results):
    return [r for r in results if not isinstance(r, Exception)]
```

`TaskGroup` запускает `first_training_session`/`second_training_session` параллельно и дожидается обеих на выходе
из `async with` (аналог `asyncio.gather`, но с более строгой обработкой ошибок).

> [!NOTE] `filter_successful_tasks` тут не сможет ничего отфильтровать
> `asyncio.TaskGroup`, в отличие от `asyncio.gather(..., return_exceptions=True)`, не кладёт исключения в
> результаты задач - если любая из задач в группе упадёт, `TaskGroup` отменяет остальные и перевыбрасывает
> ошибку как `ExceptionGroup` **на выходе из `async with`**, до строки `results = [...]`. Поэтому `results` в
> этом коде физически не может содержать `Exception` - `filter_successful_tasks` написан под паттерн
> `gather(return_exceptions=True)`, а используется с `TaskGroup`, где до неё просто не дойдёт выполнение при ошибке.
