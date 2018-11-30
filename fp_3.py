from collections import defaultdict

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