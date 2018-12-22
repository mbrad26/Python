import re
import reprlib
import operator
from contextlib import contextmanager
from functools import lru_cache
from collections import defaultdict


@contextmanager
def looking_glass():
    import sys
    original = sys.stdout.write

    def reverse_write(text):
        original(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original


################################################################

registry = []


def register(func):
    print('Running register {}'.format(func))
    registry.append(func)
    return func


@register
def f1():
    print('Running f1()')


@register
def f2():
    print('Running f2()')


def f3():
    print('Running f3()')


def main():
    print('Running main()')
    print('Registry: ', registry)
    f1()
    f2()
    f3()


main()

##############################################################


@lru_cache()
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


print(fib(250))


#########################################

text = 'kshd ckacajhc aljhclah lkchlac ahcalh alkjskljkja lskjja;kdjak; djdiajd ja;ja;jdj aslj;as5ajab s jlanca ca ' \
       'kjsac45as'

RE_WORDS = re.compile('\w+')

words = RE_WORDS.findall(text)

print(words)
print(reprlib.repr(text))


##############################################


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = defaultdict(list)
print(d)
for k, v in s:
    d[k] = v

print(d)


###############################################################


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

print(sorted(metro_data, key=operator.itemgetter(1)))














