# list generator
L = ['Hello', 'World', 18, 'Apple', None]
g = (s.lower() for s in L if isinstance(s, str))
print(next(g), next(g), next(g))


# The Fibonacci sequence
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


def gfib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'Is Over'


g = gfib(4)
print(next(g), next(g), next(g), next(g))

# 直接作用于for循环的对象统称为可迭代对象：Iterable

from collections.abc import Iterable

isinstance(range(12), Iterable)

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
from collections.abc import Iterator

print(isinstance((x for x in range(10)), Iterator))

print(isinstance([1, 2, 3], Iterator))
print(isinstance([1, 2, 3], Iterable))

print(isinstance(iter([1, 2, 3]), Iterator))

