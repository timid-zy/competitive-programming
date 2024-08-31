class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)        
        s = ""
        max_len = 0
        i = 0
        while i < len(word):
            s += word[i]
            for key in range(1, 11):
                if s[-1 * key:] in forbidden:
                    max_len = max(max_len, len(s) - 1)
                    s = ""
                    i -= (key - 1)
                    break
            
            i += 1
        
        return max(max_len, len(s))