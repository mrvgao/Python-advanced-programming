"""" Itertools
"""
import itertools
from dataclasses import dataclass
import random

some_names = ['GRU', 'CNN', 'LSTM']
lr = [1e-3, 1e-4, 3e-5, 1e-6]
gamma = [1e-3, 1e-2, 1e-1]

# set{A} X set{B}
@dataclass
class Model:
    lr: float
    gamma: float


class CNN(Model):
    pass


class GRU(Model):
    pass


class LSTM(Model):
    pass


def run_a_model(model_name, lr, gamma):
    model_name_mapping = {
        'CNN': CNN,
        'LSTM': LSTM,
        'GRU': GRU,
    }

    print(f'running model {model_name} as {lr} {gamma} ')
    acc = model_name_mapping[model_name](lr, gamma)

    print(acc)

# group by


if __name__ == '__main__':
    # for p in itertools.product(some_names, lr, gamma):
    #     run_a_model(*p)

    for n in itertools.permutations(some_names, r=2):
        print(n)

    print('*'*8)
    for n in itertools.combinations(some_names, r=2):
        print(n)

    mock_login = ['uid22111', 'uid2213', 'uid2322', 'uid2344', 'uid2321'] * 20
    random.shuffle(mock_login)

    print(mock_login)

    for g, elements in itertools.groupby(mock_login, key=lambda n: int(n[-1]) % 2):
        print(g, list(elements))

    numbers = [2, 1, 31, 21, 41, 1, 31, 12, 1, 43, 1, 43, 12, 43, 11, 12, 31]
    max_list = [2, 2, 31, 31, 41, 41, 41, 41]

    # for 0 -> N
    print(list(itertools.accumulate(numbers, max)))
    print(list(itertools.accumulate(numbers, min)))
    print(list(itertools.accumulate(numbers, lambda x, y: x + y)))

    # for r in itertools.tee(numbers, 3):
    #     print(list(r))

    lines = open('itertools_show.py')

    # for lines_copy in itertools.tee(lines, 2):
    #     for line in lines: # -> Pytorch, tensorflow: Dataloader
    #         print(line)

    for line in lines:
        print(line)

    print('#'*8)

    for line in lines:
        print(line)

