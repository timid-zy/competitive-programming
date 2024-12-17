# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_neg = False
        if n < 0:
            is_neg = True
            n = abs(n)
        
        res = 1
        while n > 0:
            if n & 1:
                res *= x

            x *= x
            n >>= 1
        
        return res if not is_neg else 1/res