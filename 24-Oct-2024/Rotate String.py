class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            
        target = goal + goal
        lps = [0] * len(s)
        l, r = 0, 1
        while r < len(s):
            if s[l] == s[r]:
                l += 1
                lps[r] = l 
                r += 1
            elif l == 0:
                r += 1
            else:
                l = lps[l-1]
        
        si = ti = 0
        while si < len(s) and ti < len(target):
            if s[si] == target[ti]:
                si += 1; ti += 1
            elif si == 0:
                ti += 1
            else:
                si = lps[si-1]
        
        return si == len(s)