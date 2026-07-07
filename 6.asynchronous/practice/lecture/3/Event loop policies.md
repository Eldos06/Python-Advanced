[[6.asynchronous/practice/lecture/3/main.py|main]]

---
tags:
  - python
  - asyncio
  - eventloop
---

# Event loop policy: Windows vs uvloop — конспект

Весь урок умещается в один короткий файл [[6.asynchronous/practice/lecture/3/main.py|main.py]], но затрагивает важную тему — какая реализация event loop реально крутит все корутины из [[Asyncio basics]] и [[Async client-server]].

```python
import os
import asyncio
import uvloop

if __name__ == "__main__":
    if 'nt' in os.name:
        asyncio.set_event_loop_policy(
            asyncio.WindowsSelectorEventLoopPolicy()
        )
    else:
        uvloop.install()
```

## 1. Зачем вообще менять политику event loop

`asyncio` не завязан на одну конкретную реализацию цикла событий — есть "политика" (`EventLoopPolicy`), которая решает, какой именно loop создавать под капотом:

- **Windows**: по умолчанию с Python 3.8 используется `ProactorEventLoop` (на основе IOCP). Он умеет полноценный subprocess/pipe I/O, но не поддерживает некоторые низкоуровневые операции (`add_reader`/`add_writer` на сокетах), которые нужны отдельным библиотекам (например, DNS-резолверам вроде `aiodns`, некоторым драйверам БД). Поэтому явно переключаются на `WindowsSelectorEventLoopPolicy` — цикл на основе `select()`, более совместимый, но без нормальной поддержки subprocess.
- **Linux/macOS**: вместо стандартного `SelectorEventLoop` можно поставить **uvloop** — реализацию event loop поверх `libuv` (той же библиотеки, что использует Node.js). `uvloop.install()` подменяет политику так, что все последующие `asyncio.run(...)` в процессе будут использовать именно uvloop. Заявленный выигрыш — в 2-4 раза быстрее стандартного loop на I/O-нагруженных сценариях.

## 2. `os.name` вместо `sys.platform`

```python
if 'nt' in os.name:
```

`os.name` на Windows равен строке `'nt'`, на Linux/macOS — `'posix'`. Проверка `'nt' in os.name` эквивалентна `os.name == 'nt'` (просто более "исторический" стиль записи, встречающийся в старом коде).

> [!WARNING] Код ничего не запускает
> В файле нет ни одной корутины и ни одного вызова `asyncio.run(...)` — весь скрипт только настраивает политику event loop и завершается. Это осознанно урезанный пример "как настроить политику", а не рабочее приложение; чтобы увидеть эффект, политику нужно установить **до** первого `asyncio.run()` в реальном скрипте (как это, например, сделано в [[Async client-server]] в варианте `errors ClientConnnectorError/`).

> [!NOTE] uvloop не работает на Windows
> Пакет `uvloop` в принципе не устанавливается на Windows (только Linux/macOS), поэтому ветка `if/else` здесь — не просто стилистика, а обязательное условие: попытка `import uvloop` и `uvloop.install()` на Windows привела бы к ошибке ещё на этапе импорта.

## Дальше по теме

- [[Asyncio basics]] — базовые примитивы, которые крутятся поверх выбранного loop.
- [[Async client-server]] — реальный пример использования `WindowsSelectorEventLoopPolicy` в HTTP-клиенте.
