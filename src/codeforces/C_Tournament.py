def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[0]*15 for _ in range(N)]
    dp[0][0], dp[0][1] = A[0] - K, A[0] // 2
    for i in range(1, len(A)):
        for halves in range(min(i+2, 15)):
            dp[i][halves] = max(
                dp[i-1][halves] + (A[i] // (2 ** halves)) - K, # full pick
                dp[i-1][halves-1] + (A[i] // (2 ** halves)) if halves > 0 else float('-inf') # half pick
            )

    max_cols = float('-inf')
    for r in dp:
        max_cols = max(max_cols, r[-1])        

    return max(*dp[-1], max_cols)


for _ in range(int(input())):
    print(solve())