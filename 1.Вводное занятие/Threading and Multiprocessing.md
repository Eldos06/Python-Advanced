[[1.Вводное занятие/common.py|common]] [[1.Вводное занятие/main.py|main]] [[1.Вводное занятие/await.py|await]] [[1.Вводное занятие/parallel_tasks_with_threads.py|parallel_tasks_with_threads]] [[1.Вводное занятие/parallel_tasks_with_threadpool.py|parallel_tasks_with_threadpool]] [[1.Вводное занятие/Multithreaded User Fetching with Logging and Timer.py|Multithreaded User Fetching]] [[1.Вводное занятие/Multiprocessing Pool for Parallel CPU Tasks with Logging and Timing.py|Multiprocessing Pool]] [[1.Вводное занятие/Multithreading vs Sequential Requests User Data Fetching Demo.py|Sequential vs Threaded Requests]]

---
tags:
  - python
  - concurrency
  - threading
  - multiprocessing
---

# Многопоточность и многопроцессность — вводное занятие

Папка — это прогрессия одного и того же демо (`get_users`, `get_posts`, `get_user(user_id)`, `cpu_expensive(timeout)`)
через разные модели конкурентности: последовательно → `threading.Thread` → `ThreadPoolExecutor` → `multiprocessing.Pool`.
Общая инфраструктура вынесена в [[1.Вводное занятие/common.py|common.py]].

## 1. Общая инфраструктура: `common.py`

```python
def timer(func):
    @wraps(func)
    def wrapper(*a, **kw):
        start_time = default_timer()
        result = func(*a, **kw)
        total_time = default_timer() - start_time
        logger.info("Func %s call total time %.3f", func.__name__, total_time)
        return result
    return wrapper
```

`timer` - обычный декоратор-обертка (с `functools.wraps`, чтобы не терять `__name__` функции), меряющий время выполнения.
`configure_logging()` настраивает единый формат логов для всех демок в папке (`%(funcName)`, `%(module)`, `%(lineno)`).

## 2. Последовательная версия — [[1.Вводное занятие/await.py|await.py]]

Несмотря на имя файла, `async`/`await` здесь не используется - это базовый (последовательный) вариант для сравнения:

```python
@timer
def demo_threading():
    get_users()
    get_posts()
```

`get_users`/`get_posts` эмулируют I/O-bound задержку через `sleep(1)`. Последовательно - это 2 секунды суммарно.

## 3. I/O-bound задачи: потоки

Три нарастающих по удобству варианта одной и той же идеи - распараллелить `get_users`/`get_posts`, чтобы уложиться в ~1 секунду вместо двух:

- [[1.Вводное занятие/parallel_tasks_with_threads.py|parallel_tasks_with_threads.py]] - вручную через `threading.Thread` + `start()`/`join()`:
  ```python
  thread_users = Thread(target=get_users)
  thread_posts = Thread(target=get_posts)
  thread_users.start(); thread_posts.start()
  thread_users.join(); thread_posts.join()
  ```
- [[1.Вводное занятие/parallel_tasks_with_threadpool.py|parallel_tasks_with_threadpool.py]] - тот же результат через пул `ThreadPoolExecutor`, без ручного `join`:
  ```python
  with ThreadPoolExecutor() as executor:
      executor.submit(get_users)
      executor.submit(get_posts)
  ```
- [[1.Вводное занятие/Multithreaded User Fetching with Logging and Timer.py|Multithreaded User Fetching...py]] - показывает, что `ThreadPoolExecutor` одинаково хорошо параллелит и I/O (`get_users`/`get_posts`), и (ошибочно, см. ниже) CPU-bound `cpu_expensive`.

> [!WARNING] Потоки не ускоряют CPU-bound код
> `cpu_expensive(timeout)` - чистый Python-цикл (`while timeout: timeout -= 1`), без I/O. Из-за GIL параллельные потоки
> над таким кодом выполняются практически последовательно - выигрыша по времени не будет, в отличие от I/O-bound задач.

## 4. CPU-bound задачи: процессы

[[1.Вводное занятие/Multiprocessing Pool for Parallel CPU Tasks with Logging and Timing.py|Multiprocessing Pool...py]] решает проблему GIL, реально запуская отдельные процессы:

```python
with multiprocessing.Pool() as pool:
    pool.map(cpu_expensive, [64_000_000, 72_000_000])
```

`multiprocessing.Pool` тут - аналог `ThreadPoolExecutor`, но с процессами вместо потоков: обходит GIL, поэтому
именно здесь получаем реальное ускорение на CPU-bound счетчике.

## 5. `main.py` — сводная демка

[[1.Вводное занятие/main.py|main.py]] держит все 7 вариантов (`get_users`/`get_posts` последовательно, через `Thread`,
через `ThreadPoolExecutor`, реальные HTTP-запросы `get_user` через `executor.map`, `cpu_expensive` последовательно/через
потоки/через `multiprocessing.Pool`) закомментированными построчно - удобно раскомментировать нужный вариант и сравнить
время в логах через `@timer`.

## 6. HTTP-запросы: последовательно vs потоки

[[1.Вводное занятие/Multithreading vs Sequential Requests User Data Fetching Demo.py|Sequential vs Threaded Requests Demo]]
дергает реальный API (`https://jsonplaceholder.typicode.com/users/{id}`) для 10 пользователей подряд, в цикле `for user_id in range(1, 11)`.
Это I/O-bound нагрузка (сеть) - именно такой код лучше всего выигрывает от `ThreadPoolExecutor.map`, как в [[1.Вводное занятие/main.py|main.py]] (вариант 5).

## См. также

[[multithreading vs multiprocessing]] - короткая заметка со сравнительными схемами (картинки) на ту же тему.
[[1.Вводное занятие/requirements.txt|requirements.txt]] - зависимости для примеров этой папки (в первую очередь `requests`,
используемый в `get_user`/HTTP-демках выше).
