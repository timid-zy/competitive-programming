# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def get_pattern(word):
            pattern, mp, idx = [], {}, 0
            for c in word:
                if c not in mp:
                    mp[c] = idx
                    idx += 1
                
                pattern.append(mp[c])
            
            return pattern
            
        pt = get_pattern(pattern)
        res = []
        for word in words:
            if get_pattern(word) == pt:
                res.append(word)
        
        return res

