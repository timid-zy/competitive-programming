w, h, n = list(map(int, input().split()))

def checkFit(s):
    global n
    ver = s // h
    hor = s // w
    return ver * hor >= n

l, r = 0, max(w, h) * n
while l < r:
    mid = l + (r - l) // 2
    if checkFit(mid):
        r = mid
    else:
        l = mid + 1

print(l)