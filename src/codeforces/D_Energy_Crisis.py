_, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
k = 1 - (k / 100)

def checkVal(v):
    backlog = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] >= v:
            backlog += (arr[i] - v) * k
        else:
            req = v - arr[i]
            backlog -= req
            if backlog < 0: return False
    
    return True


l, r = arr[0], arr[-1]
while abs(r - l) > pow(10, -6):
    mid = l + (r - l) / 2
    if checkVal(mid):
        l = mid
    else:
        r = mid

print(l)