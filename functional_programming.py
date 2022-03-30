import time
import numpy as np
from dataset import example_data


def cache(f):
    cache._memo = {}

    def _wrap(*args):
        if args in cache._memo:
            return cache._memo[args]
        else:
            value = f(*args)
            cache._memo[args] = value
            return value

    return _wrap


def get_time(f):
    def _wrap(*args, **kwargs):
        begin = time.time()
        value = f(*args, **kwargs)
        end = time.time()
        print(f'{f.__name__} call with {args, kwargs} used time: {end - begin}')
        return value
    return _wrap


@get_time
@cache
def fib(n):
    return fib(n-1) + fib(n - 2) if n > 2 else 1


def factorial(n):
    return n * factorial(n-1) if n >= 1 else 1


def sum_range(n, m):
    return sum(list(range(n))) + sum(list(range(m)))


def _quit(): print('quit')
def go_on(): print('continue')
def break_down(): print('break down')


def person_action(function_mapping, action):
    for cmd, func in function_mapping.items():
        if action == cmd:
            func()
            break


@get_time
def add_first_row(matrix):
    for i, row in enumerate(matrix):
        first = row[0]
        for j, c in enumerate(row):
            matrix[i][j] = c + first

    return matrix


@get_time
def add_with_broadcast(matrix):
    return matrix + matrix[:, 0]


if __name__ == '__main__':
    # print(fib(15))
    # print(sum_range(5, 10))

    M = np.random.random(size=(1000, 1000))

    #add_first_row(M)
    #add_with_broadcast(M)
