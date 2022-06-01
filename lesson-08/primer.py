def is_prime(n):
    for i in range(2, n):
        if n % i == 0: return False

    return True


def collect_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)

    return primes

