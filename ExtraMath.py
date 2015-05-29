__author__ = '804'

def is_prime(n):
    d = 2
    while (d**2 <= n) and (n % d != 0):
        d += 1
    return d * d > n