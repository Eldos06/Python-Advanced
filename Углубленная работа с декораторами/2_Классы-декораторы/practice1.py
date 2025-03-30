# Измени код
# def add_new_method(class_to_decorate):
#     class DecoratedClass(class_to_decorate):
#         def new_method(self):
#             return "A"
#     return DecoratedClass
 
# @add_new_method
# class MyClass:
#     def my_method(self):
#         return "B"
 
# my_object = MyClass()
# print(my_object.my_method())  # вывод: This is my method
# print(my_object.new_method())  # вывод: This is a new method


def add_new_method(class_to_decorate):
    class DecoratedClass(class_to_decorate):
        def power(self, a, b):
            self.a = a
            self.b = b
            return f"power: {a ** b}"
    return DecoratedClass

@add_new_method
class MyClass:
    def multi(self, a , b):
        self.a = a
        self.b = b
        return f"multipli is {a * b}"
  
numbers = MyClass()

print(numbers.power(2, 3))
print(numbers.multi(2,3))
