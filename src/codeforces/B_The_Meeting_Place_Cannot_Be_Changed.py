input()
pos = list(map(int, input().split()))
speed = list(map(int, input().split()))
arr = list(zip(pos, speed))
arr.sort(key=lambda x: x[0])

def checkTime(t):
    ub = arr[0][0] + (arr[0][1] * t)
    lb = arr[-1][0] - (arr[-1][1] * t)
    
    if lb > ub: return False

    for i in range(1, len(arr) - 1):
        pos, speed = arr[i]
        l, r = pos - (speed * t), pos + (speed * t)
        if l > ub or r < lb:
            return False
        
        lb, ub = min(lb, l), min(ub, r)
    
    return True

l, r = 0, arr[-1][0]
while abs(r - l) > pow(10, -6):
    mid = l + (r - l) / 2
    if checkTime(mid):
        r = mid
    else:
        l = mid

print(r)