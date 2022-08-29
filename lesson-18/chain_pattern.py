import numpy as np


def complex_functions(x, *funcs):
    if len(funcs) == 1: 
        return funcs[0](x)
    else:
        return complex_functions(funcs[0](x), *funcs[1:])



def add_10(x): return x + 10

def mod_7(x): return x % 7

def cube(x): return x ** 2

def sigmoid(x):  return 1 / (1 + np.exp(-x))

print(complex_functions(1, add_10))

print(complex_functions(1, add_10, mod_7, cube, cube, mod_7, sigmoid))
print(complex_functions(1, mod_7, cube, sigmoid, add_10, cube))
