# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        idx = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        seen = {(0, 0, 0, 0, 0): -1}
        curr = [0, 0, 0, 0, 0]
        ans = 0
        for i in range(len(s)):
            if s[i] in idx:
                curr[idx[s[i]]] = (curr[idx[s[i]]] + 1) % 2
            
            if tuple(curr) in seen:
                ans = max(ans, i - seen[tuple(curr)])
            
            if tuple(curr) not in seen:
                seen[tuple(curr)] = i
        
        return ans
