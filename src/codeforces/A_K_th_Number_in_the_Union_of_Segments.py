import bisect
n, k = list(map(int, input().split()))

arr = []
min_, max_ = float('inf'), float('-inf')
for i in range(n):
    l, r = list(map(int, input().split()))
    arr.append((l, r + 1))
    min_, max_ = min(min_, l), max(max_, r)

def getLast(n):
    found = False
    count = 0
    for i in range(len(arr)):
        l, r = arr[i]
        while l < r:
            pass
    
    return count if not found else count - 1

l, r = min_, max_
while l < r:
    mid = l + (r - l) // 2
    c = getLast(mid)
    if c <= k:
        r = mid
    else:
        l = mid + 1

print(l)
