class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def dp(i):
            if i == len(s):
                return 0
            
            res = dp(i+1) + 1
            for j in range(i, len(s)):
                if s[i:j+1] in set_dct:
                    res = min(res, dp(j+1))
            
            return res
        
        set_dct = set(dictionary)
        return dp(0)
