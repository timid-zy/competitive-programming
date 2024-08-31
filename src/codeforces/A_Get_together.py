import bisect

arr = []
for i in range(int(input())):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x: x[0])

def checkTime(t):
    ub = arr[0][0] + t * arr[0][1]
    lb = arr[-1][0] - t * arr[-1][1]
    if ub < lb: return False

    for i in range(1, len(arr) - 1):
        pos, v = arr[i]
        l, u = pos - t * v, pos + t * v
        
        if lb > u or l > ub:
            return False

        lb = max(lb, l)
        ub = min(ub, u)
    
    return True

l, r = 0, arr[-1][0] - arr[0][0]

while abs(r - l) > pow(10, -6):
    mid = l + (r - l) / 2
    if checkTime(mid):
        r = mid
    else:
        l = mid

print(l)