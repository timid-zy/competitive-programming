# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C

import math

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

for _ in range(int(input())):
    n = int(input())

    st, res = -1, 0
    for i in range(25, -1, -1):
        if n & (1 << i):
            st = i if st == -1 else st
            break

    if n != (2 ** (st + 1)) - 1:
        print((2 ** (st + 1)) - 1)
        continue

    cand = 1
    for i in range(2, math.floor(n**0.5) + 1):
        if n % i == 0:
            cand = n // i
            break
    
    print(cand)
