# Parallel Programming

import random
import requests
import time
from threading import Thread
from threading import Lock

visited = 0
url_lock = Lock()


def get_url_content(results=None):
    fid = f'{random.randint(100, 999)}'
    print(f'fid-{fid} started')
    for i in range(10):
        time.sleep(0.00001)
        # 1. Web-Page, Database
        # 2. File-IO, Image-Process
        # 3. Use-Input, Output
        # with url_lock:
        # print(url_lock.locked())
        # url_lock.acquire()
        # global visited
        # visited += 1
        # print(url_lock.locked())
        # url_lock.release()
        # print(url_lock.locked())

        print(f'func-{fid} : {i}', end=' ')
        if results is not None:
            results.append(i)


if __name__ == '__main__':
    begin = time.time()
    total = 10
    collectd = [[] for _ in range(total)]

    threads = [
        Thread(target=get_url_content, args=(collectd[i], )) for i in range(total)
        # Thread(target=get_url_content, kwargs={'results': collectd[i]})
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('\ncollected elements == ', sum(map(len, collectd)))
    # word-count
    # simulation

    # thread1 = Thread(target=get_url_content)
    # thread2 = Thread(target=get_url_content)
    # thread3 = Thread(target=get_url_content)
    # thread4 = Thread(target=get_url_content)

    # thread1.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()
    # get_url_content()
    # get_url_content()
    # get_url_content()
    # get_url_content()
    # thread1.join()
    # thread2.join()
    # thread3.join()
    # thread4.join()
    end = time.time()
    print(f'\ntime:  {end - begin}')
    print(f'visited-{visited}')
