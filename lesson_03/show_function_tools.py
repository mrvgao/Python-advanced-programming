"""
Some useful function tools.

Speed up the dev process.
"""

from functools import reduce
import operator as op
from functools import cache
from functools import lru_cache
from functools import cached_property
from functools import total_ordering
from functools import partial
from functools import singledispatch
import time
import random
from icecream import ic


#Task - 01 Merge lists


# @cache
@lru_cache(maxsize=2**10)
def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 2 else 1


class User:
    def __init__(self, basic_info):
        self.basic_info = basic_info

    def __hash__(self):
        return hash(self.basic_info[0])


@lru_cache
def get_user_log(user: User):
    time.sleep(0.5)

    return f'result {user}'

@cache
def matrix(position):
    x, y = position
    if x >= 1 and y >= 1:
        return matrix((x - 1, y - 1)) + matrix((x, y - 1)) + matrix((x - 1, y))
    else:
        return x + y

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


@total_ordering
class Hero:
    def __init__(self, name,  live=None, magic=None):
        self.name = name
        self.live = live or random.randint(0, 100)
        self.magic = magic or random.randint(0, 100)

    def __lt__(self, other):
        return (self.live, self.magic) < (other.live, other.magic)

    def __eq__(self, other):
        return (self.live, self.magic) == (other.live, other.magic)


"""
Partial Function: 
    g(x, y) -> 
        h(y) = g(x, y) # x with a constant value
"""

# sorted([li_bai, cao, hunter, master] * 10)


def reset_user_base(base_info, user):
    user.basic_info = base_info


def load_training_info(agent_id, agent_name, agent_env, agent_action_space, agent_obs):
    """

    :param agent_id:
    :param agent_name:
    :param agent_env:
    :param agent_action_space:
    :param agent_obs:
    :return:
    """
    return agent_id, agent_name, agent_env, agent_action_space, agent_obs


""""

Single Dispatch

def some_func(arg1, arg2): 
    pass
"""


@singledispatch
def multiply(arg1, arg2):
    # if isinstance(arg1, int) and isinstance(arg2, str):
    #     pass
    # elif isinstance(arg1, list) and isinstance(arg2, list):
    #     pass
    # elif
    # match arg1, arg2: # in python3.10
    #     case int, str:
    #         pass
    #     case str, str:
    #         pass
    #     case int, int:
    print(arg1, arg2)
    return arg1 * arg2


@multiply.register
def _(arg1: str, arg2: str): return int(arg1) * arg2


@multiply.register
def _(arg1: int, arg2: int):
    return arg1 * arg2


@multiply.register
def _(arg1: list, arg2: list): return [a1 * a2 for a1, a2 in zip(arg1, arg2)]


@multiply.register
def _(arg1: int, arg2: str):
    return arg1 * arg2


@multiply.register
def _(arg1: Hero, arg2: int):
    arg1.live *= arg2
    arg1.magic *= arg2

    return arg1

# @multiply.register
# def _(arg1: int, arg2: list):
#     return [a * arg1 for a in arg2]


ic(multiply(3, 'test'))  #'testtesttest'
ic(multiply([3, 4, 5], [4, 5, 6])) # [12, 20, 30]
ic(multiply('4', 'test')) # 'testtesttesttes'
ic(multiply(3, 4))  # '
# multiply(3, [3, 4, 5]) # '




if __name__ == '__main__':
    # merge(some_lists)
    # merge(some_sets)
    # merge(['string1', 'string2', 'string3', 'string4'])
    # merge([])
    # merge(None)

    # print(matrix({10, 9}))

    jack = User(['Jack', 21, 178, 80])
    ma = User(['Ma', 81, 43, 11])

    print(get_user_log(jack))
    print(get_user_log(ma))
    print(get_user_log(jack))

    li_bai = Hero('libai')
    cao = Hero('caocao')
    hunter = Hero('deman-hunter')
    master = Hero('blood-master')
    print(li_bai, cao, hunter, master)

    print(Hero('libai', 10, 10) == Hero('caocao', 10, 10))
    print(Hero('libai', 11, 10) >= Hero('caocao', 10, 10))

    agent_1_config = {
        "agent_id": 'agent_01',
        "agent_name": "jack",
        # "agent_env": 'foot_ball',
        "agent_action_space": list(range(6))
    }

    load_agent_1_obs = partial(load_training_info, **agent_1_config)

    print(load_agent_1_obs)
    ic(load_agent_1_obs(agent_obs=[0.1, 0.2, 0.3, 0.4], agent_env='dota2'))

    reset_user_base('base-info_typ1', User('1'))
    reset_user_base('base-info_typ1', User('2'))
    reset_user_base('base-info_typ1', User('3'))
    reset_user_base('base-info_typ1', User('4'))
    reset_user_base('base-info_typ1', User('5'))

    rest_type1 = partial(reset_user_base, base_info='base_info_typ1')

    u = User('1')
    rest_type1(user=u)
    ic(u.basic_info)

    multiply(li_bai, 2)
