import random
from collections import defaultdict
from collections import Counter
from operator import itemgetter


class Average:

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Average()

print(avg(4))
print(avg(5))
print(avg(9))

###############################################################


def make_average():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


favg = make_average()

print(favg(4))
print(favg(5))
print(favg(9))

###############################################################


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = defaultdict(list)

for k, v in s:
    d[k].append(v)

print(type(d))
print(d)
print('Itemgetter: ', sorted(s, key=itemgetter(0)))


s = 'mississippi'

d = defaultdict(int)
for k in s:
    d[k] += 1

print(d.items())


#################################################################

s = 'abracadabra'

ct = Counter(s)

print(ct.items())

ct.update('aaaabbbaaa')

print(ct)


##############################################################


class Bingo:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def __iter__(self):
        # pass
        return iter(self._items)

    def __getitem__(self, item):
        pass
        # return self._items

    def pick(self):
        try:
            self._items.pop()
        except IndexError:
            raise LookupError

    def __call__(self):
        return self.pick()


bingo = Bingo(range(20))

print(bingo)

alist = []
for k in bingo:
    alist.append(k)

print(alist)

#############################################################################















