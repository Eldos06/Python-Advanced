# # class decorators
# # классы-декораторы
# # декораторы классов

# from dataclasses import dataclass

# @dataclass(slots=True)
# class User:
#     id: int
#     userName: str

# user = User(id=1,userName="Yeldos2")

# print(user)
# print(User.__slots__)
# print(User.mro())
# print(User.__dataclass_params__)
# print(repr(user))

# registry = {}

# def register_model(cls):
#     registry[cls.__name__] = cls
#     cls.__models_registry__ = registry
#     return cls

# print(registry)

# @register_model
# class Post:
#     pass

# print(registry)

# @register_model
# class Comment:
#     pass

# print(Comment.__models_registry__)

# print(Post.__models_registry__)

# class ModelsRegistry:
#     def __init__(self):
#         self._registry = {}

#     def register(self, decorated_class):
#         self._registry[decorated_class.__name__] = decorated_class
#         decorated_class.__models_registry__ = self._registry
#         return decorated_class
    

# models_registry = ModelsRegistry()

# print(models_registry._registry)

# @models_registry.register
# class Client():
#     pass

# print(models_registry._registry)


# @models_registry.register
# class Manager():
#     pass

# print(Manager.__models_registry__)
# print(models_registry._registry)

# class Cached:
#     def __init__(self, func):
#         self.func = func
#         self._cache = {}

#     def __call__(self, *args):
#         if args not in self._cache:
#             self._cache[args] = self.func(*args)

#         return self._cache[args]
    

# @Cached
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)


# print(fib)
# print(fib._cache)
# fib(3)
# print(fib._cache)

# from functools import wraps

# class History:
#     def __init__(self, total_items=2):
#         self.total_items = total_items
#         self.results_history = []
#         self.func = None

#     def add_history_item(self, result):
#         self.results_history.append(result)  # Corrected this line
#         if len(self.results_history) > self.total_items:
#             self.results_history.pop(0)

#     def wrap(self, func):
#         self.func = func
#         func.history = self  # Attach the history to the function

#         @wraps(func)
#         def wrapper(*a, **kw):
#             result = self.func(*a, **kw)
#             self.add_history_item(result)
#             return result
        
#         return wrapper

#     def __call__(self, func):
#         return self.wrap(func)


# @History(3)
# def power(a, e):
#     return a ** e

# # Testing the function and its history
# print(power)  # This will show the wrapped function, not the result
# power(2, 3)
# print(power.history)  # Shows the history object
# print(power.history.results_history)  # Shows the history results
# power(3, 2)
# power(3, 5)
# power(2, 6)
# print(power.history.total_items)  # Total items to keep in history
# print(power.history.results_history)  # Shows the history of last 3 results

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
