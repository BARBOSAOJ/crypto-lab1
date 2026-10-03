# Lab 1A - part D
import sys

# D.1 with 6k-1 and 6k+1
def is_prime_6k(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    k = 5
    while k * k <= n:
        if n % k == 0 or n % (k + 2) == 0:
            return False
        k += 6
    return True

print("D.1", [n for n in range(1, 101) if is_prime_6k(n)])

# D.2
primes = [n for n in range(1, 1001) if is_prime_6k(n)]
print("D.2 highest prime up to 1000:", primes[-1])

# D.3 sieve from the lab sheet
def sieve_for_primes_to(n):
    size = n // 2
    sieve = [1] * size
    limit = int(n ** 0.5)
    for i in range(1, limit):
        if sieve[i]:
            val = 2 * i + 1
            tmp = ((size - 1) - i) // val
            sieve[i + val::val] = [0] * tmp
    return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0]

for test in (100, 1000, 5000, 10000):
    print("D.3 up to", test, "->", sieve_for_primes_to(test)[-1])

# D.4 Miller-Rabin
import random
def miller_rabin(n, k=20):
    if n < 2:
        return False
    for p in (2, 3, 5, 7):
        if n % p == 0:
            return n == p
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

for n in (5, 7919, 858599509, 982451653, 982451652):
    print("D.4", n, "prime?", miller_rabin(n))
