def function (a: int, b : int) -> str:
    return str(a + b)

def add_with_type(int a, int b):
    return a + b

def fib(a):
    return fib(a - 1) + fib(a - 2) if a >= 2 else 1

print('the simple loaded!')
