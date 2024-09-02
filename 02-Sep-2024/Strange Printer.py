# Problem: Strange Printer - https://leetcode.com/problems/strange-printer/

class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def dp(i, j):
            print(i, j)
            if i > j: return 0
            res = dp(i, j-1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    res = min(
                        res,
                        dp(i, k-1) + dp(k, j-1)
                    )
            
            return res
            
        return dp(0, len(s)-1)