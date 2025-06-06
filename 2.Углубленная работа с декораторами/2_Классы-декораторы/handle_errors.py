import functools

def handle_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, ZeroDivisionError, KeyError) as e:
            print(f"[{type(e).__name__}] - {e}")
        except Exception as e:
            print(f"[UNEXPECTED ERROR] - {type(e).__name__}: {e}")
    return wrapper
