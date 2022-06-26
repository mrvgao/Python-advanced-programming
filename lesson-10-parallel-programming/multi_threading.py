from threading import Thread
from threading import Lock
from queue import Queue
import random
import time
from functools import reduce


thread_visit = 0

visit_lock = Lock()


def my_func(self_id=None, q=None):
    # print()
    global thread_visit
    for i in range(1000):
        # time.sleep(0.001)
        # q.append(i)
        # print(f'fid: {self_id} -- {i}', end=' ')
        # if q:
            # q.get_nowait()
            # q.put(1)
            # q.task_done()
        # with visit_lock:
        visit_lock.acquire()
        # v = thread_visit
        thread_visit += 1
        visit_lock.release()
        # thread_visit = v + 1
        # thread_visit += 1


if __name__ == '__main__':
    note_queue = Queue()
    # thread1 = Thread(target=my_func, args=(1, ))
    # thread2 = Thread(target=my_func, args=(2, ))
    # thread3 = Thread(target=my_func, args=(3, ))

    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread3.start()
    # thread2.join()
    # thread3.join()

    TOTAL = 10

    results = [[] for _ in range(TOTAL)]
    threads = [
        Thread(target=my_func, args=(i, results[i])) for i in range(TOTAL)
    ]

    for t in threads: t.start()

    for t in threads: t.join()

    # print(results)
    # print('\n visisted num: ', reduce(lambda a, b: a + b, map(len, results)))
    print('\n visisted num: ', thread_visit)
    # thread.join()
    # " This blocks the calling thread until the thread whose join() method is
    # " called terminates -- either normally or through an unhandled exception
    # "   or until the optional timeout occurs.

    # map-reduce-for word count
    # monta-carlo simulate