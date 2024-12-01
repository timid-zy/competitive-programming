def solve():
    n = int(input())
    res = ((n) * (n+1)) // 2
    c = 1
    while c <= n:
        res -= 2 * c
        c *= 2
    
    return res


for _ in range(int(input())):
    print(solve())