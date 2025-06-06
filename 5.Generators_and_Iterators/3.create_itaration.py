

from typing import Iterator
from itertools import count, cycle, repeat



class Range():
    def __init__(self, start, stop = None, step = 1):
        if stop is None:
            stop = start
            start = 0

        self.start = start 
        self.stop = stop
        self.step = step

        self._current = self.start


    def __iter__(self):
        self._current = self.start
        return self  # <- вот этот объект и будет дергаться потом в forAnd. Between self but you also see the stores that. Next. Karachi courageous help with this show, be it possible business in terms of. Shows up front. What the hell? We stood beside the ratio, a big torsion. Image method detail self method next. On the. Stop iteration. You mean it method? Who says social? Did I stop iteration, stop iteration, stop iteration? Return to Joshua. Customer UK Local. Switch to. Show. Send a. You should. 
    
    def __next__(self):
        if self._current < self.stop:
            current = self._current
            self._current += self.step
            return current
        raise StopIteration #StopIteration — это способ сказать Python'у: "Братан, всё, элементов больше нет. Цикл for может идти нахуй"
        

# for i in Range(10):
#     print(i)

    


    

r = Range(10)

# for i in r:
#     print(i)
# print()
# for i in r:
#     print(i)


class Range:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0

        self.start = start
        self.stop = stop
        self.step = step

        self._current = self.start

    def __iter__(self):
        self._current = self.start
        return self

    def __next__(self):
        if self._current < self.stop:
            current = self._current
            self._current += self.step
            return current

        raise StopIteration



# for i in Range(1, 10, 2):
#     print(i)


class fibIter(Iterator):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib


# for f in fibIter():
#     print(f)
#     if f >= 100:
#         break

# for fib, pos in zip(fibIter(), Range(13)):
#     print(pos, fib) 


class Count(Iterator):
    def __init__(self):
        self._count = 0

    def __next__(self):
        c = self._count
        self._count += 1
        return c
    
class Count(Iterator):
    def __init__(self, start= 0):
        self._count = start

    def __next__(self):
        c = self._count
        self._count += 1
        return c
    
# for c, num in zip(Count(), Range(3, 17, 3)):
#     print(f"{c} -- {num}")

class Cycle(Iterator):
    def __init__(self, sequence):
        self._sequence = sequence
        self._step = 0

    def __next__(self):
        if self._step >= len(self._sequence):
            self._step = 0
        elem = self._sequence[self._step]
        self._step += 1
        return elem
    

class CycleN(Iterator):
    def __init__(self, sequence, repeat):
        self._sequence = sequence
        self._repeat = repeat
        self._step = 0
        self._cycles_done = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cycles_done >= self._repeat:
            raise StopIteration

        elem = self._sequence[self._step]
        self._step += 1

        if self._step >= len(self._sequence):
            self._step = 0
            self._cycles_done += 1

        return elem


c = CycleN([1, 2, 3], repeat=2)

for i in c:
    print(i)



# for i, elem in zip(Range(7), Cycle([7, 9, 11])):
#     print(i, elem)


# print()

# for i, elem in zip(range(7), cycle([7, 9, 11])):
#     print(f"{i} -- {elem}")













