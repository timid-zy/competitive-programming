class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(i=0, prev=None, firstitr=True):
            if i == len(s):
                return not firstitr
            
            for r in range(i+1, len(s)+1):
                if (prev is None or int(s[i:r]) == prev-1) and backtrack(r, int(s[i:r]), prev is None):
                    return True

            return False
        
        return backtrack()