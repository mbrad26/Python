def my_gen():

    n = 1
    print('This is printed first.')
    yield n

    n += 1
    print('This is printed second.')
    yield n

    n += 1
    print('This is printed last.')
    yield n


a = my_gen()
print(next(a))
print(next(a))
print(next(a))
# print(next(a))

for item in my_gen():
    print(item)


# Generators with a Loop

def rev_str(str):
    length = len(str)
    for i in range(length - 1, -1, -1):
        yield str[i]


for char in rev_str('Hello World!'):
    print(char)


# Generator Expression

alist = list(range(10))

a = [x**2 for x in alist]
print(a)
b = (x**2 for x in alist)
print(b)

print(next(b))
print(next(b))

for item in b:
    print(item)

# print(next(b))