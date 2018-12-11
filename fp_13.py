import math
import itertools


class Vector:

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            return Vector(a + b for a, b in itertools.zip_longest(self, other, fillvalue=0))
        except TypeError:
            raise NotImplemented

    def __radd__(self, other):
        return self + other

