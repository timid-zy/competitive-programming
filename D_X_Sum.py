from collections import defaultdict

for _ in range(int(input())):
    N, M = map(int, input().split())
    mat = []
    for _ in range(N):
        row = list(map(int, input().split()))
        mat.append(row)
    
    lrd = defaultdict(int)
    rrd = defaultdict(int)
    for r in range(N):
        for c in range(M):
            rrd[r-c] += mat[r][c]
            lrd[r+c] += mat[r][c]
    
    ans = float('-inf')
    for r in range(N):
        for c in range(M):
            ans = max(
                ans,
                lrd[r+c] + rrd[r-c] - mat[r][c]
            )
    
    print(ans)
