class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first, last = {}, {}
        for i, c in enumerate(s):
            last[c] = i
            if c not in first:
                first[c] = i

        curr = {}
        res = 0
        for i, c in enumerate(s): 
            if i == last[c]:
                for k in curr:
                    if first[c] < curr[k] < i:
                        res += 1
                
            curr[c] = i
        
        return res