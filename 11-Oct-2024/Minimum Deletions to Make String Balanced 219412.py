# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        # dp = bc = 0
        # for c in s:
        #     if c == "a":
        #         dp = min(bc, dp + 1)
        #     else:
        #         bc += 1
        
        # return dp

        n = len(s)
        ac = [0] * n
        bc = [0] * n
        bc[0] = 1 if s[0] == "b" else 0
        ac[-1] = 1 if s[-1] == "a" else 0
        for i in range(1, n):
            bc[i] = bc[i-1]
            if s[i] == "b":
                bc[i] += 1
        
        for i in range(n - 2, -1, -1):
            ac[i] = ac[i+1]
            if s[i] == "a":
                ac[i] += 1
        
        ans = float('inf')
        for i in range(n):
            ans = min(ans, ac[i] + bc[i] - 1)
        
        return ans
