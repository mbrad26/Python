from collections import defaultdict
from collections import Counter
from collections import UserDict

d = {'a': 3, 'c': 4, 'g': 9, 'y': 3}

print(d.get('x'))

d.setdefault('x', []).append(443)
print(d)

###################################################

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

dd = defaultdict(list)

for k, v in s:
    dd[k].append(v)

print(dd.items())

#####################################################################

s = 'mississippi'

dd = defaultdict(int)

for k in s:
    dd[k] += 1

print(dd.items())

#######################################################################

s = 'abracadabrajdudsb'

ct = Counter(s)

print(ct)

ct.update('oiwpqdncncpjcq qjoqqwojd')

print(ct)

###########################################################################

class str_key(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return key in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

































