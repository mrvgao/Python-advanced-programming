from collections import defaultdict
from icecream import ic


some_elements = list()


def append(e, elements):
    return elements.append(e)


def get(elements):
    return elements.pop(0)
    # return elements.pop(-1)
    # list-> pop(0) : 队列
    # pop(-1) 堆栈


nested_tree = {
    'a': {
        'a1': {
            'b': {'b1': -1,
                  'b2': {'b21': {'b211': 0,
                                 'b212': 1}}}

        },
        'a2': {
            'c': {'c1': -2,
                  'c2': {'c21': {'c211': 2,
                                 'c212': 3}}}
        },
        'a3': {
            'd': {'d1': -3,
                  'd2': {'d21': {'d211': 4,
                                 'd212': 5}}}
        }
    }
}

# print(nested_tree)


def get_connect_graph(tree):
    connect_graph = defaultdict(list)

    for node, connect in tree.items():
        if isinstance(connect, dict):
            for k in connect:
                connect_graph[node].append(k)
            connect_graph |= get_connect_graph(connect)
        else:
            connect_graph[node].append(connect)

    return connect_graph


def get_next(a, b, A, B):
    """
    :param a:  current water amount in cup a.
    :param b:  current water amount in cup b.
    :param A:  capacity of cup A
    :param B:  capacity of cup B
    :return:   the next possible state
    """
    next_state = {
        "a -> P": (0, b),
        "b -> p": (a, 0),
        "p -> a": (A, b),
        "p -> b": (a, B),
        "a -> b": (a + b - B, B) if a + b > B else (0, a + b),
        "b -> a": (A, a + b - A) if a + b > A else (a + b, 0),
    }

    return next_state


def search(a, b, A, B, target=None):
    paths = [ [('init', (a, b))] ]

    seen = set()

    while paths:
        ic(paths)
        path = get(paths)
        # path = paths[0]

        state = path[-1][-1]

        if state in seen: continue

        # for next_ in connect_g[node]:
        for action, next_s in get_next(*state, A, B).items():
            # need_visit.append(next_)
            paths.append(path + [(action, next_s)])

            if target in next_s:
                return paths[-1]

        seen.add(state)

        paths = sorted(paths, key=len)


def matter_match(names):
    match names:
        case [first, *middle, last] if len(middle) < 3:
            print(f"{first} and {last} have some few friends")
        case [first, *middle, last] if len(middle) >= 5:
            print(f"{first} and {last} have some many friends!!!, they got {len(middle)}!! ")
        case _:
            print('just two boys')


matter_match(['Tom', "Joey", 'Alice', "Ross"])
matter_match(['Tom', "Joey", "Jack", "Mike", "Alex", 'Alice', "Rancher"])


# connect_graph = get_connect_graph(nested_tree)
# ic(search(a=0, b=0, A=90, B=40, target=70))

# L1 = [.......]
# L2 = [... ]
# L4 = [.... ]

