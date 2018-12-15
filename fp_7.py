from collections import defaultdict
from collections import Counter


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




























