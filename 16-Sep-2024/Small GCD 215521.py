# Problem: Small GCD - https://codeforces.com/contest/1900/problem/D

from collections import defaultdict

def get_factors(x):
    factors = set([1])
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            factors.add(i)
            factors.add(x // i)
    
    return factors

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    dp = defaultdict(int)
    count = defaultdict(int)
    for i in range(N):
        factors = get_factors(A[i])
        for f in factors:
            dp[f] += count[f] * (len(A) - i - 1)
            count[f] += 1
    
    # eliminate over counted factors
    for k in sorted(list(dp.keys()), reverse=True):
        factors = get_factors(k)
        for local_factor in factors:
            if local_factor == k:
                continue

            dp[local_factor] -= dp[k]
    
    res = 0
    for k in dp:
        res += k * dp[k]
    
    return res

for _ in range(int(input())):
    print(solve())
