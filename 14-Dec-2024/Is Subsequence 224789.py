# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        for ti in range(len(t)):
            if si == len(s):
                return True
            
            if s[si] == t[ti]:
                si += 1

        
        return si == len(s)