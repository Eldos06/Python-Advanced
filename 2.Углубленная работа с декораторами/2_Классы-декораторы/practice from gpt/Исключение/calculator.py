
# def safe_divide(a, b):
#     try:
#         if b == 0:
#             return "Cannot divide by zero"
#     except ValueError:
#         pass
#     else:
#         return a / b

# while True:
#     print(safe_divide(int(input('a: ')), int(input('b: '))))

def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

while True:
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        print(safe_divide(a, b))
    except ValueError as e:
        print("Error:", e)
