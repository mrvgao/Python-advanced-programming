import re
from collections import defaultdict
from icecream import ic
from functools import wraps
import copy


class Person:
    count = 0

    def __init__(self, _id):
        self._id = _id
        self.count += 1


def get_freq(text, count=None):
# def get_freq(text, count=0):
    count = count or defaultdict(int)
    for word in [w.lower() for w in re.findall('\w+', text)]:
        # freq[word] += 1
        count[word] +=1

    # return freq
    return count


def metric(fn):
    ncalls = [0]
    # ncalls = 0
    name = fn.__name__

    def wrapper(*arg, **kwargs):
        ncalls[0] += 1
        # nonlocal ncalls
        # global ncalls
        # ncalls += 1
        # wrapper.ncalls += 1
        # ic(f'{name} called {wrapper.ncalls} times')
        # ic(f'{name} called {wrapper.ncalls} times')
        ic(f'{name} called {ncalls[0]} times')

    # wrapper.ncalls = 0

    return wrapper


@metric
def inc(n):
    return n + 1

inc(10)


def add_n(items, n):
    items += range(n)
    return items


items = [0, 1]
new_item = add_n(items, 3)
new_item[-1] = -99
ic(items)


def func_small(n):
    m = 10
    return n + m


def func_complex(n):
    result = func_small(n)

    return result ** 2

# version-01

def new_small_func(n):
    if n > 5: n = 5
    m = 10
    return n + m


def change_small_func(func):
    def _wrap(n):
        if n > 0: n = 5
        r = func(n)
        return r
    return _wrap


def change_func_complex(func):
    def _wrap(*args, **kwargs):
        original = copy.copy(new_small_func)
        global func_small
        func_small = new_small_func
        r = func(*args, **kwargs)
        func_small = original
        return r
    return _wrap


ic(func_complex(100))

# func_complex = change_func_complex(func_complex)
func_complex = change_small_func(func_complex)
ic(func_complex(100))


if __name__ == '__main__':
    p = Person(1190)
    print(Person.count)
    print(p.count)


    display = []
    buttons = []

    for var in range(10):  # var
        print(id(var))
        # buttons.append(lambda var=var: display.append(id(var)))  # var -> address
        buttons.append(lambda: display.append(var))

    print(get_freq('鸭子 来了 鸭子！'))
    print(buttons)
    btn = buttons[3]
    btn()

    print(display)
    #
    another_btn = buttons[5]
    another_btn()

    print(display)

    ic(get_freq('兔子 来了 兔子 兔子 啊 兔子！'))

