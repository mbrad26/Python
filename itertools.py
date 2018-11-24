import itertools as it
from _datetime import datetime


def better(inputs, n):
    itr = [iter(inputs)] * n
    return [item for item in zip(*itr)]


start = datetime.now()
for _ in better(range(10000), 10):
    pass
print(datetime.now() - start)

##################################################

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def grouper(nums, n):
    iters = [iter(nums)] * n
    return zip(*iters)


print(list(grouper(nums, 2)))
print(list(grouper(nums, 3)))


def grouper_longest(nums, n):
    iters = [iter(nums)] * n
    return list(it.zip_longest(*iters))


print(grouper_longest(nums, 2))
print(grouper_longest(nums, 3))
print(grouper_longest(nums, 4))

######################################################

# You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, and five $1 dollar bills. How many ways
# can you make change for a $100 dollar bill?

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

results = []

for n in range(1, len(bills) + 1):
    for combination in it.combinations(bills, n):
        if sum(combination) == 100:
            results.append(combination)

print(len(set(results)))


# How many ways are there to make change for a $100 bill using any number of $50, $20, $10, $5, and $1 dollar bills?

# bills = [50, 20, 10, 5, 1]
# results = []
#
# for n in range(1, 101):
#     for combination in it.combinations_with_replacement(bills, n):
#         if sum(combination) == 100:
#             results.append(combination)
#
# print(len(results))  # 96,560,645 combinations!


#########################################################

# Evens and odds using generators

def evens():
    n = 0
    while True:
        yield n
        n += 2


even = evens()
print(next(even))
print(next(even))


def odds():
    n = 1
    while True:
        yield n
        n += 2


odd = odds()
print(next(odd))
print(next(odd))


# Evens and odds using it.count()

evens = it.count(step=2)

a = [next(evens) for _ in range(20)]
print(a)

##########################################################

# The Fibonacci sequence


def fibs():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibs()

a = [next(fib) for _ in range(100)]
print(a)


















































