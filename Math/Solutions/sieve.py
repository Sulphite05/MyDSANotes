from math import sqrt

sieve = [1, 1] + [-1] * 10**5
n = len(sieve)
for i in range(2, int(sqrt(n))):
    if sieve[i] == -1:
        for j in range(i, n, i):
            if sieve[j] == -1: sieve[j] = i     # remembers smallest factor
