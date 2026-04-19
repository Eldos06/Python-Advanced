from sys import *

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# user1 = User('John', 36)
# user2 = User('John', 36)
# print(user1.name, user2.name)
# print(user1.name)
# print(user1.age)
#
#
#
# user1.email = '321452@sdu.edu.kz'
# print(user1.email)
# print(vars(user1))
# print(vars(user2))
#
# print(getsizeof(user1))

class User:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


user1 = User('John', 36)
user2 = User('John', 36)
print(user1.name, user2.name)
print(user1.name)
# user1.email = '321452@sdu.edu.kz'
print(User.__slots__)
print(user1.__slots__)
del user1.name
# print(user1.name) #AttributeError: 'User' object has no attribute 'name'

from dataclasses import dataclass

@dataclass(slots=True)
class User:
    username: str
    age: int


print(User.__slots__)
# print(Student.__slots__)

@dataclass(slots=True, frozen=True)
class User:
    username: str
    age: int

yeldos = User('Yeldos', 36)
yeldos.name = 'Yerbol'
print(yeldos.name)
print(yeldos.age)

