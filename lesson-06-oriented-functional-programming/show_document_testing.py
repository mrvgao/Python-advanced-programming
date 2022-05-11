
def fib(n):
    """
    Get fib numbers ... 

    >>> fib(1)
    1
    >>> fib(5)
    5
    >>> fib(11)
    89

    """ 
    return fib(n - 1) + fib(n - 2) if n > 2 else 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
