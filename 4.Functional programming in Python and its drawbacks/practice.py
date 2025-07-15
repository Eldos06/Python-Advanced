# some = ['1', '2', '3']

# someInt = list(map(int, some))
# print(type(someInt[0]))


# someNumbers = [1, -2, 3, 0, -1, 4]

# def onlyPlus(x):
#     if x >= 0:
#         return x
    
# result = list(filter(onlyPlus, someNumbers))
# print(result)


#3
from operator import add


some = ['cat', 'DOG', 'FoX']

lower = list(map(str.lower, some))
# print(lower)

namePretty = [
    name.lower()
    for name in some
]
# print(namePretty)
namePretty = list(
    map(lambda s: s.lower(), some)
)
# print(namePretty)

#4
h = ['ivan ivanov', 'petr petrov']

h = [
    i.title()
    for i in h
]
# print(h)        

#5
first = [1, 2, 3] 
second = [4, 5, 6]

both = list(map(add, first, second))

#6 
def power(n):
    return n**2

someNum = [1, 2, 3, 4]

result = list(map(power, someNum))
# print(result)     

#7
someNum = [10, 11, 12, 13, 14, 15]
result = [n for n in someNum if n % 2]
# print(result)

#8
someText = [' hello ', ' world']
result = list(map(str.strip, someText))
# print(result)

#9 
s = ['1.1', '2.5', '3.3']
# print(list(map(float, s)))

#10
t = [('john', 30), ('jane', 25)]
# print(list(map(lambda x: x[0], t)))


f = ['John', 'Jane']
s = [80, 90]
# print(list(zip(f, s)))

g = ['python', 'map', 'filter'] 
# print(list(map(len, g)))

g = ['admin', '', 'user', '', 'root']

r = [i for i in g if len(i) > 0]
# print(r)


#11 ['John: 80', 'Jane: 90']

result = dict(zip(f, s))
# print(result)

a = ['python', 'map', 'filter']
# for i in a:
#     print(f"{i} ---> {len(i)}")


# 13

a = ['admin', '', 'user', '', 'root']

print(list(n for n in a if len(n)>0))
print([n for n in a if len(n)>0])


#14
def poweR(a):
    return a**2

n = [10, 20, 30]
result = list(map(poweR, n))
print(result)


#15
y = ['a', 'ab', 'abc']

print([n for n in y if len(n)> 2])








