# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        pr = [0] * len(s)
        pr[-1] = 1 if s[-1] == "1" else 0
        for i in range(len(s)-2, -1, -1):
            pr[i] = pr[i+1]
            if s[i] == "1": pr[i] += 1

        res = z = 0
        for i in range(1, len(s)):
            if s[i-1] == "0":
                z += 1
        
            res = max(res, z + pr[i])

        return res 