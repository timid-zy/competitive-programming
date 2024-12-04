class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def solve(si, pi):
            if (si == len(s) and pi == len(p)):
                return True
            
            if pi < len(p) and p[pi] == "*":
                for r in range(si, len(s)+1):
                    if solve(r, pi+1): return True
                
                return False

            if si >= len(s) or pi >= len(p):
                return False
            
            if p[pi] == "?" or p[pi] == s[si]:
                return solve(si+1, pi+1)
            elif p[pi] != "*" and p[pi] != s[si]:
                return False
            
            return False

        return solve(0, 0)