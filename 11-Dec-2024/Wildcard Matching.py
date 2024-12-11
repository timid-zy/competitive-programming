class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        si = pi = sialt = 0
        asterik = -1
        while si < len(s):
            if pi < len(p) and (p[pi] == "?" or p[pi] == s[si]):
                pi += 1
                si += 1
            elif pi < len(p) and p[pi] == "*":
                asterik = pi
                sialt = si
                pi += 1
            elif asterik != -1:
                pi = asterik + 1
                sialt += 1
                si = sialt
            else:
                return False
        
        while pi < len(p) and p[pi] == "*": pi += 1
        return pi == len(p)