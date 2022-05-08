from icecream import ic
from functools import wraps
from collections import defaultdict


def stringify(obj):
    if callable(obj):
        return obj.__name__
    else:
        return repr(obj)


def _show_called(func):
    _show_called.level = 0
    _show_called.stack = defaultdict(list)

    @wraps(func)
    def _wrap(*args):

        try:
            _show_called.level += 1
            result = func(*args)
            dash = '-' * _show_called.level
            notation = f'{func.__name__}{" ".join(map(stringify, args))} '
            print(f'{dash} {notation} was called')
            _show_called.stack[func.__name__].append((_show_called.level, notation))

        finally:
            _show_called.level -= 1

        return result

    return _wrap

show_called = _show_called

# def show_called(func):
#     show_called.depth = defaultdict(int)
#
#     @wraps(func)
#     def _warp(*args, **kwargs):
#         show_called.depth[func] += 1
#         dash = '-'*show_called.depth[func]
#         print(f'{dash} {func.__name__} ({args, kwargs}) was called')
#         return func(*args, **kwargs)
#     return _warp



@_show_called
def fib(n):
    if n > 2: return fib(n - 1) + fib(n - 2)
    else:
        return 1

@show_called
def is_number(n):
    return isinstance(n, (float, int))


@show_called
def only_numbers(elements):
    return is_number(elements) or (list not in set(type(e) for e in elements))


@show_called
def both_empty(test1, test2):
    return len(test1) == len(test2) == 0


@show_called
def same_count_numbers(test1, test2):
    return same_lengths(test1, test2) and only_numbers(test1) and only_numbers(test2)


@show_called
def is_iter_same_len(test1, test2):
    return type(test1) == type(test2) == list and len(test1) == len(test2)


@show_called
def is_single_number(n1, n2):
    return is_number(n1) and is_number(n2)


@show_called
def same_lengths(test1, test2):
    if type(test1) == type(test2) == list:
        return len(test1) == len(test2)
    else:
        return False


@show_called
def any_satisfy(funcs):
    def _wrap(*args):
        return any(f(*args) for f in funcs)
    return _wrap


basic_true_satisfy = any_satisfy([is_single_number, both_empty, same_count_numbers])


@show_called
def struc_equal(list1, list2, basic_true):
    if basic_true(list1, list2): return True
    if not same_lengths(list1, list2): return False

    return struc_equal(list1[0], list2[0], basic_true) and struc_equal(list1[1:], list2[1:], basic_true)


@show_called
def _struc_equal_same_len_type(basic_true):
    def _wrap(list1, list2):
        return struc_equal(list1, list2, basic_true)
    return _wrap


struc_equal_same_len_type = _struc_equal_same_len_type(basic_true_satisfy)

assert is_number(9)
assert not is_number([9])
assert only_numbers([1, 2, 3])
assert not only_numbers([1, 2, [3]])
assert both_empty([], [])
assert not both_empty([], [1])
assert same_count_numbers([1, 2, 3], [4, 5, 6])
assert is_single_number(1, 2)
assert not is_single_number(1, [2])
assert is_iter_same_len([1, 2, 3], [4, 5, 5])
assert is_iter_same_len([[1], [2], 3], [[4], 5, 5])
assert not is_iter_same_len(1, 2)
print('utilities functions test done!')

assert struc_equal([1, 2, 3], [4, 5, 6], basic_true_satisfy)
assert not struc_equal([1, 2, 3], [4, 5, 6, 7], basic_true_satisfy)
assert struc_equal(1, 2, basic_true_satisfy)
assert struc_equal([1], [4], basic_true_satisfy)
assert struc_equal([[[1]]], [[[2]]], basic_true_satisfy)
assert struc_equal([[[1]], [[2]], [3], 4, [5]],
                   [[[-1]], [[-2]], [-3], -4, [-5]], basic_true_satisfy)
assert not struc_equal([[[1]], [[2]], [3], 4, [5]],
                       [1, [[-1]], [[-2]], [-3], -4, [-5]], basic_true_satisfy)

assert struc_equal_same_len_type([1, 2, 3], [4, 5, 6])
assert not struc_equal_same_len_type([1, 2, 3], [4, 5, 6, 7])
assert struc_equal_same_len_type(1, 2)
assert struc_equal_same_len_type([1], [4])
assert struc_equal_same_len_type([[[1]]], [[[2]]])
assert struc_equal_same_len_type([[[1]], [[2]], [3], 4, [5]],
                                 [[[-1]], [[-2]], [-3], -4, [-5]])
assert not struc_equal_same_len_type([[[1]], [[2]], [3], 4, [5]],
                                     [1, [[-1]], [[-2]], [-3], -4, [-5]])

print('test structure function done!')

"""
老师把这几个utility关系画一下吧
"""


def combine_stack(stack_info, func):
    stacks = stack_info[func]
    levels = [[] for _ in range(len(stacks))]

    for level, notation in stacks:
        levels[level].append(notation)

    levels = [level for level in levels if level]

    return levels


fib(10)
for func, values in _show_called.stack.items():
    print(func)
    for v in values:
        print(v)


levels = combine_stack(_show_called.stack, fib)
print(levels)