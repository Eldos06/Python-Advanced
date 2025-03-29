import time
from functools import wraps

def measure_time(fun):
    @wraps(fun)
    def wrapped():
        tic = time.perf_counter()
        fun()
        toc = time.perf_counter()
        print(f"whole time to run is {toc - tic:0.4f} seconds")
    return wrapped

@measure_time
def slow_func():
    time.sleep(1)
    print("Done!")

slow_func()
