import collections
import random
from math import hypot

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


card = FrenchDeck()

print(len(card))
print(card[23])
# a = [next(iter(card)) for _ in range(1, len(card) + 1)]
# print(a)
# print(list(card))
print(random.choice(card))

################################################################################################


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __bool__(self):
        return bool(abs(self))

    def __abs__(self):
        return hypot(self.x, self.y)

    def __repr__(self):
        # return 'Vector({}, {})'.format(self.x, self.y)
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        return f'Vector({self.x + other.x}, {self.y + other.y})'

    def __mul__(self, scalar):
        return f'Vector({self.x * scalar}, {self.y * scalar})'


v1 = Vector(2, 3)
v2 = Vector(4, 5)
s = 7

print(v1 + v2)
print(v1 * s)
print(repr(v1))
print(abs(v2))


#########################################################
person = {'name': 'Eric', 'age': 74, 'married': 'Mary'}
print("Hello, {name}. You are {age} and married to {married}.".format(**person))




























