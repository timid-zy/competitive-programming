# Problem: Make Sum Divisible by P   - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0
        
        rs, ans = 0, float('inf')
        dct = {0: -1}
        for i in range(len(nums)):
            rs += nums[i]
            rem = rs % p
            dct[rem] = i
            
            t = (rem - target) % p
            if t in dct:
                ans = min(ans, i - dct[t])
            
        
        return ans if ans < len(nums) else -1