class ReverseRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            # Если один аргумент — считаем, что start это stop
            self.start = start
            self.stop = 0
        else:
            self.start = start
            self.stop = stop
        self.step = step
        self._current = self.start - 1

    def __iter__(self):
        self._current = self.start - 1
        return self

    def __next__(self):
        if self._current >= self.stop:
            current = self._current
            self._current -= self.step
            return current
        else:
            raise StopIteration


# Пример использования
# for i in ReverseRange(5):
#     print(i)





# class EvenNumbers:
#     def __init__(self, stop, step=2):
#         self.start = 0
#         self.stop = stop
#         self.step = step
#         self._current = self.start

#     def __iter__(self):
#         self._current = self.start
#         return self

#     def __next__(self):
#         if self._current < self.stop:
#             current = self._current
#             self._current += self.step
#             return current
#         else:
#             raise StopIteration

# # ВНИМАНИЕ СУКА: тут всё ОК!
# for i in EvenNumbers(10):
#     print(i)
# class AlphabetCycle:
#     def __init__(self):
#         self.alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         letter = self.alphabet[self.index]
#         self.index = (self.index + 1) % len(self.alphabet)  # Зацикливаем
#         return letter
    
# ac = AlphabetCycle()
# for _ in range(30):  # выведет 30 букв, зацикливаясь
#     print(next(ac), end=' ')


class SkipIterator:
    def __init__(self, lst:list, n):
        self.lst = lst
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.lst[::self.n]
        
    
lst = [10, 20, 30, 40, 50, 60]
n = 2

# for i in SkipIterator(lst, n):
#     print(i)
#     break

class Squares :
    def __init__(self, n: int):
        self.n = n + 1
        self._current = 1  

    def __iter__(self):
        return self

    def __next__(self):
        if self._current >= self.n: # если выходим за список — стоп
            raise StopIteration
        num = self._current ** 2
        self._current += 1
        return num


# for i in Squares(5):
#     print(i)

# Recursive approach
# def fib_recursive(n):
#     if n <= 1:
#         return n
#     else:
#         return fib_recursive(n-1) + fib_recursive(n-2)

# # Iterative approach
# def fib_iterative(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# Generator approach
def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

class fibG:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.i += 1
        return value


class countZero:
    def __init__(self, start):
        self.start = start
        self.count = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count == self.start:
            raise StopIteration
        _count = self.count
        _count += 1
        current = self.start
        current -= 1
        return _count
    
for i in countZero(5):
    print(i)






    



