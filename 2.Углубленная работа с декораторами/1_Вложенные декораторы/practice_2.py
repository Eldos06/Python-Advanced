from functools import wraps

def reap(func):
    wraps(func)
    def wrapped():
        func()
        func()
    return wrapped

@reap
def main():
    print("Hello Yeldos")

main()