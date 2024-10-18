from math import factorial as f

def comb(n, r):
    return f(n) // (f(n-r) * f(r))

def solve():
    N = int(input())
    arr = set(map(int, input().split()))
    p = 10 - len(arr)

    return comb(p, 2) * f(4) // 4
    

for _ in range(int(input())):
    print(solve())