class PrimeIterator:
    def __init__(self, start=2, end=None):
        self.current = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if self.end is not None and self.current > self.end:
                raise StopIteration
            if self.is_prime(self.current):
                prime = self.current
                self.current += 1
                return prime
            self.current += 1

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


start = int(input("start: "))
end = int(input("end: "))
primes = PrimeIterator(start, end)

for prime in primes:
    print(prime)