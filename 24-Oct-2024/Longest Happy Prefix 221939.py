# Problem: Longest Happy Prefix - https://leetcode.com/problems/longest-happy-prefix/description/

class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0] * len(s)
        l, r = 0, 1
        while r < len(s):
            if s[l] == s[r]:
                l += 1
                lps[r] = l
                r += 1
            elif l == 0:
                r += 1
            else:
                l = lps[l-1]
    
        return s[:lps[-1]]
