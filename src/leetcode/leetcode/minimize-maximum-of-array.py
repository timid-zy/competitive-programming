import math
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        if max(nums) == nums[0]:
            return nums[0]
        
        r_sum = nums[0]
        mx = nums[0]
        for i in range(1, len(nums)):
            r_sum += nums[i]
            mx = max(mx, math.ceil(r_sum / (i + 1)))
        
        return mx
