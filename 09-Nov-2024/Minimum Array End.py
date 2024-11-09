class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        t = n - 1
        pos = 1
        while t > 0:
            if not (x & pos):
                res |= (t & 1) * pos
                
                t >>= 1
            pos <<= 1
    
        return res