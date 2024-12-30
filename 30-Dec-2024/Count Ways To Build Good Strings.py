class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1
        MOD = (10 ** 9 + 7)
        for i in range(len(dp)):
            if i-zero >= 0:
                dp[i] += dp[i-zero]
            if i-one >= 0:
                dp[i] += dp[i-one]
            
            dp[i] %= MOD

        return sum(dp[low:high+1]) % MOD
