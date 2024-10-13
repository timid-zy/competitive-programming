def solve():
    _, l, r, k = map(int, input().split())
    prices = list(map(int, input().split()))
    prices.sort()

    res = 0
    for n in prices:
        if l <= n <= r and n <= k:
            k -= n
            res += 1
    
    return res

for _ in range(int(input())):
    print(solve())