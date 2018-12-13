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
