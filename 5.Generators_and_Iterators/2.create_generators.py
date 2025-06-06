# squares = [i for i in range(7)]

# print(squares)

# for i in (i*i for i in range(7)):
#     print(i)


# squares_g = ((i*i for i in range(777777)))

# for i in squares_g:
#     print(i)
#     if i > 70:
#         break



# print(func_g)
# g = func_g()

# print(g)
# print(next(g))
# print(next(g))

# for i in func_g():
    # print(i)


def func_g():
    # print("Start func g")
    yield 9
    print("func g after 9")
    yield 42
    print("final line ")

g = func_g()
print(g)
# print(g)

print(next(g))
# print(next(g))
# print(next(g))

# for i in func_g():
    # print("i", i)

# def fib():
#     a = 0
#     b = 1 
#     while True:
#         yield a
#         a, b = b, a + b
# f = fib()

# for i in f:
#     # print(i)
#     if i > 10:
#         break

# nextOne = [next(f) for i in range(10)]
# nextOne = [next(f) for i in range(10)]
# print(nextOne)

# squaresForOdds = (i*i for i in range(20) if i % 2)

# squaresForOdds = filter(lambda x: x % 13 == 0, range(1))

# for i in squaresForOdds:
    # print(i)
    
# g = [i for i in range(1, 20) if i % 13 == 0]
# print(g)

# print(
#     next(
#         (i for i in range(1, 1000) if i % 13 == 0),
#         -1
#     )


# )

# names = ["Yeldos", "Jaras", "Botga", "Assel"]

# print(
#     next(
#        ( n for n in names if n.startswith("J")),
#        "default"
#     )
# )


# def gen_squares(n): 
#     for i in range(1, n + 1): 
#         print("gen sq for", i) 
#         yield i * i 
# g = gen_squares()
# for i in g: 
#     print(i) 
#     # if i > 7: 
#     #     break






