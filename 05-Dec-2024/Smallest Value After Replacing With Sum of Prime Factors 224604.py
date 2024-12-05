# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def get_factors_sum(x):
            i = 2
            res = 0
            while i*i <= x:
                if x % i == 0:
                    res += i
                    x //= i
                else:
                    i += 1
            
            res += x
            return res
        
        t = get_factors_sum(n)
        while t != n:
            n = t
            t = get_factors_sum(n)
        
        return n