class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        N = len(nums)
        sieve = [0] * (max(nums) + 1)
        for i in range(2, len(sieve)):
            for j in range(i*i, len(sieve), i):
                sieve[j] = 1
            
        primes = []
        for i in range(2, len(sieve)):
            if sieve[i] == 0:
                primes.append(i)
        
        for i in range(len(nums)):
            if i == 0 and nums[i] <= 2:
                continue
            
            idx = min(len(primes) - 1, bisect.bisect_left(primes, nums[i]))
            if i == 0:
                nums[i] -= primes[idx] if primes[idx] < nums[i] else primes[idx-1]
                continue

            for j in range(idx, -1, -1):
                if nums[i] > primes[j] and nums[i-1] < nums[i] - primes[j]:
                    nums[i] -= primes[j]
                    break
            
            
            if nums[i] <= nums[i-1]:
                return False
        
        return True
            