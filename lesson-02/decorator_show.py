

def memory(f):
    memory.cache = {}  # function attribute

    def _wrap(*args, **kwargs):
        if args in memory.cache:
            print('hit {}'.format(args))
            return memory.cache[args]
        else:
            r = f(args)
            memory.cache[args] = r
            return r

    return _wrap


def chang_result_to_none(f):
    def _wrap(n):
        return None

    return _wrap


def buttons(c):
    def button(f):
        def _wrap(*a, **kwargs):
            r = f(*a, **kwargs)
            print('press keyboard {}'.format(c))
            return r
        return _wrap
    return button


buttons_m = {
    c: buttons(c) for c in 'qwert'
}


@buttons_m['q']
def fib(n):
    return fib(n - 1) + fib(n - 2) if n >= 2 else 1


if __name__ == '__main__':
    # fib = memory(fib)
    print(fib(10))
