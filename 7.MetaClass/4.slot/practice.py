from sys import *
"""
Задание 1. Базовое поведение __slots__
Создай класс Car с полями brand и year, используя __slots__.

Создай объект.

Попробуй добавить атрибут color после создания объекта.

Зафиксируй, какое исключение возникает и почему.
"""
class Car:
    __slots__ = ['brand', 'year']
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


# colalt = Car('Chevlorete', 2020)
# colalt.color = 'brown' #AttributeError: 'Car' object has no attribute 'color'
# print(colalt.color)


"""
Задание 2. Сравнение с классом без __slots__
Создай два класса UserA (без __slots__) и UserB (с __slots__ = ('name', 'age')).

Создай по 10 000 объектов каждого класса.

Сравни getsizeof() одного объекта.

Объясни, почему разница не равна реальной экономии памяти.
"""
class Bus:
    # __slots__ = ['brand', 'year']
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

# print(getsizeof(Car))
# print(getsizeof(Bus))

"""
Задание 3. __dict__ и __slots__

Создай класс Book без __slots__ и выведи book.__dict__.

Создай аналогичный класс со __slots__.

Попробуй получить __dict__ у объекта со __slots__.

Объясни, что произошло.
"""
class Book:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

# book = Book('soccer', 1999)
# print(book.__dict__)

class Note:
    __slots__ = ['title', 'content']
    def __init__(self, title, content):

        self.title = title
        self.content = content



onenote = Note('onenote', 1000)
# print(onenote.__dict__) #AttributeError: 'Note' object has no attribute '__dict__'. Did you mean: '__dir__'?

# del onenote.content
# note = Note('onenote', 1999)
# print(note.content)
# print(onenote.content)
#
# note = Note('onenote', 200)
# print(note.content)

"""
Задание 5. Наследование и __slots__
Создай:

класс Animal со __slots__ = ('species',)

класс Dog(Animal) со __slots__ = ('breed',)

Создай объект Dog.

Проверь доступность всех атрибутов.

Попробуй добавить новый атрибут.

Объясни, как __slots__ работают при наследовании.
"""

class Animal:
    __slots__ = ['species']
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    __slots__ = ['breed']
    def __init__(self, breed, species):
        super().__init__(species)
        self.breed = breed
#
# tiktok = Dog('mazhki', 'yellow')
# print(tiktok.__slots__)

"""
Задание 6. Когда нужен __dict__ в слотах
Создай класс FlexibleUser с __slots__ = ('name', 'age', '__dict__').

Добавь динамический атрибут (email).

Выведи vars() объекта.

Объясни, зачем иногда сознательно добавляют __dict__.
"""
class FlexibleUser:
    # Fixed attributes go to slots; dynamic attributes go to __dict__
    __slots__ = ("name", "age", "__dict__")

    def __init__(self, name: str, age: int, email: str):
        self.name = name      # stored in slots
        self.age = age        # stored in slots
        self.email = email    # stored in __dict__ (dynamic attribute)


# --- Demo / checks ---

user1 = FlexibleUser("John", 10, "240116042@sdu.edu.kz")
# print()
# # __dict__ exists because we included '__dict__' in __slots__
# print("user1.__dict__:", user1.__dict__)
# print("vars(user1):   ", vars(user1))          # same as user1.__dict__
# print("slots on class:", FlexibleUser.__slots__)
# print()
# # Change a slotted attribute: it does NOT appear in __dict__
# user1.name = "Yeldos"
# print("after name change, __dict__:", user1.__dict__)
# print("name:", user1.name, "| age:", user1.age, "| email:", user1.email)
# print()
# # Add another dynamic attribute (allowed because __dict__ is present)
# user1.country = "KZ"
# print("after adding country, __dict__:", user1.__dict__)
# print()
# # Prove that fixed fields are not duplicated in __dict__
# print("'name' in __dict__?", "name" in user1.__dict__)
# print("'age'  in __dict__?", "age" in user1.__dict__)
# print("'email'in __dict__?", "email" in user1.__dict__)
# print("country in __dict__?", "country" in user1.__dict__)
# print()
# # Optional: delete a slotted attribute and see behavior
# del user1.name
# try:
#     print(user1.name)
# except AttributeError as e:
#     print("Expected error after del user1.name:", e)


"""
Задание 7. dataclass(slots=True)
Создай @dataclass(slots=True) с полями title и pages.

Создай объект.

Попробуй добавить новый атрибут.

Выведи Class.__slots__.

Сравни поведение с обычным __slots__.
"""

from dataclasses import dataclass
@dataclass(slots = True)
class Book:
    title: str
    pages: int
    # def __init__(self, title, pages):
    #     self.title = title
    #     self.pages = pages
    def info(self):
        return f"Title: {self.title}, Pages: {self.pages}"

# atomic = Book("atomic", 10)
# print(atomic.info())
# print(atomic.__slots__)

class Example3:
    __slots__ = ["slot_0"]

    def set_0(self, _value):
        self.__slots__[0] = _value

    def get_0(self):
        return self.__slots__[0]



a = Example3()
b = Example3()

a.set_0("zero")
b.set_0("not zero")
a.slot_0 = 0

print(f"a.get_0() {a.get_0()}")
print(f"a.slot_0   {a.slot_0}")



