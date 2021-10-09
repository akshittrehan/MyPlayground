import timeit
from collections import defaultdict

memo = defaultdict(int)  # int -> int mapping


def fib(n):
    if n < 0:
        return 0
    fib_store = [1] * (n+1)

    for i in range(2, n+1, 1):
        fib_store[i] = fib_store[i-1] + fib_store[i-2]
    return fib_store[n]


def main():
    n = 100
    print(fib(n))


t = timeit.timeit(main, number=1)
print(t)
