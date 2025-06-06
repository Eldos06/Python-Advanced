from functools import wraps


def hello(func):

    @wraps(func)
    def wrapped():
        print(f"Hello {func()}")
        
    return wrapped

@hello
def name():
    
    return ("Yeldos")

name()

#############################################
# class Hel:
#     def __init__(self, *a, **kw):
#         self.a = a
#         self.kw = kw

#     def display(self):
#         name = self.a[0] 

#         print(f"Hello {name}")

# user1 = Hel("Yeldos")

# user1.display()


