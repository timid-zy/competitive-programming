def getTwos(m):
    c = 0
    while m % 2 == 0:
        m /= 2
        c += 1
    
    return c

for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    curr = 0
    for i in range(len(arr)):
        curr += getTwos(arr[i])
    
    req = n - curr
    if req == 0:
        print(0)
        continue
    
    if n % 2 == 1: n -= 1
    cands = []
    for j in range(n, 0, -2):
        cands.append(getTwos(j))
    
    cands.sort(reverse=True)
    ops = 0
    for i in cands:
        if req <= 0:
            break
        ops += 1
        req -= i
    
    if req <= 0:
        print(ops)
    else:
        print(-1)