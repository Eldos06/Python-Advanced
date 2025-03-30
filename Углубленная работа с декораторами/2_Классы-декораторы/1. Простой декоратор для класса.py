# 1. Простой декоратор для класса:
# Создай декоратор add_class_name, который добавляет атрибут class_name в любой класс.

# python

# def add_class_name(cls):
#     cls.class_name = cls.__name__
#     return cls

# @add_class_name
# class Example:
#     pass

# print(Example.class_name)  # Должно вывести 'Example'

##############################################################################

def add_description(cls):  # Функция-декоратор
    cls.description = "This is a class"  # Добавляем атрибут
    return cls  # Возвращаем класс обратно

@add_description  # Применяем декоратор
class MyClass:
    id = int
    name = str

# Проверяем атрибут
print(MyClass.description)  # Должно вывести: This is a class
