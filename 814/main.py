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
    * Naive, S(1) = 48 = 2^4 * 3,
             S(2) = 2256 = 2^4 * 3 * 47,
             S(3) = 125784 = 2^3 * 3^2 * 1747
'''

def gen_all_edges(n, nodes):
    if len(nodes) == 0:
        return [[]]

    node = nodes[0]
    e1 = (node, (node + 1) % (4*n))
    e2 = (node, (node - 1) % (4*n))
    e3 = (node, (node + 2*n) % (4*n))

    all_edges = []
    for edges in gen_all_edges(n, nodes[1:]):
        all_edges.append([e1] + edges)
        all_edges.append([e2] + edges)
        all_edges.append([e3] + edges)

    return all_edges

def count_double_heads(edges):
    count = 0
    for (e0, e1) in edges:
        if (e1, e0) in edges:
            count += 1
    return count

def s_naive(n):
    nodes = list(range(4*n))
    all_edges = gen_all_edges(n, nodes)

    count = 0
    for edges in all_edges:
        if count_double_heads(edges) == 2*n:
            count += 1

    return count

print(s_naive(1), 48)
print(s_naive(2), 2256)
print(s_naive(3), 125784)

'''

def s(n):
    ssum = sum(6*n - 5*(k - 1) for k in range(1, n+1))
    return (3**(2*n) - (2*n - 1)) * ssum

print(s(1), 48)
print(s(2), 243)
print(s(10) % 998244353, 420121075)

'''
