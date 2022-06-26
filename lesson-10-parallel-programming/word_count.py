import os
from collections import Counter
import re
import time
from threading import Thread
from functools import reduce

path = '../week-5-data-structure'


def token(string):
    return re.findall('\w+', string)


def process_file(filename, counter):
    if filename.endswith('bin'): return
    else:
        # file_name = os.path.join(path, filename)
        if os.path.isdir(filename): return

        for i, line in enumerate(open(filename).readlines()):
            if i % 50 == 0:
                print(f'process - {filename}')
            counter.update(token(line))


start = time.time()

files = os.listdir(path)
print(files)

counters = [Counter() for _ in files]

f_threads = [
    Thread(target=process_file, args=(os.path.join(path, f), counters[i])) for i, f in enumerate(files)
]

for f in f_threads:
    f.start()

for f in f_threads:
    f.join()

# print(words_count.most_common())
end = time.time()

print(reduce(lambda a, b: a | b, counters).most_common())

print('time consumed, ', end - start)
