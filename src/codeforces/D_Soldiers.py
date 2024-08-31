import math

def get_factor_count(n, dp):
    d = None
    for i in range(math.floor(n ** 0.5), 1, -1):
        if n % i == 0:
            d = i
    
    if d is None:
        return 1
    
    d2 = n // d
    return (dp[d-1] - dp[d-2]) + (dp[d2 - 1] - dp[d2 - 2])

dp = [0]
for i in range(2, 5_000_000):
    dp.append(dp[-1] + get_factor_count(i, dp))

