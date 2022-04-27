from icecream import ic


def some_func(arg1, arg2=0, arg3=[1, 2, 3, 4]):
    print(arg3)
    return arg1 + arg2


ic(some_func.__code__.co_varnames)
ic(some_func.__defaults__)

some_func(1, 2, arg3=[-1, -2, -3])
ic(some_func.__defaults__)

ic(some_func(1, 2))

var = some_func

var(1, 2)


class FuncClass:
    def __int__(self):
        pass

    def __call__(self, arg1, arg2=0):
        return arg1 + arg2


another_some_func = FuncClass()

print(another_some_func(1, 2))
