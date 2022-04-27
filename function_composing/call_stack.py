"""
func_a = decorate(func_a)

==>

@decorator
def func_a():
    pass
"""

from functools import wraps


def is_called(func):
    def __wrap(*args, **kwargs):
        print(f'{func.__name__} was called')
        return func(*args, **kwargs)
    return __wrap


@is_called
def func_b():
    pass


def func_c():
    pass


def func_a(n):
    if n == 0:
        return func_b()
    else:
        return func_c()

func_b()