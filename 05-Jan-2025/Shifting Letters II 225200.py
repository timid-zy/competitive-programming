# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pr = [0] * (len(s) + 1)
        for l, r, d in shifts:
            if d == 0: d -= 1
            pr[l] -= d
            pr[r+1] += d
        
        for i in range(len(s)-1, -1, -1):
            pr[i] += pr[i+1]
        
        
        res = ""
        for i in range(len(s)):
            res += chr((ord(s[i]) - ord('a') + pr[i+1]) % 26 + ord('a'))
        
        return res