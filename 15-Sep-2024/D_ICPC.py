from collections import defaultdict

def solve():
    N = int(input())
    U = list(map(int, input().split()))
    SK = list(map(int, input().split()))

    unis = defaultdict(list)
    total = 0
    for i in range(N):
        unis[U[i]].append(SK[i])
        total += SK[i]

    sk_sum = defaultdict(int)
    prefix = defaultdict(list)
    for k in unis:
        unis[k].sort()
        if len(unis[k]) == 0:
            continue

        prefix[k] = [unis[k][0]]
        for i in range(1, len(unis[k])):
            prefix[k].append(prefix[k][-1] + unis[k][i])

        sk_sum[k] = sum(unis[k])
    
    res = [0] * N
    res[0] = total
    keys = sorted(list(unis.keys()), key=lambda x: len(unis[x]), reverse=True)
    for i in range(1, N):
        local_sum = 0
        for k in keys:
            lc = sk_sum[k]
            rem = len(unis[k]) % (i + 1)
            if rem >= len(unis[k]):
                lc -= sk_sum[k]
            elif rem > 0:
                lc -= prefix[k][rem-1]
            
            local_sum += lc
            if lc == 0:
                break
        
        res[i] = local_sum

    return res

for _ in range(int(input())):
    ans = solve()
    print(*ans)
