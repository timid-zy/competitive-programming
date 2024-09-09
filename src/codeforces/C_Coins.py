dp = [float('inf')] * 101
dp[0] = 0
for i in range(1, len(dp)):
    if i-1 >= 0:
        dp[i] = min(dp[i], dp[i-1] + 1)
    if i-3 >= 0:
        dp[i] = min(dp[i], dp[i-3])
    if i-5 >= 0:
        dp[i] = min(dp[i], dp[i-5])

for _ in range(int(input())):
    print(dp[int(input())])