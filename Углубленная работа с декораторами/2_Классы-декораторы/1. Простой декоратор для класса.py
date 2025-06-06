# Задание 1: Декоратор класса для добавления атрибута
# Создай декоратор add_description, который добавляет в любой класс атрибут description со значением "This is a class".

# Контекст:

# Ты должен использовать декоратор, который добавляет атрибут description всем классам, которые он украшает.

##############################################################################

def add_description(cls):  # Функция-декоратор
    cls.description = "This is a class"  # Добавляем атрибут
    return cls  # Возвращаем класс обратно

@add_description  # Применяем декоратор
class MyClass:
    id = int
    name = str


print(MyClass.description)  
