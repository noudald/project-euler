'''
A list initially contains the numbers 2, 3, ..., n.  At each round, every
number in the list is divided by its smallest prime factor. Then the product of
these smallest prime factors is added to the list as a new number. Finally, all
numbers that become 1 are removed from the list.

For example, below are the first three rounds for n = 5

    [2, 3, 4, 5] -> [2, 60] -> [30, 4] -> [15, 2, 4]

Let S(n, m) be the sum of all numbers in the list after rounds. For example,
S(5, 3) = 15 + 2 + 4 = 21. Also S(10, 100) = 257.

Find S(10^4, 10^16) mod 1234567891.

Observations:
'''

import numpy as np

def smallest_prime_factor(n):
    for i in range(2, int(n**.5) + 1):
        if n%i == 0:
            return i
    return n

def step_naive(nlist):
    primes = np.array(list(smallest_prime_factor(n) for n in nlist))
    newlist = nlist/primes
    newlist = np.append(newlist[newlist > 1], np.prod(primes))

    return newlist

def S_naive(n, m):
    a = np.array(list(range(2, n+1)))
    for _ in range(m):
        a = step_naive(a)
    return a.sum().astype(int)

print(S_naive(5, 3), 21)
