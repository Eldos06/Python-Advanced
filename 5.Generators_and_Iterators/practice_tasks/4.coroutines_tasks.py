#Создай генератор, который по одному выдаёт квадраты чисел от 1 до N включительно.

# def power(num):
#     for i in range(num+1):
#         yield i ** 2
        

# num = int(input("num ~~> "))
# p = power(num)
# next(p)
# for i in power(num):
#     print(i)
   
# def power(num):
#     while True:
#         num = yield
#         yield num ** 2



# p = power(4)
# print(p)
# next(p)
# print(p)
# print(power(4))
# print(p.send(3))

#the best solution that I ever done
# num = int(input("num ~~> "))
# p = power(num)
# next(p)
# print(p.send(num))

#=======================

#2 Пропуск чётных Генератор, который выдаёт только нечётные числа из списка. Используй yield, не return.

# nums = [1, 2, 3, 4, 5, 6, 7]

# def only_odds(numbers):
#     for n in numbers:
#         if n % 2:
#             yield n

# odds = list(only_odds(nums))
# print(odds)

#3 Парсинг строк: Генератор, принимающий список строк, и по send выдаёт длину каждой строки, которую ты передал.

# def your_generator():
#     text = ''
#     while True:
#         text= yield len(text)
    


# g = your_generator()     # создаёшь генератор
# next(g)                  # активируешь его

# print(g.send("hello"))   # → 5
# print(g.send("banana"))  # → 6
# print(g.send(""))        # → 0

#4 Сумматор с остановкой Генератор, который прибавляет каждое новое число (send), пока не получит None. Потом возвращает общую сумму.

def add_nums():
    my_list = []
    while True:
        num = yield
        if num is None:
            return sum(my_list)
        my_list.append(num)



# g = add_nums()
# next(g)              # запустить генератор
# g.send(4)            # +4
# g.send(7)            # +7
# g.send(1)            # +1
# try:    
#     g.send(None)     # ← завершает и вернёт сумму
# except StopIteration as e:
#     print("Сумма:", e.value)   # → Сумма: 12

#5 Итерирование по вложенным спискам Генератор yield from, который по очереди выдаёт все элементы вложенных списков: [[1, 2], [3, 4]] → 1,2,3,4

# [[1, 2], [3, 4]] → 1,2,3,4


# def listPrint(multiList):
#     for i in multiList:
#         for j in i:
#             print(j, end=" ")
# try:
#     m = listPrint([[1, 2], [3, 4]])
# except TypeError as t:
#     print(f"=====  {t.value}  =====")

# def flatten(nested):
#     for sublist in nested:
#         yield from sublist


# nested = [[1, 2], [3, 4]]
# for val in flatten(nested):
#     print(val, end=" ")

# Генератор лога Генератор, который принимает сообщения через send, и добавляет их в лог. Если отправлено None, возвращает список всех сообщений.

def log_gen():
    pass

g = log_gen()
next(g)
g.send("Start server")     # лог: ["Start server"]
g.send("Request /home")    # лог: ["Start server", "Request /home"]
g.send("DB connected")     # лог: ["Start server", "Request /home", "DB connected"]
g.send(None)               # ← вернёт список всех сообщений

