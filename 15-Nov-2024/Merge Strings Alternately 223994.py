# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        res = []
        while l < len(word1) and l < len(word2):
            res.append(word1[l])
            res.append(word2[l])
            l += 1
        
        return "".join(res) + word1[l:] + word2[l:]
