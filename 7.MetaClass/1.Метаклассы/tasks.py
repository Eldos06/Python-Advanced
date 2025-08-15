# Отслеживание создания объектов
# Создай класс Tracker, который в __new__ будет увеличивать счётчик, сколько экземпляров уже создано, и выводить это число.

# class Tracker:
#   _count = 0

#   def __new__(cls,):
#     cls._count += 1
#     print(f"Создан экземпляр {cls.__name__}, всего создано: {cls._count}")
#     return super().__new__(cls)

# tr = Tracker()
# dk = Tracker()

# print(tr)
# print(dk)

# Автоматический full_name
# Сделай класс Person, у которого при создании экземпляра через __new__ автоматически формируется атрибут full_name из first_name и last_name.


# class Person:
#     def __new__(cls, first_name, last_name):
#         cls = super().__new__(cls)
#         cls.full_name = f"{first_name} {last_name}"
#         return cls.full_name

# enter_FN = Person("Yeldos", "Suleimen")

# print(enter_FN)

# Автоматический snake_case для атрибутов
# Напиши метакласс, который все атрибуты класса в CamelCase будет переименовывать в snake_case.

# Класс с запретом изменения атрибута
# Создай класс Config, который при создании объекта не позволит изменить уже установленные атрибуты.


