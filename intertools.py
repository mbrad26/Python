from _datetime import datetime


def better(input, n):
    itr = [iter(input)] * n
    return [item for item in zip(*itr)]


start = datetime.now()
for _ in better(range(100000000), 10):
    pass
print(datetime.now() - start)



