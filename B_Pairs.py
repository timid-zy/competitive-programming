def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    mn, mnidx = float('inf'), 0
    for i, n in enumerate(arr):
        if n < mn:
            mn, mnidx = n, i
    
    mx, mxidx = float('-inf'), 0
    for i, n in enumerate(arr):
        if n >= mx:
            mx, mxidx = n, i
    
    return sorted([mnidx + 1, mxidx + 1])

for _ in range(int(input())):
    ans = solve()
    print(*ans)