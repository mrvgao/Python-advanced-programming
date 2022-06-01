cimport cython
from libc.stdlib cimport malloc, free


def is_prime(int n):
    cdef int i

    for i in range(2, n):
        if n % i == 0: return False

    return True


def collect_primes(n):
    # cdef int n = 5000
    # cdef int *primes

    # primes = <int *>malloc(n*cython.sizeof(int))
    # cdef vector[int] primers
    # primes = []
    # cdef vector[int] primes
    # primes.reserve(n)

    cdef int i
    cdef int length

    primers = []

    for i in range(2, n):
        if is_prime(i):
            # primes.append(i)
            # primes.push_back(i)
            # primes[length] = i
            # primers.append(i)
            primers.append(i)
            # primes[length] = i
            # length += 1
            # primers.push_back(i)

    # return primes[:length]
    # results = [p for p in primes[:length]]
    #
    # return results

