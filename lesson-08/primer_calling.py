from primer import collect_primes
import time

start = time.time()

for _ in range(10):
    results = collect_primes(5000)

print(f'used time = {time.time() - start}')

print(results)