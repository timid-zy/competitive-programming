def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    x = min(arr.count(0), arr.count(1))
    mn = 0
    if x % 2 == 1:
        mn = 1
    
    print(mn, x)

for _ in range(int(input())):
    solve()
