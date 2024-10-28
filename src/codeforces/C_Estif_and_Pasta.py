def solve():
    n = int(input())
    MOD = 10 ** 9 + 7
    res = 6
    d = 16
    for i in range(n-1):
        res = (res * d) % MOD
        d = (d * d) % MOD
    
    return res

print(solve())