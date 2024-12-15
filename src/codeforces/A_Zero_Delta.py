def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    l, r = 0, len(arr) - 1
    while l < r and k > 0:
        if arr[l] == 0:
            l += 1
            continue
        
        arr[l] -= 1
        arr[r] += 1
        k -= 1
    
    print(*arr)

for _ in range(int(input())):
    solve()