for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    mx = max(A)
    res = []
    for _ in range(M):
        o, l, r = input().split()
        l, r = int(l), int(r)

        if not (l <= mx <= r):
            res.append(mx)
            continue
            
        if o == "+":
            mx += 1
            res.append(mx)
        else:
            mx -= 1
            res.append(mx)
    
    print(*res)