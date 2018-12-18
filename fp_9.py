import reprlib
import collections
import numbers
from array import array


class Vector2d:

        def __init__(self, x, y):
            self._x = float(x)
            self._y = float(y)

        @property
        def x(self):
            return self._x

        @property
        def y(self):
            return self._y

        def __iter__(self):
            return (i for i in (self._x, self._y))

        def __eq__(self, other):
            return tuple(self) == tuple(other)

        def __hash__(self):
            return hash(self._x) ^ hash(self._y)


vector = Vector2d(3, 4)
vector1 = Vector2d(4, 5)

print(hash(vector))
print(vector == vector1)

#######################################################################


class Vector3d:

    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector {}'.format(components)


vector = Vector3d([3, 4])
vector1 = Vector3d([4, 3])

# print(hash(vector))
print(vector == vector1)

###############################################################################


class DopperDict(dict):

    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = DopperDict(one=1)
print(dd)

dd['two'] = 2
print(dd)

dd.update(three=3)
print(dd)

###########################################################################


class DoppelDict2(collections.UserDict):

    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd2 = DoppelDict2(one=1)
print(dd2)

dd2['two'] = 2
print(dd2)

dd2.update(three=3)
print(dd2)


#########################################################################

class Vector2d:

    typecode = 'd'

    def __init__(self, *components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        if isinstance(item, numbers.Integral):
            return self._components[item]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))


vector = Vector2d(3, 4, 2, 7)

print(vector)
print(len(vector))
print(vector[:1])
























