import random
import dis


def loop_func(elements, func=print):
    for i in elements:
        func(i)


def loop_without(elements, func):
    if not elements: return []

    if elements:
        return [func(elements[0])] + loop_without(elements[1:], func)


def collect(x, result=[]):
    if x % 2:
        result.append(x)

    return result


print(loop_without(list(range(10))), )