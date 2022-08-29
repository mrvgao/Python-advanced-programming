from functools import wrap

def func2(func):
    @wrap
    def _wrap(*args, **kwargs):
        do_something_else()
        return func(*args, **kwargs)
    return _wrap
        

@func2
def func1():
    pass

"""
@func2
def func1():
    pass

=> 

func1 = func2(func1)

"""
