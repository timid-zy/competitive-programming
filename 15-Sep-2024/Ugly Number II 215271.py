# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        t1 = t2 = t3 = 0
        for i in range(1, n):
            v1, v2, v3 = dp[t1] * 2, dp[t2] * 3, dp[t3] * 5
            if v1 <= v2 and v1 <= v3:
                dp[i] = v1
                t1 += 1
            if v2 <= v3 and v2 <= v1:
                dp[i] = v2
                t2 += 1
            if v3 <= v2 and v3 <= v1:
                dp[i] = v3
                t3 += 1

        return dp[-1]
                