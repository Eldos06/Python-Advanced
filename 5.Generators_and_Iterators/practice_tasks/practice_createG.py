
# num = int(input("~~> "))
# n = (i for i in range(num) if i % 2 == 0)

# def even_numbers(g):
#     for i in n:
#         print(i)


# even_numbers(n)


#        13   → 1 + 3 = 4  
#        205  → 2 + 0 + 5 = 7  
#        7    → 7
# nums = [13, 205, 7]

# def digits_sum_gen(nums: list[int]):
#     for number in nums:
#         yield sum(int(digit) for digit in str(number))

# g = digits_sum_gen([13, 205, 7])

# for i in g:
#     print(i)

# s = (i for i in range(num) if i % 7 == 0)

# def seven(n):
#     for i in n:
#         print(i**2)


# seven(s)


# def char_gen(s: str):
#     for char in s:
#         if char.isalpha():  # проверка: это буква?
#             yield char


# text = "He11o, w0rld!🔥"

# for c in char_gen(text):
#     print(c)

# ⚙️ УРОВЕНЬ 2 — норм по-пацански









# 🧠 УРОВЕНЬ 3 — "Чо за хрень?" (прокачка)


# Сделай генератор вложенных списков, который по списку вроде [[1,2], [3], [4,5]] будет поэлементно всё плоско отдавать.

# Генератор со state reset: после 5 вызовов начинает выдавать "RESET", потом снова числа с 0.

# Напиши генератор, который повторяет каждый элемент в списке N раз.

# Генератор window_gen(seq, size) — скользящее окно из элементов: window_gen([1,2,3,4], 2) → (1,2) (2,3) (3,4)

# 👑 УРОВЕНЬ 4 — чтобы ты охренел
# Генератор с yield from — сделай итератор по списку списков, который использует yield from для разворачивания.

# Сделай генератор repeat_until(predicate, gen), который отдаёт значения другого генератора пока predicate(x) == False.

# Генератор с try/except внутри: кидай ValueError при x < 0, иначе yield x * 2.

# Генератор на map + filter в одной строке — замени все буквы на верхний регистр, но только те, что длиной > 3.

# Генератор-миксер: получает 2 генератора и чередует их значения: (a1, b1, a2, b2, ...).


# def infinite_zeros():
#     yield 0
#     # return 0

# g = infinite_zeros()
# while True:
#     print(g)


# start, end = list(map(int, input("~> ").split(" ")))


# def square(start, end):
#     for i in range(start, end+1):
#         yield i ** 2


# for x in square(start, end):
#     print(x)

# 0 1 1 2 3 5 8 ....
# n = int(input("~~> "))

# def fib(a):
#     if a <= 1:
#         yield a
#     else:
#         yield fib(a - 1) + fib(a - 2)

# for i in fib(n):
#     print(i)
# num = int(input())

# def even(n):
#     for i in range(n + 1):
#         if i % 2==0:
#             yield i

# print(list(even(num)))

# def even_only(n):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i

# # тест
# print(list(even_only(20)))

# def zero():
#     return 0

# while True:
#     print(zero())


# n = int(input('~~> '))
# def fib_n(n: int):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# for i in fib_n(n):
#     print(i)




# import re

# def palindromes_only(text):
#     words = re.findall(r'\b\w+\b', text.lower())  # берём только слова
#     for word in words:
#         if word == word[::-1] and len(word) > 1:
#             yield word

# # тест
# for w in palindromes_only("Шалаш казак не ел. Потоп был. Но мама — нет!"):
#     print(w)


# Генератор делителей: get_divisors(n) → выдаёт все делители числа n.
# def get_divisors(n):
#     for i in range(2, n//2):
#         if n % i == 0:
#             yield i
#             i += 1
        
        
# for i in get_divisors(10):
#     print(i)

# num = int(input("~> "))

# get_divisors = (i for i in range(1,num+1) if num % i == 0)

# for i in get_divisors:
#     print(i)
   

# Генератор пар (i, i²) из диапазона до n.

# def myfunc(num):
#     for i in range(num+1):

#         yield i, i**2

# for i in myfunc(11):
#     print(i)


# def myfunc(a: list):
#     for i in range(1, len(a)):
#         if a[i] > a[i - 1]:
#             yield a[i]

# a = [1, 3, 2, 5, 4, 6]

# for i in myfunc(a):
#     print(i)

# Напиши генератор prime_gen() — выдаёт простые числа бесконечно.
n = 1
def prime_gen(n):
    while True:
        yield n**n + n + 41
        print()
        n += 1

for i in prime_gen(n):
    print(i)



