n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

def checkDistance(d):
    cows = target - 1
    curr = 0

    for i in range(1, len(arr)):
        if arr[i] - arr[curr] >= d:
            cows -= 1
            curr = i
    
    return cows <= 0

l, r = 1, arr[-1] - arr[0]

while l < r:
    mid = l + (r - l) // 2
    if r - l == 1:
        if checkDistance(r):
            l = r
        else:
            r = l
        break
    
    if checkDistance(mid):
        l = mid
    else:
        r = mid - 1

print(l)