# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        res = 1
        if n % 2 == 1:
            res = 5
            n -= 1
        
        MOD = 10 ** 9 + 7
        base = 1
        while n > 0:
            if n & 1:
                res = (res * base) % MOD
            
            base = (base ** 2) % MOD if base != 1 else 20
            n >>= 1
        
        return res
