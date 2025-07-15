
from decimal import Decimal


def multi_div(iterations, number, divisor):
    number = Decimal(number)
    for i in range(iterations):
        number /= divisor
    
    return number

print(multi_div(6, 123456, 10))