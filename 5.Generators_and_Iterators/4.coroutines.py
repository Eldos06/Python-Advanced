import logging
from common import configure_logging

logger = configure_logging(level= logging.INFO)

def power(nums):
    for i in nums:
        yield i ** i
    
# for i in power(range(1,6)):
#     print(i)

# ✅ 1. Генератор степеней (аналог power)
# Задание: Напиши генератор, который принимает список чисел и возвращает число в степени его индекса. Например, [2, 3, 4] → 2**0, 3**1, 4**2

def power(nums: list):
    for i in nums:
        yield i ** i

myList = [2, 3, 4]

# for i in power(myList):
#     print(i, end=" ")

def waiter():
    print("what would you like?")
    order = yield
    print(f"your order: {order}")

# w = waiter()
# next(w)
# w.send("Pasta") 

# for i in waiter():
#     print(i)


# for i in w:
#     print("gonna order salad")
#     w.send("salad")
#     print("Nice one, thank you for every one")

# ✅ 2. Калькулятор: логирование операций через yield
# Задание: Создай генератор, который принимает строку вида "2 + 3" и возвращает результат. Используй .send() для передачи выражений.
def calc():
    while True:
        task = yield
        try:
            result = eval(task)
            print(f"{task} = {result}")
        except Exception as e:
            print(f"Error in calculation: {e}")

# clc = calc()
# next(clc)  # Запуск генератора
# clc.send("2 + 3")     # Выведет: 2 + 3 = 5
# clc.send("10 / 2")    # Выведет: 10 / 2 = 5.0
# clc.send("5 * 5 + 1") # Выведет: 5 * 5 + 1 = 26


# ✅ 3. Диалоговый бот-помощник
# Задание: Создай генератор, имитирующий разговор: "Как тебя зовут?", "Сколько тебе лет?", "Чем ты занимаешься?" — пользователь передаёт ответы через .send()

import logging

# Настройка логгера
# logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
# logger = logging.getLogger(__name__)\
logger = configure_logging(level= logging.INFO)

def chatbot():
    try:
        name = yield input("Бот: Как тебя зовут? ")
        logger.info(f"Получено имя: {name}")

        age = yield input(f"Бот: Приятно познакомиться, {name}! Сколько тебе лет? ")
        logger.info(f"Получен возраст: {age}")

        job = yield input(f"Бот: О, тебе {age}. А чем ты занимаешься? ")
        logger.info(f"Получена работа: {job}")

        logger.info(f"Финальный вывод: {name}, {age} лет, занимается: {job}")
    except Exception as e:
        logger.warning(f"Ошибка: {e}")
        raise StopIteration("Диалог завершён.")



# c = chatbot()
# next(c)
# c.send("")
# c.send("")
# c.send("")


# ✅ 4. Чек-лист задач
# Задание: Генератор хранит список задач. При каждой .send() добавляется новая задача. При .throw() — возвращает весь список.

import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

# def checklist():
#     task = []
#     try:
#         while True:
#             ms = yield
#             task.append(ms)
#             logger.info(f"Append --> {ms}")
#     except Exception as e:
#         logger.info(f"Finished: {e}")
#         return task
    
# ch = checklist()
# next(ch)
# ch.send("First task")
# ch.send("Second task")

# try:
#     ch.throw(Exception("Calm down"))
# except StopIteration as e:
#     print("Finally checkList:", e.value)


def menu():
    orderList = []
    try:
        while True:
            order = yield
            orderList.append(order)
            logger.info(f"Ok, Do you want another food except {order}")
    except Exception as e:
        logger.info(f"Nice one, hold on 10 min")
        return orderList
    
# m = menu()
# next(m)
# m.send("Palay")
# m.send("Kola")

# try:
#     m.throw(Exception("That is all!"))
# except StopIteration as e:
#     print("Your orders are", e.value)

import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def menu():
    order_list = []
    logger.info("🍽 Меню открыто. Введите заказ или /done для завершения.")
    try:
        while True:
            order = yield
            if not order:
                logger.warning("❗ Пустой заказ не принят")
                continue

            if order == "/done":
                logger.info("✅ Заказ завершён")
                break

            if order == "/list":
                logger.info(f"📋 Текущие заказы: {order_list}")
                continue

            order_list.append(order)
            logger.info(f"Добавлено: {order}. Что-то ещё?")
    except Exception as e:
        logger.info("🕒 Принято. Подождите 10 минут.")
    return order_list

# m = menu()
# next(m)
# m.send("Palay")
# m.send("Kola")
# m.send("/list")     # Выведет текущие заказы
# m.send("/done")     # Завершит генератор

# Получаем финальный список
# try:
#     next(m)
# except StopIteration as e:
#     print("Your orders are:", e.value)





# try:
#     g.throw(Exception("Хватит!"))
# except StopIteration as e:
#     print("Результат:", e.value)  # тут будут ["A", "B", "C"]



# ✅ 6. Игровая логика: счетчик опыта

# def counter():
#     count = 0
#     try:
#         while count <= 100:
#             ex = yield int
#             count += ex
#             if count >= 100:
#                 logger.info(f"experience enough ({count} XP)")
#                 # return count
#             else:
#                 ex = int(input(f"Not enough {100 - count} enter over {100 - count}: "))
#                 logger.info(f"experience enough ({count} XP)")
#     except Exception as e:
#         logger.info(f"Finished: {e}")
#         return count

import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def counter():
    count = 0
    try:
        while count < 100:
            xp = yield
            if not isinstance(xp, (int, float)):
                logger.warning("⛔ XP должен быть числом!")
                continue
            count += xp
            logger.info(f"🔥 Получено {xp} XP — всего {count}")
        logger.info(f"✅ Уровень повышен! Всего XP: {count}")
    except Exception as e:
        logger.info(f"💤 Преждевременное завершение: {e}")
    return count

    
# c = counter()
# next(c)
# c.send(10)
# c.send(40)
# c.send(50)

# try:
#     c.throw(Exception("Done!"))
# except StopIteration as e:
#     print("🎖 Финальный XP:", e.value)

def even_filter(target):
    try:
        while True:
            value = yield
            if value is None:
                break
            if value % 2 == 0:
                target.send(value)
    except Exception as e:
        target.throw(e)


def square(target):
    try:
        while True:
            value = yield
            if value is None:
                break
            target.send(value ** 2)
    except Exception as e:
        target.throw(e)


def summator():
    total = 0
    try:
        while True:
            value = yield
            if value is None:
                yield total  # мягкий возврат
                break
            total += value
    except Exception as e:
        print(f"Summator stopped: {e}")





s = summator()
next(s)

sq = square(s)
next(sq)

f = even_filter(sq)
next(f)

f.send(2)
f.send(3)
f.send(4)

try:
    f.send(None)
except StopIteration as e:
    print("✅ Сумма квадратов чётных чисел:", e.value)  # 4 + 16 = 20




# try:
#     f.send(None)
# except StopIteration as e:
#     print("✅ Сумма:", e.value)  # ожидаем: 2 и 4 → 4 + 16 = 20










def waiter():
    order_items = []
    print("What would U like?")
    while True:
        order = yield order_items
        if order is None:
            print("done", order_items)
            return order_items
        order_items.append(order)
        print(order, "ok, what else")

# w = waiter()
i_want_to_order = [
    "fruit salad",
    "palay",
    "kola"
]
# next(w)

# for food in i_want_to_order:
#     w.send(food)

# next(w)

class OrderCoplete(Exception):
    pass

def waiter():
    order_items = []
    print("What would U like?")
    while True:
        
        try:
            order = yield order_items
        except:
            print("done", order_items)
            return order_items
        

        if order is not None:
            order_items.append(order)
            print(order, "ok, what else")


# w = waiter()

# for food, already_order in zip(i_want_to_order, w):
#     print("already_order", already_order)
#     w.send(food)
    

# for i in range(5):
#     print(next(w))
# w.throw(OrderCoplete)


def power(num):
    p = 0
    while True:
        p = yield num ** p
        

# p = power(2)
# next(p)
# # print(p.send(3))

# for i in range(5):
#     print(i, p.send(i))
# p.close()
# for i in range(5):
#     print(i, p.send(i))

# def items_by_one(seq):
#     yield from seq

# for i in items_by_one(range(4)):
#     print(i)

def add_count():
    counter = 0
    while True:
        num = yield 
        if num is None:
            return counter
        counter += num
        print(f"counter inc by {num} now = {counter}")

def collect_counters(counters: list):
    while True:
        counter = yield from add_count()
        counters.append(counter)

numbers = []
collector = collect_counters(numbers)
# print(numbers)
# next(collector)
# collector.send(4)
# collector.send(5)
# # collector.send(None)
# print(numbers)
# collector.send(11)
# print(numbers)

