"""
Some useful function tools.

Speed up the dev process.
"""

from functools import reduce
import operator as op
from functools import cache
from functools import lru_cache
from functools import cached_property


#Task - 01 Merge lists


# @cache
@lru_cache(maxsize=2**10)
def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 2 else 1


class Dataset:
    def __init__(self):
        pass

    @cached_property
    def get_obj(self):
        return 'consuming data'


some_lists = [
    [1, 2],
    [3, 5],
    [5, 6, 7, 1, 10.1, 11.1],
    [121.4, 11.34],
    [11.31, 1921, 321.],
]

some_sets = (
    {'1', '2'},
    {'some_node', 'node_2'},
    {'action_1', 'action_2'},
    {'id_x'}
)

some_files = [
    'file_01',
    'file_02',
    'file_03,'
    'file_01',
    'file_02',
    'file_03,'
    'file_01',
    'file_02',
    'file_03,'
    'file_01',
    'file_02',
    'file_03,'
]

some_numbers = [1, 2, 3, 4, 56]

# whole_list = []
#
# for a_list in some_lists:
#     whole_list.append(a_list)


def merge(nested):
    """
    :param nested: a list which contains lots of lists
    :return: a single list, which concat the lists.
    """
    type_op = {
        list: op.add,
        int: op.add,
        float: op.add,
        set: op.or_,
        str: op.add
    }
    # if nested is None
    # if len(nested) > 0:
    # or and ... 短路执行
    # if check_user(user_id) and user_is_activited(used_id):
    #   pass
    if nested:
        element = nested[0]
        return reduce(type_op[type(element)], nested)
    else:
        return nested


if __name__ == '__main__':
    merge(some_lists)
    merge(some_sets)
    merge(['string1', 'string2', 'string3', 'string4'])
    merge([])
    merge(None)


