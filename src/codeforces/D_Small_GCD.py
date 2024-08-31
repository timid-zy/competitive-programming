from math import ceil
from collections import defaultdict

def factors(x):
    res = set([1, x])
    for cand in range(2, ceil(x ** 0.5) + 1):
        if x % cand == 0:
            res.add(cand)
            res.add(x // cand)

    return res

for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    A.sort()

    dp = defaultdict(int)
    counts = defaultdict(int)
    for i, n in enumerate(A):
        fs = factors(n)
        for f in fs:
            dp[f] += counts[f] * (len(A) - i - 1)
            counts[f] += 1
    
    for k in sorted(dp.keys(), reverse=True):
        fs = factors(k)
        for f in fs:
            if f == k: continue
            dp[f] -= dp[k]

    res = sum(k * dp[k] for k in dp)
    print(res)
