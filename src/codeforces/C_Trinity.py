def check(arr, cuts):
    ssize = len(arr) - cuts
    if ssize <= 2:
        return True
    
    for l in range(len(arr) - ssize + 1):
        r = l + ssize - 1
        if arr[l] + arr[l+1] > arr[r]:
            return True
    
    return False

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    l, r = 0, n
    while l < r:
        mid = (r + l) // 2
        if check(arr, mid):
            r = mid
        else:
            l = mid + 1
    
    print(l)


for _ in range(int(input())):
    solve()