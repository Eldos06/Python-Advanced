from collections.abc import Iterator


# class PrimeIterator:
#     def __init__(self, start=2, end=None):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while True:
#             if self.end is not None and self.current > self.end:
#                 raise StopIteration
#             if self.is_prime(self.current):
#                 prime = self.current
#                 self.current += 1
#                 return prime
#             self.current += 1

#     @staticmethod
#     def is_prime(n):
#         if n < 2:
#             return False
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True


# # Пример использования
# start = int(input("start: "))
# end = int(input("end: "))
# primes = PrimeIterator(start, end)

# for prime in primes:
#     print(prime)


# Итерируемый стек
# Реализуйте свой тип Стек, поддержите следующие методы:

# push - добавить новый элемент наверх;
# pop - удалить и вернуть верхний элемент. Выкинуть исключение, если значений больше нет;
# peek - вернуть верхний элемент, не удалять из стека. Выкинуть исключение, если значений больше нет;
# При инициализации стека должна быть возможность указать стартовые значения в виде коллекции в порядке от нижнего к верхнему.

# Добавьте в Стек возможность пройти по структуре в цикле. На первой итерации должно вернуться верхнее значение, на второй следующее, и так далее.

# Если в стек были добавлены значения 3, 5, 7 методом push, при проходе по объекту в цикле значения должны вернуться в следующем порядке: 7, 5, 3
class Stack:
    def __init__(self, iterable=None):
        self.items = list(iterable) if iterable else []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def __iter__(self):
        return reversed(self.items)  # верхний элемент первый




# s = Stack([1, 2, 3])  # 1 — низ, 3 — верх
# s.push(5)
# s.push(7)

# print("🔁 Перебор стека:")
# for item in s:
#     print(item)  # 7, 5, 3, 2, 1

# print("👀 peek:", s.peek())  # 7
# print("📤 pop:", s.pop())    # 7
# print("📤 pop:", s.pop())    # 5

# print("♻ Осталось в стеке:")
# for item in s:
#     print(item)  # 3, 2, 1

class PrimeIterator(Iterator):
    def __init__(self, start: int = 2, end: int | None = None) -> None:
        self.current = start
        self.end = end

    @classmethod
    def is_prime(cls,  num: int) -> bool:
        if num < 2:
            return False
        for val in range(2, int(num**0.5) + 1):
            if num % val == 0:
                return False
        return True
    
    def __next__(self) -> int:
        while self.current != self.end:
            if self.is_prime(self.current):
                prime_number = self.current
                self.current += 1
                return prime_number
            self.current += 1
        raise StopIteration
    
def main() -> None:
    for idx, prime in zip(range(1, 17), PrimeIterator()):
        print(f"prime {idx}: {prime}")

    print()

    for idx, prime in enumerate(PrimeIterator(end=100), start=1):
        print(f"prime: {idx:2d}: {prime}")
    
    print()

    for prime in PrimeIterator(start = 20, end = 100):
        PRINT)PRIMR

















