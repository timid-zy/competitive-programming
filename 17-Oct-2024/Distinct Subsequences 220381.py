# Problem: Distinct Subsequences - https://leetcode.com/problems/distinct-subsequences/description/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * len(s) for _ in range(len(t))]
        for ti in range(len(t)):
            for si in range(ti, len(s)):
                dp[ti][si] += dp[ti][si-1]
                if t[ti] == s[si]:
                    dp[ti][si] += dp[ti-1][si-1] if ti > 0 else 1
                
        
        return dp[-1][-1]
                