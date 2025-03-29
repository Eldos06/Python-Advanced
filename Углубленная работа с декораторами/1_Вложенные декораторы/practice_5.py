from functools import wraps

def count_calls(fun):
    count = 0  # Счётчик вызовов
    @wraps(fun)
    def wrapped(*args, **kwargs):
        nonlocal count  # Счётчик должен сохраняться
        count += 1
        print(f"{fun(*args, **kwargs)} ({count})")  # Вызов функции и вывод
    return wrapped

@count_calls
def say_hi():
    return "Hi!"

say_hi()
say_hi()
say_hi()

