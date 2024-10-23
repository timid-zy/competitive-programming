from math import factorial as f

def comb(n, r):
    return f(n) // (f(n-r) * f(r))

n = int(input())
print(comb(n, 5) + comb(n, 6) + comb(n, 7))
