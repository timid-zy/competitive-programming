# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        ones = [0] * (len(s) + 1)
        for i in range(len(s) - 1, -1, -1):
            ones[i] = ones[i+1]
            if s[i] == "1": ones[i] +=1
        
        zeroes = 1 if s[0] == "0" else 0
        ans = 0
        for i in range(1, len(s)):
            ans = max(ans, zeroes + ones[i])
            if s[i] == "0": zeroes += 1
        
        return ans