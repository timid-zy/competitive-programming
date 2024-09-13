# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        evens = [0] * (len(nums) + 1)
        evens[-2] = 1 if nums[-1] % 2 == 0 else 0
        for i in range(len(nums) - 1, -1, -1):
            evens[i] = evens[i+1] + 1 if nums[i] % 2 == 0 else 0
        
        l = res = odds = 0
        for i in range(len(nums)):
            odds += nums[i] % 2
            while odds == k:
                res += evens[i+1] + 1
                odds -= nums[l] % 2
                l += 1
        
        return res
