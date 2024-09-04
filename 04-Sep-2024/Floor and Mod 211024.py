# Problem: Floor and Mod - https://codeforces.com/problemset/problem/1485/C

import math

def solve():
    x, y = map(int, input().split())
    res = 0
    nxt_start, skip = 3, 5 

    for rem in range(1, math.floor(x**0.5) + 1):
        pairs = min(
            (x - nxt_start) // rem + 1,  # check if x is a limiter
            y - rem  # all possible
        )

        if pairs > 0:
            res += pairs
        
        nxt_start += skip
        skip += 2
        
    return res


for _ in range(int(input())):
    print(solve())
