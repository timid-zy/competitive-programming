# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        curr = res = 0
        for c in s:
            curr += 1 if c == "(" else -1
            if curr < 0:
                res += 1
                curr = 0
        
        return res + max(0, curr)
        