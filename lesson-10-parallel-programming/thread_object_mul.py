import random
from collections import Counter
from collections import deque
# from threading import Thread
from multiprocessing import Pool
import ctypes
from multiprocessing import Process


class Thinker:
    def __init__(self, elements=None):
        self.elements = deque([]) or deque(elements)

    def next(self):
        """
        :return: the next element it will receive.
        """

        return Counter(self.elements).most_common(1)[0][0]

    def obs(self, x):
        max_length = 20

        while len(self.elements) > max_length:
            self.elements.popleft()

        self.elements.append(x)


def train(agent, num=10):
    # print('run into!')
    # thinker = eval('thinker')
    for i in range(num):
        print('step in loop')
        agent.obs(random.randint(0, 10))
        print(f'thinker id : {id(agent)} next: {agent.next()}')
        # print(i + num2)


def generate_objs():
    # some process -> obj -> send to another process
    return Thinker([random.randint(1, 10) for _ in range(3)])
    # return True


def get_results():
    return 1


def recovery_obj(_id):
    return ctypes.cast(_id, ctypes.py_object).value


def mul_trainer():
    # p1 = Process(target=generate_objs)
    # p1.start()
    # result = p1
    # print(result)
    num_process = 4
    with Pool(num_process) as pool:
        results = pool.starmap(generate_objs, [() for _ in range(num_process)])

    print(results)
    ids = [id(r) for r in results]
    print(ids)
    #
    # for obj in map(recovery_obj, ids):
    #     print(obj)
    with Pool(num_process) as pool:
        results = pool.map(recovery_obj, ids)
    # for i in ids:
    #     print(f'recovery: {i}')
    #     print(recovery_obj(_id=i))
    # second = ids[1]
    # print(int(second))

    # print(recovery_obj((second))))
    # print(recovery_obj((int(second))))
    # print(recovery_obj((int(second))))
    # print(recovery_obj((int(second))))

    # with Pool(num_process) as pool:
    #     recoveried = pool.map(recovery_obj, ids)

    # for obj in recoveried:
    #     print(obj)

    # for obj in map(recovery_obj, ids):
    #     print(obj)

    # for r in results:

    # with Pool() as pool:
    #     pool.map(train, results[::-1])

    # print(type(results))

    # print(results)
    # thinker = Thinker([1, 3, 1, 2])
    # thinker2 = Thinker([1, 2, 3, 1])
    # thinker3 = Thinker([1, 2, 3, 1])
    # thinker4 = Thinker([1, 2, 3, 1])
    #
    # each_train = 200
    #
    # thread_num = 10
    #
    # process_num = 4
    # with Pool(processes=process_num) as pool:
    #     pool.map(train, [thinker, thinker2, thinker3, thinker4])
    pass


if __name__ == '__main__':
    # new_thinker = Thinker([1, 2, 3])
    # id_ = id(new_thinker)
    # obj = ctypes.cast(id_, ctypes.py_object).value
    # print(obj.elements)
    mul_trainer()

    # threads = [Thread(target=train, args=(thinker, each_train)) for _ in range(thread_num)]

    # for t in threads:
    #     t.start()
    #
    # for t in threads:
    #     t.join()
    #
    # print(thinker.next())



