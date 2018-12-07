import reprlib
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