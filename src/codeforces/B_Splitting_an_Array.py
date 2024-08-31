n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

def checkMax(mx):
    segs = 0
    r_sum = 0
    for i in range(len(arr)):
        r_sum += arr[i]
        if r_sum >= mx:
            segs += 1
            r_sum = arr[i] if r_sum > mx else 0
    if r_sum > 0: segs += 1
    
    return segs <= target


l, r = max(arr), sum(arr)
while l < r:
    mid = l + (r - l) // 2
    if checkMax(mid):
        r = mid
    else:
        l = mid + 1

print(l)