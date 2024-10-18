# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        neg = n < 0
        n = abs(n)
        while n > 0:
            if n & 1:
                res *= x

            x *= x
            n >>= 1
        
        return res if not neg else 1/res
