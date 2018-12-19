from contextlib import contextmanager


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



























