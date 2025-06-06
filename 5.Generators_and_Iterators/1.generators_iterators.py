name = "Yeldos"
# import "\file"
# print("Hi", name)

# times = 0
# while times < 5:
#     print("Hi", name)
#     times += 1

#3
numbers = [i for i in range(1, 6)]

# for num in numbers:
    # print(num)


#4
data = {
    "foo": "bar",
    "sdu": "turk"
}

# for key in data:
#     data.pop(key)


# for i in range(1, 5):
#     print(i)

# for i in range(1000000):
#     print(i)
#     if i > 7:
#         break


r = range(0, 7)
# print(r)

# for i in r:
#     print(i)
#     if i > 3:
#         break

# g = list(map(lambda n: n*n, range(8)))
# print(g)
# for i in g:
#     print(i)
#     if i > 6:
#         break
# print()
# print(next(g))
# for i in g:
#     print(i)

file = "file.txt"

# with open(file, "w") as f:
#     f.writelines(
#         [
#             f"line {i} \n"
#             for i in range(1, 101)
#         ]
#     )

with open(file, "r") as f:
    for line in f:
        print(repr(line))
        if "7" in line:
            break

    print("One more line:")
    print(repr(next(f)))