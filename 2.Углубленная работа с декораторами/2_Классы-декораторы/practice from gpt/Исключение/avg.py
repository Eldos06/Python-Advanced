def get_average(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    return (a + b) / 2

while True:
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        print(get_average(a, b))
    except ValueError as e:
        print("Error:", e)
