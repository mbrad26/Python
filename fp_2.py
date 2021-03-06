from array import array
from collections import namedtuple
from random import random
from collections import deque


symbols = '£$"&^%*()_+'

codes = [ord(char) for char in symbols]
print(codes)
print(list(symbols))

# as opposed to less readable map and filter
print(list(filter(lambda x: x > 40, map(ord, symbols))))

###############################################################

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

t_shirts = [(color, size) for color in colors
                            for size in sizes]

print(t_shirts)

t_shirts = [(color, size) for size in sizes for color in colors]

print(t_shirts)

##############################################################

codes = (ord(char) for char in symbols)

for x in codes:
    print(x)

print(array('I', codes))

#####################################################################

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
for city, county, pop, (lat, long) in metro_areas:
    print('{:15} | {:9.4f} | {:9.4f}'.format(city, lat, long))

#############################################################################

City = namedtuple('Tokyo', 'city country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(City._fields)
delhi_data = ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
delhi = City._make(delhi_data)
delhi._asdict()
print(delhi._asdict())

########################################################################

board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)


weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = 'X'
print(weird_board)


board1 = []
row = ['_']

for i in range(3):
    board1.append(row)
print(board)
# board1[1][2] = 'X'
# print(board1)
###################################################

alist = [1, 2, 3]

alist += [3]
print(alist)
print(id(alist))

atuple = 1, 2, 3,

print(atuple)
print(id(atuple))

atuple += 5,
print(atuple)
print(id(atuple))


########################################################

floats = array('d', (random() for i in range(10**7)))

print('Double_precision float: ', floats[192828])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats_2 = array('d')
fp = open('floats.bin', 'rb')
floats_2.fromfile(fp, 10**7)
fp.close()

print(floats[-1])

################################################################























