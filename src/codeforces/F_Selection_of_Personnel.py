from math import factorial as f

def comb(n, r):
    return f(n) // (f(n-r) * f(r))

N = int(input())
ans = comb(N, 5) + comb(N, 6) + comb(N, 7)
print(ans)