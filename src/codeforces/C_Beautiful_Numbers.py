from math import factorial as fac

MOD = 10 ** 9 + 7
FM = [1] * (10**6 + 2)
for i in range(1, len(FM)):
    FM[i] = (FM[i-1] * i) % MOD

def f(x):
    return FM[x]

def mod_inverse(x, m):
    return pow(x, m-2, m) % m

def perm(n, i):
    return (f(n) * mod_inverse(f(i) * f(n-i), MOD)) % MOD

A, B, N = map(int, input().split())
t = [str(A),  str(B)]
res = 0
for i in range(N+1):
    s = str(A*i + B*(N-i))
    valid = True
    for c in s:
        if c not in t:
            valid = False
            break

    if not valid:
        continue

    res = (res + perm(N, i)) % MOD
    
print(res)
