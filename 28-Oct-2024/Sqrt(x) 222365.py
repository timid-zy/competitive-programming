# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            mid = (r + l + 1) // 2
            t = mid ** 2
            if t > x:
                r = mid - 1
            else:
                l = mid 
        
        return l
