from functools import wraps
from multiprocessing import Pool
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Caching decorator
def cached(func):
    results = {}
    @wraps(func)
    def wrapped(n):
        if n not in results:
            results[n] = func(n)
        return results[n]
    return wrapped

# Trace decorator
def trace(_func=None, *, sep="="):
    
    def decorator(func):
        func.calls = 0

        @wraps(func)
        def wrapper(*a, **kw):
            func.calls += 1
            print(sep * func.calls, f"-> {func.__name__}(*{a}, **{kw})")
            try:
                return func(*a, **kw)
            finally:
                print(sep * func.calls, f"<- {func.__name__}(*{a}, **{kw})")
                func.calls -= 1

        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)

# Fibonacci function with decorators
@cached
@trace(sep="~")
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# Function for multiprocessing
def multiprocessing_fib(numbers):
    logger.info("Started multiprocessing...")
    with Pool() as pool:
        results = pool.map(fib, numbers)
    return results


if __name__ == "__main__":

    a = int(input("Enter a number ~~> "))
    numbers = list(range(a))

    result = multiprocessing_fib(numbers)
    print("Fibonacci results:", result)
