from functools import wraps


def greet(func):

    @wraps(func)
    def wrapped():
        print("Hello")
        func()
        
    return wrapped

@greet
def my_func():

    print("Hi let's play tennis!!!!!!!!")


my_func()
























