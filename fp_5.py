import random
import operator
from functools import reduce
from functools import partial

asum = lambda x, y: x + y
print(callable(asum))

print(asum(3, 4))

###########################################################


class Bingo:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty Bingo Class')

    def __call__(self):
        return self.pick()


b = Bingo(range(5))
print(f'Is it callable: {callable(b)}')
print(b.pick())
print(b())

###############################################################


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


print(fact(35))

#################################################################


def factorial(n):
    return reduce(operator.mul, range(1, n + 1))


print(factorial(20))

n = 20
alist = []
for i in range(1, n + 1):
    alist.append(factorial(i))

print(alist)

##################################################################


triple = partial(operator.mul, 5)

print(triple.func)
print(triple(3))

print(list(map(triple, range(1, 15))))
print(list(map(lambda x: 5 * x, range(1, 15))))


































