from abc import ABC, abstractmethod
#



# # user.name = 'Yeldos'
# # # log(user.name)

# # log(vars(user))

# # log(object.__getattribute__(user, 'name'))

# # log(type.__getattribute__(User, 'name'))

# class User:
#     def __init__(self, username):
#         self.username = username
#
#     @property
#     def email(self):
#         return f"{self.username}@example.com".lower()


# user = User("Sam")
# # log(user.username)
# # log(user.email)


# # class EmailDescriptor:
# #     def __get__(self, instance, owner):
# #         return f"{instance.username}@example.com".lower()


# # class User:
# #     def __init__(self, username):
# #         self.username = username

# #     email = EmailDescriptor()


# # user = User("Yerbol")
# # log(user.username)
# # log(user.email)



# # log(vars(User))
# # print()
# # log(vars(user))

# class EmailDescriptor:
#     def __init__(self, domain):
#         self.domain = domain

#     def __get__(self, instance, owner):
#         return f"{instance.username}@{self.domain}".lower()

# class User:
#     def __init__(self, username):
#         self.username = username

#     email = EmailDescriptor(domain="example.org")

# user = User("Yerbol")
# # log(user.username)
# # log(user.email)

# # # log(User.email)
# # log(vars(User))
# # log(vars(User)['email'])
# # vars(User)['email'].domain = 'abc.org'
# # log(vars(User)['email'].domain)

# # print(user.username)
# # print(user.email)

# class  Validator(ABC):

#     def __set_name__(self, owner, name):
#         self.attr_name = '_' + name

#     def __get__(self, instance, owner):
#         print('get attr', self.attr_name)
#         return getattr(instance, self.attr_name)

#     def __set__(self, instance, value):
#         print('validate', repr(value), 'before setting to', self.attr_name)
#         value = self.validate(value)
#         print('set', repr(value), 'to attr', self.attr_name)
#         setattr(instance, self.attr_name, value)


#     @abstractmethod
#     def validate(self, value):
#         pass


# class LowerStr(Validator):
#     def validate(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f'Value {value} has to be type {str}, not {type(value)}')
#         return value.lower()

# class Number(Validator):
#     def __init__(self, min_value=None, max_value=None):
#         self.min_value = min_value
#         self.max_value = max_value

#     def validate(self, value):
#         if not isinstance(value, int):
#             raise TypeError(f"Value {value} has to be type {int}, not {type(value)}")
#         value = int(value)

#         if self.min_value is not None and value < self.min_value:
#             raise ValueError(f"Value {value} is less than {self.min_value}")

#         if self.max_value is not None and value > self.max_value:  # 👈 исправлено
#             raise ValueError(f"Value {value} is greater than {self.max_value}")

#         return value



# class Node:
#     name = LowerStr()
#     value = Number(min_value=1, max_value=10)

#     def __init__(self, name, value):
#         self.name = name
#         self.value = value


# node = Node("HeLLo", 5)
# print(node.name)   # hello
# print(node.value)  # 5

# node = Node("test", 0)  # ❌ ValueError: Value 0 is less than 1

from abc import ABC, abstractmethod
from common import configure_logging
import logging


configure_logging()

# удобная функция, как print()
def log(message, *args, level=logging.INFO, **kwargs):
    logging.log(level, str(message), *args, **kwargs)


# ==== Пример с property ====
class User:
    def __init__(self, username):
        self.username = username

    @property
    def email(self):
        return f"{self.username}@example.com".lower()


user = User("Sam")
# log(user.username)
# log(user.email)


# ==== Пример с простым дескриптором ====
class EmailDescriptor:
    def __init__(self, domain):
        self.domain = domain

    def __get__(self, instance, owner):
        return f"{instance.username}@{self.domain}".lower()


class User:
    def __init__(self, username):
        self.username = username

    email = EmailDescriptor(domain="example.org")


user = User("Yerbol")
# log(user.username)
# log(user.email)
# log(vars(User))
# log(vars(User)['email'].domain)












# ==== Абстрактный валидатор ====
class Validator(ABC):
    def __set_name__(self, owner, name):
        self.attr_name = '_' + name

    def __get__(self, instance, owner):
        print('get attr', self.attr_name)
        return getattr(instance, self.attr_name)

    def __set__(self, instance, value):
        print('validate', repr(value), 'before setting to', self.attr_name)
        value = self.validate(value)
        print('set', repr(value), 'to attr', self.attr_name)
        setattr(instance, self.attr_name, value)

    @abstractmethod
    def validate(self, value):
        pass


# ==== Валидатор строки ====
class LowerStr(Validator):
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Value {value} has to be type {str}, not {type(value)}')
        return value.lower()


# ==== Валидатор числа ====
class Number(Validator):
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Value {value} has to be type {int}, not {type(value)}")
        value = int(value)

        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Value {value} is less than {self.min_value}")

        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Value {value} is greater than {self.max_value}")

        return value


# ==== Класс с валидируемыми атрибутами ====
class Node:
    name = LowerStr()
    value = Number(min_value=1, max_value=10)

    def __init__(self, name, value):
        self.name = name
        self.value = value


# ==== Проверка работы ====
node = Node("HeLLo", 5)
print(node.name)   # hello
print(node.value)  # 5

try:
    node = Node("test", 0)  # ❌ ValueError: Value 0 is less than 1
except ValueError as e:
    print("Ошибка:", e)

try:
    node = Node("test", 20)  # ❌ ValueError: Value 20 is greater than 10
except ValueError as e:
    print("Ошибка:", e)




