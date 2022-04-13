import time
import numpy as np


def test_string_cut(size, proce=lambda x: x):
    string = b'x' * size
    #
    string = proce(string)
    # memory_viewed = paramters
    # memory_viewed = string

    start = time.time()

    # window = memory_viewed[:]

    step = 1
    while string:
        string = string[:-step]

    # window = paramters[:, :]
    #
    # while len(window) > 4:
    #     window = window[:-1, :-1]

    end = time.time()

    print(f'size {size} used time = {end - start}')


for s in [1000, 2000, 5000, 10000, 100000]:
    test_string_cut(s)
    test_string_cut(s, proce=memoryview)

