class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if len(pref) > len(word):
                continue
            
            if pref == word[:len(pref)]:
                res += 1
        
        return res