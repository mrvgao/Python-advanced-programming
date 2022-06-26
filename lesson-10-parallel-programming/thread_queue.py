from queue import Queue
from threading import Thread
import time


def producer(product: Queue):
        size = product.qsize()
        threshold = 10
        while size < threshold:
            # for i in range(threshold - size):
            # time.sleep(0.001)
            product.put(size)
            print(f'put ->  {size}')
            size = product.qsize()


def consumer(product: Queue):
    while not product.empty():
        size = product.qsize()
        # print('size', size)
        if size > 0:
            # time.sleep(0.001)
            item = product.get()
            print(f'\n GET <- {item}')
            # time.sleep(0.001)
            # print('no element, I am finished')


if __name__ == '__main__':
    product_q = Queue()
    t1 = Thread(target=producer, args=(product_q, ))
    t2 = Thread(target=consumer, args=(product_q, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()