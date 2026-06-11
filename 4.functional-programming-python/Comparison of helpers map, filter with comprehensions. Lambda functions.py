# print(map.__doc__)


#1 


absNum = []

# for num in someNum:
#     absNum.append(abs(num))

# print(absNum)


# absNum = list(map(abs, someNum))
# print(absNum)

# for num in map(abs, someNum):
#     print(num)


#2
# absNum = [abs(num) for num in someNum]

# print(absNum)


#3

def square(n):
    return n*n

# squares = [square(num) for num in someNum]
# print(squares)

# print(
#     list(map(square, someNum))
# )

# squares = list(num ** 2 for num in someNum)
# print(squares)

def power(x, y):
    return x ** y

someNum = [1, 3, 6, 3, 3]
sumPowers = [10, 2, -1, -3, 0]

# for n in map(power, someNum, sumPowers):
#     print(n)

# for n in map(lambda x, y: x**y, someNum, sumPowers):
#     print(n)


# for n, p in zip(someNum, sumPowers):
#     print(n, "^", p)

# print(list(zip(someNum, sumPowers)))

# numsPower = [
#     power(a, b)
#     for a , b in zip(someNum, sumPowers)
# ]

# print(numsPower)

# numsPower = [
#     a ** b
#     for a , b in zip(someNum, sumPowers)
# ]

# print(numsPower)


from timeit import timeit

# print(
#     timeit(
#     stmt="2 ** 10"
# ))

# print(
#     timeit(
#     stmt="power(2, 10)",
#     globals={
#         "power": power
#     }
# ))

# print(
#     timeit(
#         stmt="[power(a, b) for a , b in zip(someNum, sumPowers)]",

#         globals= {
#             "power": power,
#             "someNum": someNum,
#             "sumPowers": sumPowers, 
#         }
#     )
# )

# print(
#     timeit(
#         stmt="list(map(power, someNum, sumPowers))",

#         globals= {
#             "power": power,
#             "someNum": someNum,
#             "sumPowers": sumPowers, 
#         }
#     )
# )

# print(
#     timeit(
#         stmt="[a**b for a , b in zip(someNum, sumPowers)]",

#         globals= {
#             "someNum": someNum,
#             "sumPowers": sumPowers, 
#         }
#     )
# )

# # print(
# #     timeit(
# #         stmt="list(map(lambda x, y: x**y, someNum, sumPowers))",

# #         globals= {
# #             "someNum": someNum,
# #             "sumPowers": sumPowers, 
# #         }
# #     )
# # )

# print(
#     timeit(
#         stmt="list(map(power, someNum, sumPowers))",

#         globals= {
#             "power": power,
#             "someNum": someNum,
#             "sumPowers": sumPowers, 
#         }
#     )
# )

# print(
#     timeit(
#         stmt="list(map(pow, someNum, sumPowers))",

#         globals= {
#             "someNum": someNum,
#             "sumPowers": sumPowers, 
#         }
#     )
# )


from operator import add

# print(
#     timeit(
#         stmt="list(map(someNum, sumPowers))",

#         globals= {
#             "someNum": someNum,
#             "sumPowers": sumPowers
#         }
#     )
# )

someNum = [1, 3, 6, 45,-10000,0,-3, 3]
absNum = [4, 5, 6, 7]
new = list(map(add, someNum,absNum))


# print(new)

names = [
    "suleimen yeldos",
    "botga  bahytzhon",
    "gvozdikov   vitya",
    "vitya   gvozdikov",
    "dima  petrov",
    "masha   ivanova",
    "sergey    kuznetsov",
    "alexey   novikov",
    "ivan    ivanov",
    "dima   chel",
    "frodo    baggins",
    "johnny   depp",
    "maxim   bolotov",
    "elena    krasnova",
    "egor   morozov",
    "kiril   petrov",
    "alexandr    petrovich"
]


# namePretty = [
#     name.title()
#     for name in names
# ]



# namePretty = list(
#     map(lambda s: s.title(), names)
# )

# namePretty = list(map(str.title, names))

# print(namePretty)


# print(
#     timeit(
#     stmt="[name.title() for name in names]",

#     globals= {
#         "names" : names
#     },

#     number=1_000_000 
# ))

# print(
#     timeit(
#     stmt="list(map(lambda s: s.title(), names))",

#     globals= {
#         "names" : names
#     },

#     number=1_000_000 
# ))

# print(
#     timeit(
#     stmt="list(map(str.title, names))",

#     globals= {
#         "names" : names
#     },

#     number=1_000_000 
# ))

# for num in filter(lambda n: n >= 0,someNum):
#     print(num)

# posetiveNum = list(filter(lambda n: n >= 0,someNum))
# print(posetiveNum)

# posetiveNum = [n for n in someNum if n >= 0]
# print(posetiveNum)

def isNotNegative(n):
    return n >= 0

# notNegative = list(filter(isNotNegative, someNum))

# print(notNegative)

from timeit import timeit

someNum = [1, -2, 3, 0, -1, 4, -3]
isNotNegative = lambda n: n >= 0

# print(
#     timeit.timeit(
#         stmt="[n for n in someNum if n >= 0]",
#         globals={"someNum": someNum},
#         number=1_000_000
#     )
# )

# print(
#     timeit.timeit(
#         stmt="list(filter(isNotNegative, someNum))",
#         globals={"someNum": someNum, "isNotNegative": isNotNegative},
#         number=1_000_000
#     )
# )

# print(
#     timeit.timeit(
#         stmt="list(filter(lambda n: n >= 0,someNum))",
#         globals={"someNum": someNum},
#         number=1_000_000
#     )
# )



numbers = list(range(1, 11))
print(numbers)

evens = [n for n in numbers if n % 2 == 0]
print(evens)
odds = [n for n in numbers if n % 2 != 0]
print(odds)

print(
    timeit(
    stmt = "[n for n in numbers if n % 2 == 0]",
    globals = {
        "numbers": numbers
    },
    number=1_000_000
)
)

print(
    timeit(
    stmt = "[n for n in numbers if n % 2 != 0]",
    globals = {
        "numbers": numbers
    },
    number=1_000_000
)
)

print(
    timeit(
    stmt = "[n for n in numbers if n % 2]",
    globals = {
        "numbers": numbers
    },
    number=1_000_000
)
)



