# Problem: Make Sum Divisible by P   - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dct = {0: -1}
        ans = float('inf')
        rs = 0
        target = sum(nums) % p
        if target == 0:
            return 0
        
        for i in range(len(nums)):
            rs += nums[i]
            rm = rs % p
            dct[rm] = i
            t = (rm - target) % p
            if t in dct:
                ans = min(ans, i - dct[t])
        
        return ans if ans < len(nums) else -1
