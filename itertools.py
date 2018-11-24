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