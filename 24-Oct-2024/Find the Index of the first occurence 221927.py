# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        for i in range(len(haystack) - len(needle) + 1):
            res = True
            c = i
            for j in range(len(needle)):
                if haystack[c] != needle[j]:
                    res = False
                    break
                
                c += 1
            
            if res: return i
        
        return -1
