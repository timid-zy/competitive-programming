# Problem: Twin Permutations - https://codeforces.com/contest/1831/problem/A

def solve():
    n  = int(input())
    arr = list(map(int, input().split()))
    
    target = n + 1
    for i in range(len(arr)):
        arr[i] = target - arr[i]
    
    return arr

for _ in range(int(input())):
    res = solve()
    print(*res)