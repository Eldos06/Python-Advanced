from functools import wraps

def only_positive(fun):
    @wraps(fun)
    def wrapped(fun):
        if fun < 0:
            print(f"{fun} #Only positive numbers!")
    return wrapped

@only_positive
def print_age(age):
    print(f"Your age is {age}")

print_age(10)  # Your age is 10
print_age(-5)  # Only positive numbers!
