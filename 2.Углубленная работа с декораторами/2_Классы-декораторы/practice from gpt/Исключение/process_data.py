def process_data(data: dict):
    if "a" not in data or "b" not in data:
        raise KeyError("Key 'a' or 'b' not found")
    
    a = data["a"]
    b = data["b"]

    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b


# Тестируем
test_cases = [
    {"a": 10, "b": 2},     # ✅ OK
    {"a": 10, "b": 0},     # ❌ ZeroDivisionError
    {"a": "x", "b": 2},    # ❌ ValueError
    {"x": 1, "y": 2},      # ❌ KeyError
]

for i, case in enumerate(test_cases, 1):
    try:
        result = process_data(case)
        print(f"Test {i}: Result = {result}")
    except Exception as e:
        print(f"Test {i}: {type(e).__name__} - {e}")
