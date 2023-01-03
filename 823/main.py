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
    * If the chain has a loop, it will continue to loop. It's sufficient to
      find a loop in S(10^4, 10^16), such that we don't have to calculate all
      10^16 steps.
    * We already have to complete prime factorization of all the numbers we
      add to the end of the list.
    * Cycles are less common than I thought. Perhaps they can be found in a
      different way?
    * Sum of integers is not unique, e.g., in S(6, 10^16) we have
      [[2, 3, 5], [2, 3], [2, 2]] = 40 and [[2], [2, 3, 3], [2, 2, 5]] = 40.
'''

import numpy as np

from functools import reduce

from tqdm import tqdm


# Constants
N = 10**4
M = 10**6
P = 1234567891


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


def step(nlist):
    # Step 1, find smallest primes.
    smallest_prime = []
    for elm in nlist:
        if isinstance(elm, list):
            smallest_prime.append(elm[0])
        else:
            smallest_prime.append(smallest_prime_factor(elm))

    # Step 2, divide by smallest prime number.
    newlist = []
    for prime, elm in zip(smallest_prime, nlist):
        if isinstance(elm, list):
            if len(elm) == 1:
                continue
            else:
                newlist.append(elm[1:])
        else:
            if prime == elm:
                continue
            else:
                newlist.append(elm // prime)

    # Step 3, add product of primes to list.
    newlist.append(sorted(smallest_prime))

    return newlist

def prod(e):
    if isinstance(e, list):
        return reduce(lambda x, y: x*y, e)
    else:
        return e

def S(n, m):
    a = list(range(2, n+1))
    ap = sum([prod(elm) for elm in a]) % P
    hist = [a]
    hist2 = [ap]
    for i in range(m):
        a = step(a)
        ap = sum([prod(elm) % P for elm in a]) % P
        # print('{:<4} {:<6} {}'.format(i, sum([np.prod(elm) for elm in a]), a))
        print('{:<4} {:<6}'.format(i, ap))
        if a in hist:
            print('Found cycle!', i)
            break
        if ap in hist2:
            print('Found double value!', i)
            break
        hist.append(a)
        hist2.append(ap)
        if i == 1000:
            break
    return sum([np.prod(elm) for elm in a])

print(S(5, 3), 21)

S(10**4, 10**16)

# for i in range(10, 1000):
#     S(i, 10**16)
