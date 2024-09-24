# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        sieve = [False] * n
        for i in range(2, n):
            if not sieve[i]:
                count += 1
            
            for j in range(i*2, n, i):
                sieve[j] = True
        
        return count
    