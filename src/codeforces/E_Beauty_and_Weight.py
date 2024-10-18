from collections import defaultdict

def solve():
    N, M, MXW = map(int, input().split())
    W = list(map(int, input().split()))
    B = list(map(int, input().split()))

    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        
        if abs(a - b) == 1:
            edges.append((a, b))
    
    edges.sort()
    nxtint = 0
    jump = {}
    grp = {}
    for x, y in edges:
        if x in grp:
            grp[y] = grp[x]
            jump[grp[x]] = y + 1
        else:
            grp[x] = grp[y] = nxtint
            jump[grp[x]] = y + 1
            nxtint += 1
    
    grpweights = defaultdict(int)
    grpvalues = defaultdict(int)
    for i, v in grp.items():
        grpweights[v] += W[i-1]
        grpvalues[v] += B[i-1]

    dp = [[0] * (MXW + 1) for _ in range(N + 1)]
    for idx in range(N-1, -1, -1):
        for w in range(MXW):
            # no take
            dp[idx][w] = dp[idx+1][w]

            # take one
            if w + W[idx] <= MXW:
                diff = idx + 1
                if idx + 1 in grp:
                    diff = jump[grp[idx + 1]] - 1

                dp[idx][w] = max(dp[idx][w], dp[diff][w + W[idx]] + B[idx])
            
            # take group
            if idx + 1 in grp and w + grpweights[grp[idx+1]] <= MXW:
                diff = jump[grp[idx + 1]] - 1
                dp[idx][w] = max(dp[idx][w], dp[diff][w + grpweights[grp[idx+1]]] + grpvalues[grp[idx+1]])

    return max(dp[0])

print(solve())