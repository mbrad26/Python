import functools
from datetime import datetime
import time


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)

print(say_whee())


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper


def say_whee():
    print("Whee!")


say_whee = not_during_the_night(say_whee)

print(say_whee())


def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


@do_twice
def say_whee():
    print('Whee!')


print(say_whee())


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice()


# Timing Functions

def timer(func):

    @functools.wraps(func)
    def wraper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        print(f'Finished {func.__name__} in {run_time:.4f} secs.')
        return value

    return wraper


@timer
def sum_sqr(num):
    for i in range(num):
        sum([x**2 for x in range(10000)])


print(sum_sqr(999))


# Debugging code

def debugging(func):

    @functools.wraps(func)
    def wraper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})...')
        value = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {value!r}')
        return value
    return wraper


@debugging
def greeting(name, age=None):
    if age is None:
        return f'Howdy {name}!'
    else:
        return f'Howdy {name}! {age} already, you are growing up!'


greeting('Bob')
greeting('Taylor', 18)


# Slowing down code

def slow_down(func):

    @functools.wraps(func)
    def wraper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wraper


@slow_down
def countdown(from_num):
    if from_num < 1:
        print('Liftoff!')
    else:
        print(from_num)
        countdown(from_num - 1)


countdown(10)

























