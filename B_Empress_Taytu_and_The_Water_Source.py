import math

def checkD(d, a, val, k):
    hours = 0
    for i in range(len(d)):
        hours += math.ceil(d[i] / val) * a[i]

    return hours <= k


for i in range(int(input())):
    n, k = list(map(int, input().split()))
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    l, r = 1, pow(10, 9)
    while l < r:
        mid = l + (r - l) // 2
        if checkD(d, a, mid, k):
            r = mid
        else:
            l = mid + 1
    
    if checkD(d, a, l, k):
        print(l)
    else:
        print(-1)