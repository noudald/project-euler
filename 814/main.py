'''
4n people stand in a circle with their heads down. When the bell rings they all
raise their heads and either look at the person immediately to their left, the
person immediately to their right or the person diametrically opposite. If two
people find themselves looking at each other they both scream.

Define S(n) to be the number of ways that exactly half of the people scream.
You are given and S(1) = 48 and S(10) = 420121075 mod 998244353.

Find S(10^3) mod 998244353.
'''

'''
Notes:
    * 998244353 is prime.
'''

def s(n):
    ssum = sum(6*n - 5*(k - 1) for k in range(1, n+1))
    return (3**(2*n) - (2*n - 1)) * ssum

print(s(1))
print(s(2))
print(s(10) % 998244353)
