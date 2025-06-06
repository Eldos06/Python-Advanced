import math

def compute_sqrt_division(data: dict):
    if "a" not in data or "b" not in data:
        raise KeyError("Key 'a' or 'b' not found")

    a = data["a"]
    b = data["b"]

    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    result = a / b

    if result < 0:
        raise ValueError("Result is negative. Cannot compute square root.")

    return math.sqrt(result)


# Тесты
test_cases = [
    {"a": 16, "b": 4},   
    {"a": 16, "b": 0},     
    {"a": "x", "b": 2},  
    {"a": 4, "b": -2},
    {"x": 1, "y": 2}     
]

for i, case in enumerate(test_cases, 1):
    try:
        result = compute_sqrt_division(case)
        print(f"Test {i}: Result = {result}")
    except Exception as e:
        print(f"Test {i}: {type(e).__name__} - {e}")
