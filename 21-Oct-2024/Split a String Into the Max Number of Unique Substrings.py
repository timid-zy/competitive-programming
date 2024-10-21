class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(prev, i, subs):
            if i == len(s):
                return 0
            
            res = backtrack(prev, i+1, subs)
            ss = s[prev:i+1]
            if ss not in subs:
                subs.add(ss)
                res = max(res, backtrack(i+1, i+1, subs) + 1)
                subs.remove(ss)
            
            return res
        
        return backtrack(0, 0, set())